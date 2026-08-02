from api.schemas.auth_schema import RegisterRequest , UserResponse , TokenResponse
from api.dependencies.auth_dependencies import get_current_user
from api.services.auth_service import register_user,login_user
from fastapi import APIRouter , HTTPException , status , Depends
from fastapi.security import OAuth2PasswordRequestForm

router=APIRouter(prefix="/auth",tags=["Authentication"])

@router.post("/register",response_model=UserResponse,status_code=status.HTTP_201_CREATED)
def register(user:RegisterRequest):
    try:
        return register_user(user)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,detail=str(e)
        )
        

@router.post("/login",response_model=TokenResponse)
def login(form_data:OAuth2PasswordRequestForm=Depends()):
    try:
        return login_user(form_data)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,detail=str(e)
        )

@router.get("/me")
def get_info(current_user=Depends(get_current_user)):
    return{
        "username":current_user["username"],
        "email":current_user["email"]
    }