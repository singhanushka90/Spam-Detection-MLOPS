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
    existing_user=users_collection.find_one({"email":user.email})
    if existing_user:
        raise ValueError("Email Registerd aleady")
    hashed_password=hash_password(user.password)

    users_data={
        "username":user.username,
        "email":user.email,
        "password":hashed_password
    }
    users_collection.insert_one(users_data)
    return UserResponse(username=user.username,email=user.email)


def login_user(form_data:OAuth2PasswordRequestForm)->TokenResponse:
    db_user=users_collection.find_one({"email":form_data.username})
    if not db_user:
        raise ValueError("Invalid Email or Passowrd")

    if not verify_password(form_data.password,db_user["password"]):
         raise ValueError("Invalid Email or Passowrd")
    access_token=create_access_token(
        data={"sub":db_user["email"],
        "username":db_user["username"],
        }
    )

    return TokenResponse(
        access_token=access_token,
        token_type="bearer"
    )