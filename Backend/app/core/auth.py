from fastapi import Depends,HTTPException,status
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from app.core.security import decode_access_token
from app.core.database import db
security = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = decode_access_token(token)

    if not payload:
        raise HTTPException(status_code=401,detail="Invalid Credentials or expired Token")
    
    user = await db.user.find_one({"email":payload["sub"]})

    if not user:
        raise HTTPException(status_code=401,detail="User not found")
    
    return user