import joblib
from datetime import datetime
from api.core.database import prediction_collection
from src.data_preprocessing import transform_text

model=joblib.load("models/model.pkl")
vectorizer=joblib.load("models/vectorizer.pkl")
SPAM_THRESHOLD = 0.4


def predict_message(text:str,email:str):
    processed_text = transform_text(text)
    text_vectorized=vectorizer.transform([processed_text])
    probabilities = model.predict_proba(text_vectorized)[0]
    spam_probability = probabilities[1] if len(probabilities) > 1 else 0.0
    prediction_index = 1 if spam_probability >= SPAM_THRESHOLD else 0
    result = "SPAM" if prediction_index == 1 else "HAM"

    prediction_data={
        "email":email,
        "text":text,
        "prediction":result,
        "created_at":datetime.utcnow()
        }
    prediction_collection.insert_one(prediction_data)
    return prediction_data
