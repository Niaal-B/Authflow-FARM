from fastapi import FastAPI
from app.core.database import db  
from app.api.routes.auth import auth_router

app = FastAPI(title="FastAPI MongoDB Project")
app.include_router(auth_router,prefix="/auth",tags=["Auth"])


@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI with MongoDB!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
