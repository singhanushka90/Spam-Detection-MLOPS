from fastapi import Depends , HTTPException , status
from fastapi.security import OAuth2PasswordBearer
from api.core.security import verify_access_token
from api.core.database import users_collection

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token:str=Depends(oauth2_scheme)):
    payload=verify_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or Expired Token",
            headers={"WWW-Authenticate":"Bearer"}
        )
    email=payload.get("sub")
    if email is None:
         raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token")
    user=users_collection.find_one({'email':email})
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Not Found")
    return user


