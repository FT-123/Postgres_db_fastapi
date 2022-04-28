from typing import List

from uuid import UUID
from fastapi.params import Depends
from pydantic import EmailStr
from sqlalchemy.orm import Session

from User.UsersModels import User
from dependencies import get_db
from schemas.Usersschem import UserCreate


class UserRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def find(self, uuid: UUID) -> User:
        query = self.db.query(User)
        return query.filter(User.id == uuid).first()

    def find_by_email(self, email: EmailStr):
        query = self.db.query(User)
        return query.filter(User.email == email).first()

    def find_by_name(self, username: str):
        query = self.db.query(User)
        return query.filter(User.name == username).first()

    def all(self, skip: int = 0, max: int = 100) -> List[User]:
        query = self.db.query(User)
        return query.offset(skip).limit(max).all()

    def create(self, user: UserCreate) -> User:
        faked_pass_hash = user.password

        db_user = User(
            name=user.name,
            email=user.email,
            password=faked_pass_hash
        )

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        return db_user
