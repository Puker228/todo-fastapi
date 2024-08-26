from fastapi import FastAPI
from contextlib import asynccontextmanager
from asgi_lifespan import LifespanManager

from app.database import init_models, drop_models
from app.routers.todo import router as todo_router

# from app.routers.user_routers import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_models()
    yield
    await drop_models()


app = FastAPI(lifespan=lifespan)
app.include_router(todo_router)
# app.include_router(user_router)


@app.get("/")
async def root():
    return {"ping": "pong"}
