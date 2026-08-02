from api.schemas.prediction_schema import PredictionRequest , PredictionResponse
from api.dependencies.auth_dependencies import get_current_user
from api.services.prediction_service import predict_message
from api.core.database import prediction_collection
from fastapi import APIRouter , Depends


router=APIRouter(prefix="/prediction",tags=["Prediction"])
@router.post("/predict",response_model=PredictionResponse)
def predict(request:PredictionRequest,current_user=Depends(get_current_user)):
    return predict_message(
        request.text,
        current_user["email"]
    )
    
@router.get("/history")
def prediction_history(current_user=Depends(get_current_user)):
    history=list(
        prediction_collection.find(
            {"email": current_user["email"]},
            {"_id": 0}
       )
    )
    return history   