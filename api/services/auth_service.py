from api.core.database import users_collection
from api.core.password import hash_password,verify_password
from fastapi.security import OAuth2PasswordRequestForm
from api.core.security import create_access_token
from api.schemas.auth_schema import (
    RegisterRequest,
    TokenResponse,
    UserResponse
)

def register_user(user:RegisterRequest)->UserResponse:
    normalized_email = user.email.strip().lower()
    normalized_username = user.username.strip()

    if not normalized_email or "@" not in normalized_email or "." not in normalized_email.split("@")[-1]:
        raise ValueError("Please enter a valid email address")

    if len(user.password) < 8:
        raise ValueError("Password must be at least 8 characters long")

    existing_user=users_collection.find_one({"email": normalized_email})
    if existing_user:
        raise ValueError("Email already registered")
    hashed_password=hash_password(user.password)

    users_data={
        "username": normalized_username,
        "email": normalized_email,
        "password":hashed_password
    }
    users_collection.insert_one(users_data)
    return UserResponse(username=normalized_username,email=normalized_email)


def login_user(form_data:OAuth2PasswordRequestForm)->TokenResponse:
    email = form_data.username.strip().lower()
    db_user=users_collection.find_one({"email": email})
    if not db_user:
        raise ValueError("Invalid Email or Password")

    if not verify_password(form_data.password,db_user["password"]):
         raise ValueError("Invalid Email or Password")
    access_token=create_access_token(
        data={"sub":db_user["email"],
        "username":db_user["username"],
        }
    )

    return TokenResponse(
        access_token=access_token,
        token_type="bearer"
    )