from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.router.auth_router import router as auth_router
from api.router.prediction_router import router as prediction_router

app = FastAPI(
    title="Spam Detection API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_origin_regex=r"https?://(localhost|127\.0\.0\.1)(:\d+)?$",
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(prediction_router)

@app.get("/")
def home():
    return {"message": "Spam Detection API Running"}