from pydantic import BaseModel
from datetime import datetime

class PredictionRequest(BaseModel):
    text:str

class PredictionResponse(BaseModel):
    prediction:str
    text:str
    created_at:datetime