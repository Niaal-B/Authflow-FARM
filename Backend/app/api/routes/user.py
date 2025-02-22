from fastapi import APIRouter, Depends
from app.core.auth import get_current_user
from app.core.database import db

user_router = APIRouter()

@user_router.get("/profile")
async def get_profile(user=Depends(get_current_user)):
    return {"id": str(user["_id"]),"name":user["name"], "email": user["email"]}


@user_router.put("/profile/update")
async def update_profile(name:str,user=Depends(get_current_user)):
    await db.user.update_one({"_id": user["_id"]},{"$set":{"name" : name}})
    return {"messsage" : "Profile Updated Successfully"}
