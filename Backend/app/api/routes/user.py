from fastapi import APIRouter, Depends
from app.core.auth import get_current_user

user_router = APIRouter()

@user_router.get("/profile")
async def get_profile(user=Depends(get_current_user)):
    return {"id": str(user["_id"]), "email": user["email"]}
