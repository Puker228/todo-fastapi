from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.database import create_tabels, delete_tables
from app.routers.todo_routers import router as todo_router
from app.demo_auth.views import router as demo_auth_router
from app.demo_auth.demo_jwt_auth import router as jwt_router


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
app.include_router(demo_auth_router)
app.include_router(jwt_router)


@app.get("/")
async def root():
    return {"message": "hello"}
