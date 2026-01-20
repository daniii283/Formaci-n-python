from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

def get_user_by_name(db: Session, username: str) -> User | None:
    return db.query(User).filter(User.username == username).first()

def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user_data: UserCreate, hashed_password: str) -> User:
    db_user = User(username = user_data.username, email = user_data.email, hashed_password = hashed_password)
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user