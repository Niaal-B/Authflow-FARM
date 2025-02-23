from fastapi import APIRouter,HTTPException
from app.schemas.user import UserCreate,UserResponse,UserLogin
from app.core.database import db
from app.core.security import hash_password,verify_password,create_access_token

auth_router = APIRouter()

@auth_router.post("/register",response_model=UserResponse)
async def register_user(user: UserCreate):
    existing_user = await db.user.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400,detail="Email Already Registered")

    hashed_password = hash_password(user.password)
    user_data = {"name":user.name,"email":user.email,"password": hashed_password,"role": "user"}
    result = await db.user.insert_one(user_data)
    return UserResponse(id=str(result.inserted_id), email=user.email,name=user.name)


@auth_router.post("/login")
async def login_user(user: UserLogin):
    existing_user = await db.user.find_one({"email": user.email})
    if not existing_user or not verify_password(user.password, existing_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}