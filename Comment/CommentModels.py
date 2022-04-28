from sqlalchemy import Column, String, Integer
from auth import hashing
from database import Model
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID


class Comments(Model):
    __tablename__ = "Comments"

    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String)
    comment_owner = Column(String, unique=True, index=True)
    Photo_owner = Column(String, unique=True, index=True)
