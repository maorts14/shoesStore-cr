from fastapi import APIRouter, status, Depends
import schemas, database
from sqlalchemy.orm import Session
from repository import users
from typing import List

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return users.create(request, db)


@router.get('/', response_model=List[schemas.ShowUser])
def get_all(db: Session = Depends(get_db)):
    return users.get_all(db)


@router.get('/{user_id}', response_model=schemas.ShowUser, status_code=status.HTTP_200_OK)
def get_user(user_id, db: Session = Depends(get_db)):
    return users.get_by_id(user_id, db)


@router.delete('/{user_id}', status_code=status.HTTP_200_OK)
def delete_user(user_id, db: Session = Depends(get_db)):
    return users.delete(user_id, db)
