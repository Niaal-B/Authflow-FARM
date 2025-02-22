from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta,timezone
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"])


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str,hashed_password: str) -> bool:
    return pwd_context.verify(plain_password,hashed_password)


def create_access_token(data: dict,expires_delta: timedelta = timedelta(hours=1)):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta 
    to_encode.update({"exp" : expire})
    return jwt.encode(to_encode,settings.JWT_SECRET,algorithm=settings.JWT_ALGORITHM)

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token,settings.JWT_SECRET,algorithms=[settings.JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None