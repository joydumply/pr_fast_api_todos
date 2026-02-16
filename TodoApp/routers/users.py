from typing import Annotated

from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status, Path, Body
from database import SessionLocal
from .admin import db_dependency, user_dependency
from .auth import get_current_user
from models import Users

router = APIRouter(
    prefix='/users',
    tags=['users']
)

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get('/', status_code=status.HTTP_200_OK)
async def get_user(user:user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Auth failed")
    return db.query(Users).filter(Users.id == user.get('id')).first()

@router.put('/password', status_code=status.HTTP_202_ACCEPTED)
async def change_user_password(user:user_dependency, db: db_dependency, password: str = Body(min_length=6)):

    user_model = db.query(Users).filter(Users.id == user.get('id')).first()
    if user_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found in db')

    user_model.hashed_password = bcrypt_context.hash(password)

    db.add(user_model)
    db.commit()
