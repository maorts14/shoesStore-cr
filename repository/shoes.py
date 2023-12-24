from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import models
import schemas


def get_all(db: Session):
    shoes = db.query(models.Shoe).all()
    if not shoes: # cr - i wouldnt throw exception for that, its legitimate to return 0 results
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There are no shoes in store")
    return shoes


def get_by_id(shoe_id: int, db: Session):
    shoe = db.query(models.Shoe).filter(models.Shoe.id == shoe_id).first()
    if not shoe: # cr - i wouldnt throw exception for that, its legitimate to return 0 results
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Shoe with id {shoe_id} was not found")
    return shoe


def create(request: schemas.Shoe, db: Session):
    new_shoe = models.Shoe(name=request.name, size=request.size, color=request.color, price=request.price,
                           instock=request.instock, creator_id=request.creator_id)
    db.add(new_shoe)
    db.commit()
    db.refresh(new_shoe)
    return new_shoe


def delete(db: Session, shoe_id: int):
    shoe = db.query(models.Shoe).filter(models.Shoe.id == shoe_id).first()
    if not shoe:  # cr - this for example is a good exception , because the user shouldnt ask to delete something that is not exist
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Shoe with id {shoe_id} was not found")
    db.delete(shoe)
    db.commit()
    return f"The shoe with id {shoe_id} has been deleted"


def update(db: Session, shoe_id: int, request: schemas.Shoe):
    shoe = db.query(models.Shoe).filter(models.Shoe.id == shoe_id)
    if not shoe.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Shoe with id {shoe_id} was not found")
    shoe.update(request)
    db.commit()
    return f"The shoe with id {shoe_id} has been updated"
