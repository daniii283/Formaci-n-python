from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.schemas.user import UserCreate
from app.repositories import user_repository as repo
from app.core.security import get_password_hash, create_access_token, verify_password

def register_user(db: Session, user_data: UserCreate):
    if repo.get_user_by_email(db, user_data.email) or repo.get_user_by_name(db, user_data.username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "User already exists")
    
    hashed_password = get_password_hash(user_data.password)
    return repo.create_user(db, user_data, hashed_password)


def login_user(db: Session, email: str, password: str):
    user = repo.get_user_by_email(db, email)

    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    token = create_access_token({"sub": user.username})
    return {
        "access_token": token,
        "token_type": "bearer"
    }

