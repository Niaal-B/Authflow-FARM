from fastapi import FastAPI
from app.core.database import db  
from app.api.routes.auth import auth_router
from app.api.routes.user import user_router
from app.api.routes.admin import admin_router

app = FastAPI(title="FastAPI MongoDB Project")
app.include_router(auth_router,prefix="/auth",tags=["Auth"])
app.include_router(user_router,prefix="/user",tags=["User"])
app.include_router(admin_router,prefix="/admin",tags=["Admin"])

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI with MongoDB!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
