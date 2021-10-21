from fastapi import FastAPI

from .routers import recommendations

app = FastAPI()

app.include_router(recommendations.router)


@app.get("/")
async def welcome():
    return {"message": "Welcome to Vaas!"}
