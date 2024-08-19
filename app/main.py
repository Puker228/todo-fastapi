from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.database import init_models
from app.routers.todo_routers import router as todo_router
from app.routers.user_routers import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_models()
    yield
    print("exit")


app = FastAPI(lifespan=lifespan)
app.include_router(todo_router)
app.include_router(user_router)


@app.get("/")
async def root(name: str = 'World!'):
    format_name = name.title().strip()
    return {"message": f"Hello, {format_name}"}
