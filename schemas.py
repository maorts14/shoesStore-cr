from typing import List, Optional

from pydantic import BaseModel


class User(BaseModel):
    name: str
    password: str
    email: str


class Shoe(BaseModel):
    name: str
    size: int
    color: str
    price: int
    instock: bool
    creator_id: int

    class Config():
        orm_mode = True


class ShowUser(BaseModel):
    name: str
    email: str
    shoes: List[Shoe] = []

    class Config():
        orm_mode = True


class ShowShoe(BaseModel):
    name: str
    size: int
    color: str
    price: int
    instock: bool
    creator: ShowUser

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str
