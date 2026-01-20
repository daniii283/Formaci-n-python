from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.models.user import User
from app.db.session import get_db
from app.core.dependencies import get_current_user
from fastapi.security import OAuth2PasswordRequestForm
from app.services.user_service import login_user

router = APIRouter()

from app.services.user_service import register_user

@router.post("/register", response_model=UserOut)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user_in)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return login_user(db, form_data.username, form_data.password)

@router.get("/me", response_model= UserOut)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
