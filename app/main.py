from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.database import create_tabels, delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("db is clear")
    await create_tabels()
    print("db is create")
    yield
    print('exit')


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "hello"}
