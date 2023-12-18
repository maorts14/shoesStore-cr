from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import models, schemas
from hashing import Hash


def create(request: schemas.User, db: Session):
    new_user = models.User(name=request.name, password=Hash.bcrypt(request.password), email=request.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all(db: Session):
    users = db.query(models.User).all()
    return users


def get_by_id(user_id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} was not found")
    return user


def delete(user_id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Shoe with id {user_id} was not found")
    db.delete(user)
    db.commit()
    return f"The shoe with id {user_id} has been deleted"
