from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker 
from sqlmodel.ext.asyncio.session import AsyncSession 
from contextlib import asynccontextmanager
from typing import Annotated
from fastapi import Depends, BackgroundTasks
import os 

postgresql_url = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:1427109t531@localhost:5432/PersonalNews")
engine = create_async_engine(postgresql_url, echo=True, future=True)

async_session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(
    engine, 
    expire_on_commit=False, #hello
    class_=AsyncSession
)
@asynccontextmanager
async def create_db():
	async with engine.begin() as conn:
		try:
			yield await conn.run_sync(SQLModel.metadata.create_all)
		finally:
			pass

async def get_session():
	async with async_session_maker() as session:
		yield session 
	
SessionDep = Annotated[AsyncSession, Depends(get_session)]