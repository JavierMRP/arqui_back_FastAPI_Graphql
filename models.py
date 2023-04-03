from db import Base
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.sql.sqltypes import Integer, String

class Book(Base):
    __tablename__ ="book"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
