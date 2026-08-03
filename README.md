Spam Detection MLOps

A production-ready Machine Learning project for SMS Spam Detection built with FastAPI, MongoDB, JWT Authentication, DVC, DVCLive, and MLflow. This project follows an end-to-end MLOps workflow including data versioning, model training, experiment tracking, API development, and model management.

Features

- User Registration & Login
- JWT Authentication
- Protected Prediction API
- SMS Spam Detection
- TF-IDF Feature Engineering
- Random Forest Classifier
- MongoDB Integration
- DVC Pipeline
- DVCLive Experiment Tracking
- MLflow Experiment Tracking
- MLflow Model Registry
- Logging
- Environment Variable Configuration

Tech Stack

Machine Learning

- Python
- Scikit-learn
- Random Forest
- TF-IDF Vectorizer
- Pandas
- NumPy

Backend

- FastAPI
- Pydantic
- JWT Authentication
- Passlib (bcrypt)
- Python-Jose

Database

- MongoDB

MLOps

- DVC
- DVCLive
- MLflow

Project Structure

Spam-Detection-MLOPS/
│
├── api/
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── password.py
│   │   └── security.py
│   │
│   ├── dependencies/
│   │   └── auth_dependencies.py
│   │
│   ├── routers/
│   │   ├── auth_router.py
│   │   └── prediction_router.py
│   │
│   ├── schemas/
│   │   ├── auth_schema.py
│   │   └── prediction_schema.py
│   │
│   ├── services/
│   │   ├── auth_services.py
│   │   └── prediction_service.py
│   │
│   └── main.py
│
├── src/
│   ├── data_ingestion.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   └── model_evaluation.py
│
├── data/
├── models/
├── reports/
├── logs/
├── dvclive/
├── experiments/
├── params.yaml
├── dvc.yaml
├── requirements.txt
└── README.md

Machine Learning Pipeline

Raw Dataset
     ↓
Data Ingestion
     ↓
Data Preprocessing
     ↓
TF-IDF Feature Engineering
     ↓
Random Forest Training
     ↓
Model Evaluation
     ↓
Model Saving

Authentication Flow

Register User
     ↓
Password Hashing
     ↓
MongoDB
     ↓
Login
     ↓
JWT Token
     ↓
Protected APIs

Prediction Flow

User Message
     ↓
JWT Verification
     ↓
Load TF-IDF Vectorizer
     ↓
Transform Text
     ↓
Load Random Forest Model
     ↓
Prediction
     ↓
Spam / Ham

Model Performance

Metric| Score
Accuracy| 0.966
Precision| 0.966
Recall| 0.779
ROC-AUC| 0.978

API Endpoints

Authentication

Method| Endpoint| Description
POST| "/auth/register"| Register User
POST| "/auth/login"| Login User
GET| "/auth/me"| Get Current User

Prediction

Method| Endpoint| Description
POST| "/prediction/predict"| Predict Spam/Ham

MLOps Components

DVC

- Data Versioning
- Pipeline Automation
- Reproducible Experiments

DVCLive

- Metrics Tracking
- Parameter Tracking

MLflow

- Experiment Tracking
- Parameter Logging
- Metric Logging
- Model Artifact Logging
- Model Registry

Getting Started

Clone Repository

git clone https://github.com/your-username/Spam-Detection-MLOPS.git
cd Spam-Detection-MLOPS

Install Dependencies

pip install -r requirements.txt

Run DVC Pipeline

dvc repro

Run FastAPI

uvicorn api.main:app --reload

Swagger API Documentation

http://127.0.0.1:8000/docs

Run MLflow UI

mlflow ui

Open:

http://127.0.0.1:5000

Current Project Status

- End-to-End ML Pipeline
- FastAPI Backend
- MongoDB Integration
- JWT Authentication
- Protected Prediction API
- DVC Pipeline
- DVCLive Integration
- MLflow Experiment Tracking
- MLflow Model Registry
- Production-Ready Project Structure

Upcoming Features

- Docker
- Docker Compose
- React Frontend
- Prediction History
- GitHub Actions (CI/CD)
- AWS Deployment

Author

Anushka Singh

AI & Data Science Student | Machine Learning | MLOps | FastAPI | DVC | MLflow | MongoDB | JWT

If you like this project, consider giving it a star on GitHub.
