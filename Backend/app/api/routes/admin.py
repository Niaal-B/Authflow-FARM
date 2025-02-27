from fastapi import APIRouter, Depends
from app.core.auth import get_current_admin
from app.core.database import db
from bson import ObjectId

admin_router = APIRouter()

@admin_router.get("/users")
async def list_users(search: str = "", limit: int = 10, page: int = 1, admin=Depends(get_current_admin)):
    query = {"email": {"$regex": search, "$options": "i"}} if search else {}
    users = await db.user.find(query).skip((page - 1) * limit).limit(limit).to_list(length=limit)
    print(users)
    return [{"id": str(user["_id"]),"name": user["name"] , "email": user["email"],} for user in users]


@admin_router.put("/users/{user_id}")
async def update_user(user_id: str,name: str,admin=Depends(get_current_admin)):
    await db.user.update_one({"_id":ObjectId(user_id)},{"$set": {"name": name}})
    return {"message":"User updated"}