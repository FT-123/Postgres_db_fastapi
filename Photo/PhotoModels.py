from sqlalchemy import Column, String, Integer
from auth import hashing
from database import Model
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID


class Photo(Model):
    __tablename__ = "Photos"

    id = Column(Integer, primary_key=True, index=True)
    photo_file = Column(String, unique=True, index=True)
    photo_dis = Column(String)
    photo_owner = Column(String, unique=True, index=True)

