from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker 
from sqlmodel.ext.asyncio.session import AsyncSession
from contextlib import asynccontextmanager
from typing import Annotated
from fastapi import Depends, BackgroundTasks
import os 
from PersonalNews.config import settings

postgresql_url = os.getenv("DATABASE_URL", settings.POSTGRES_URL)
engine = create_async_engine(postgresql_url, echo=True, future=True)

async_session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(
    engine, 
    expire_on_commit=False, #hello
    class_=AsyncSession
)

async def get_session():
	async with async_session_maker() as session:
		yield session 
	
SessionDep = Annotated[AsyncSession, Depends(get_session)]