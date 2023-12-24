# cr - move to models directory as well, split into seperate files
# and the classes that exist also in models can be merged into 
# one class that have the ability to act as sql class

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


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None