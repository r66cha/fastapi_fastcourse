from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_table, drop_table
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_table()
    print("--db was cler")
    await create_table()
    print("--db was created")
    yield
    print("--reload")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
