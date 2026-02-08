from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Users
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm

#app = FastAPI() # Creates a new instance of APP

router = APIRouter()

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return True

@router.post("/auth", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    #create_user_model = Users(**create_user_request.model_dump()) # Will fire an error because CreateUserRequest has "password" field, not "hashed_password" field\

    is_username_occupied = bool(db.query(Users).filter(Users.username == create_user_request.username).first())
    is_email_occupied = bool(db.query(Users).filter(Users.email == create_user_request.email).first())

    if is_username_occupied:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username is already registered")

    if is_email_occupied:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")


    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True
    )

    db.add(create_user_model)
    db.commit()

@router.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        return 'Failed Auth'
    return 'Successful Auth'