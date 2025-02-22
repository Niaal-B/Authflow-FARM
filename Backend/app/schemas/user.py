from pydantic import BaseModel,EmailStr

class UserCreate(BaseModel):
    name : str
    email : EmailStr
    password : str

class UserResponse(BaseModel):
    name : str
    id : str
    email : EmailStr

    class Config:
        form_attributes = True


class UserLogin(BaseModel):
    email : EmailStr
    password : str