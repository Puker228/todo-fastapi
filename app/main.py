from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.database import create_tabels, delete_tables
from app.routers.todo_routers import router as todo_router
from app.routers.user_routers import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("db is clear")
    await create_tabels()
    print("db is create")
    yield
    print("exit")


app = FastAPI(lifespan=lifespan)
app.include_router(todo_router)
app.include_router(user_router)


@app.get("/")
async def root():
    return {"message": "hello"}
