from fastapi import APIRouter, status, Depends
import schemas, database
from sqlalchemy.orm import Session
from repository import shoes
from typing import List

router = APIRouter(
    prefix="/shoe",
    tags=["Shoes"]
)

get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowShoe], status_code=status.HTTP_200_OK)
def all_shoe(db: Session = Depends(get_db)):
    return shoes.get_all(db)


@router.get('/{shoe_id}', response_model=schemas.ShowShoe, status_code=status.HTTP_200_OK)
def shoe_by_id(shoe_id, db: Session = Depends(get_db)):
    return shoes.get_by_id(shoe_id, db)


@router.post('/', response_model=schemas.ShowShoe, status_code=status.HTTP_201_CREATED)
def create_shoe(request: schemas.Shoe, db: Session = Depends(get_db)):
    return shoes.create(request, db)


@router.delete('/{shoe_id}', status_code=status.HTTP_200_OK)
def delete_shoe(shoe_id, db: Session = Depends(get_db)):
    return shoes.delete(db, shoe_id)


@router.put('/{shoe_id}', status_code=status.HTTP_202_ACCEPTED)
def update_shoe(shoe_id, request: schemas.Shoe, db: Session = Depends(get_db)):
    return shoes.update(db, shoe_id, request)