from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.users.router import router as users_router
from src.permission.router import router as permission_router
from src.init_data import init_db_data


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db_data()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(users_router)
app.include_router(permission_router)
