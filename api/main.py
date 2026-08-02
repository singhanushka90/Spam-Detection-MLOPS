from fastapi import FastAPI
from api.router.auth_router import router as auth_router
from api.router.prediction_router import router as prediction_router

app=FastAPI(
    title="Spam Detection API",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(prediction_router)

@app.get("/")
def home():
    return {"message":"Spam Detection API Running"}