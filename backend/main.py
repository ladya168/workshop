from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from API.routers.users_router import router_Users
from API.routers.goods_router import router_Goods
from DB.db import create_all_tables, delete_all_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("dropping all tables")
    await delete_all_tables()
    print("creating all tables")
    await create_all_tables()
    yield
    print("App stopped")

app = FastAPI(lifespan=lifespan
)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_Users)
app.include_router(router_Goods)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)