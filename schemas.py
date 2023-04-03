from typing import Optional
from graphene_sqlalchemy import SQLAlchemyObjectType
from pydantic import BaseModel

from models import Book


class BookSchema(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True



class BookModel(SQLAlchemyObjectType):
    class Meta:
        model = Book