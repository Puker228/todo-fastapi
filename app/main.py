from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
import starlette.status as status

from app.database import create_tabels, delete_tables
from app.routers.todo_routers import router as todo_router


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


@app.get("/")
async def root():
    return RedirectResponse(url="/docs", status_code=status.HTTP_302_FOUND)
