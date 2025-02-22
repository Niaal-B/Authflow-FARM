from pydantic import BaseModel,EmailStr

class UserCreate(BaseModel):
    email : EmailStr
    password : str

class UserResponse(BaseModel):
    id : str
    email : EmailStr

    class Config:
        form_attributes = True