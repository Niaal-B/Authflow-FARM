from fastapi import APIRouter, Depends,File,UploadFile
from app.core.auth import get_current_user
from app.core.database import db
import os


user_router = APIRouter()

@user_router.get("/profile")
async def get_profile(user=Depends(get_current_user)):
    return {"id": str(user["_id"]),"name":user["name"], "email": user["email"]}


@user_router.put("/profile/update")
async def update_profile(name:str,user=Depends(get_current_user)):
    await db.user.update_one({"_id": user["_id"]},{"$set":{"name" : name}})
    return {"messsage" : "Profile Updated Successfully"}


@user_router.post("/profile/upload")
async def upload_profile_image(file: UploadFile = File(...), user=Depends(get_current_user)):
    # Ensure the 'uploads' directory exists
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)  # Creates if it doesn't exist
    
    # Define file location
    file_location = f"{upload_dir}/{user['_id']}.jpg"

    # Write the file
    with open(file_location, "wb") as buffer:
        buffer.write(file.file.read())

    return {"message": "Profile image uploaded", "file_path": file_location}