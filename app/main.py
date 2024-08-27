from fastapi import FastAPI
from contextlib import asynccontextmanager

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from redis import asyncio as aioredis

from database import drop_models, init_models
from todo.router import router as todo_router
from users.router import router as user_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    await drop_models()
    await init_models()
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(todo_router)
app.include_router(user_router)


@cache()
async def get_cache():
    return 1


@app.get("/")
@cache(expire=60)
async def root():
    return dict(hello="world")
