from fastapi import FastAPI

from .routers import recommendations
from .routers import email_validation

app = FastAPI()

app.include_router(recommendations.router)
app.include_router(email_validation.router)

@app.get("/")
async def welcome():
    return {"message": "Welcome to Vaas!"}
