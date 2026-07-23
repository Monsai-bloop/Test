from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
# User models


class SubscriptionCreate(SQLModel):
	topic: str 



class Subscription(SubscriptionCreate, table=True):
	id: int | None = Field(default=None, primary_key=True)
	user_id: int | None = Field(default=None, foreign_key="user.id")


class UserBase(SQLModel):
	name: str = Field(max_length=255)
	email: str = Field(max_length=255)


class User(UserBase, table=True):
	id: int | None = Field(default=None, primary_key=True)
	password: str = Field(max_length=255)


class UserCreate(UserBase):
	password: str = Field(max_length=255)


class ReadHistory(SQLModel, table=True):
	id: int | None = Field(default=None, primary_key=True)
	user_id: int = Field(foreign_key="user.id")
	article_title: str = Field(max_length=255)
	article_url: str = Field(unique=True, max_length=255)
	read_at: datetime 
