from sqlalchemy import Column, String, Integer
from auth import hashing
from database import Model
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID


class User(Model):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    def __init__(self, name, email, password, *args, **kwargs):
        self.name = name
        self.email = email
        self.password = hashing.get_password_hash(password)

    def check_password(self, password):
        return hashing.verify_password(self.password, password)


class Photo(Model):
    __tablename__ = "Photos"

    id = Column(Integer, primary_key=True, index=True)
    photo_file = Column(String, unique=True, index=True)
    photo_dis = Column(String)
    photo_owner = Column(String, unique=True, index=True)


class Comments(Model):
    __tablename__ = "Comments"

    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String)
    comment_owner = Column(String, unique=True, index=True)
    Photo_owner = Column(String, unique=True, index=True)
