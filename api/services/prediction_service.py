import joblib
from datetime import datetime
from api.core.database import prediction_collection

model=joblib.load("models/model.pkl")
vectorizer=joblib.load("models/vectorizer.pkl")

def predict_message(text:str,email:str):
    text_vectorized=vectorizer.transform([text])
    prediction=model.predict(text_vectorized)[0]
    result="SPAM" if prediction==1 else "HAM"

    prediction_data={
        "email":email,
        "text":text,
        "prediction":result,
        "created_at":datetime.utcnow()
        }
    prediction_collection.insert_one(prediction_data)
    return prediction_data
