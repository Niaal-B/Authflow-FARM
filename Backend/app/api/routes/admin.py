from fastapi import APIRouter, Depends
from app.core.auth import get_current_admin
from app.core.database import db
from bson import ObjectId

admin_router = APIRouter()

@admin_router.get("/users")
async def list_users(search: str = "", limit: int = 10, page: int = 1, admin=Depends(get_current_admin)):
    query = {"email": {"$regex": search, "$options": "i"}} if search else {}
    users = await db.user.find(query).skip((page - 1) * limit).limit(limit).to_list(length=limit)
    
    return [{"id": str(user["_id"]), "email": user["email"]} for user in users]
