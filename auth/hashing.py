from passlib.context import CryptContext


pwd_contex = CryptContext(schemes=["argon2"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_contex.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_contex.hash(password)
