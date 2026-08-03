 # 🚀 Spam Detection MLOps

An end-to-end Machine Learning and MLOps project for detecting spam messages using FastAPI, JWT Authentication, MongoDB, DVC, DVCLive, and MLflow.

---

# 📌 Project Overview

This project predicts whether a given SMS/message is **Spam** or **Ham** using a Machine Learning model. The project follows a complete MLOps pipeline from data ingestion to deployment-ready APIs.

---

# ✨ Features

- User Registration
- User Login
- JWT Authentication
- Protected APIs
- Spam Prediction API
- MongoDB Integration
- DVC Pipeline
- DVCLive Experiment Tracking
- MLflow Experiment Tracking
- MLflow Model Registry
- Model & Vectorizer Serialization
- Logging
- Production Ready FastAPI Structure

---

# 🛠 Tech Stack

### Machine Learning
- Python
- Scikit-Learn
- Random Forest Classifier
- TF-IDF Vectorizer

### Backend
- FastAPI
- JWT Authentication
- Passlib
- Python-Jose

### Database
- MongoDB

### MLOps
- DVC
- DVCLive
- MLflow

---

# 📂 Project Structure

```
Spam-Detection-MLOPS
│
├── api
│   ├── core
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── password.py
│   │   └── security.py
│   │
│   ├── dependencies
│   │   └── auth_dependencies.py
│   │
│   ├── routers
│   │   ├── auth_router.py
│   │   └── prediction_router.py
│   │
│   ├── schemas
│   │   ├── auth_schema.py
│   │   └── prediction_schema.py
│   │
│   ├── services
│   │   ├── auth_service.py
│   │   └── prediction_service.py
│   │
│   └── main.py
│
├── data
├── models
├── reports
├── logs
├── src
│   ├── data_ingestion.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   └── model_evaluation.py
│
├── dvc.yaml
├── params.yaml
├── requirements.txt
└── README.md
```

---

# ⚙️ ML Pipeline

```
Raw Dataset
      │
      ▼
Data Ingestion
      │
      ▼
Data Preprocessing
      │
      ▼
TF-IDF Feature Engineering
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Save Model & Vectorizer
```

---

# 🤖 Model

- Random Forest Classifier
- TF-IDF Vectorizer
- Max Features = 500

---

# 📊 Model Performance

| Metric | Score |
|---------|--------|
| Accuracy | **96.6%** |
| Precision | **96.6%** |
| Recall | **77.9%** |
| ROC-AUC | **97.8%** |

---

# 🔐 Authentication

The project uses JWT Authentication.

### APIs

### Register

```
POST /auth/register
```

### Login

```
POST /auth/login
```

### Current User

```
GET /auth/me
```

---

# 📩 Prediction API

```
POST /prediction/predict
```

### Request

```json
{
    "text":"Congratulations! You won a free iPhone."
}
```

### Response

```json
{
    "prediction":"SPAM"
}
```

---

# 🗄 Database

MongoDB is used for:

- User Authentication
- User Information

---

# 📦 MLOps

### DVC

Used for

- Data Versioning
- Pipeline Management

Pipeline Stages

- Data Ingestion
- Data Preprocessing
- Feature Engineering
- Model Training
- Model Evaluation

---

### DVCLive

Used for

- Metrics Tracking
- Parameter Tracking

---

### MLflow

Used for

- Experiment Tracking
- Parameter Logging
- Metric Logging
- Model Logging
- Model Registry

---

# 🚀 Run Project

## Clone Repository

```bash
git clone <repository-url>
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run DVC Pipeline

```bash
dvc repro
```

## Run FastAPI

```bash
uvicorn api.main:app --reload
```

## Swagger

```
http://127.0.0.1:8000/docs
```

## Run MLflow

```bash
mlflow ui
```

Open

```
http://127.0.0.1:5000
```

---

# 🔥 Future Improvements

- Docker
- Docker Compose
- React Frontend
- Prediction History
- GitHub Actions CI/CD
- AWS Deployment
- Model Monitoring

---

# 👨‍💻 Author

**Anushka Singh**

AI & Data Science Student

Machine Learning | MLOps | FastAPI | DVC | MLflow
