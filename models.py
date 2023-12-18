from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey


class Shoe(Base):
    __tablename__ = "shoes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    size = Column(Integer)
    color = Column(String)
    price = Column(Integer)
    instock = Column(Boolean)
    creator_id = Column(Integer, ForeignKey("users.id"))

    creator = relationship("User", back_populates='shoes')


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)
    email = Column(String)

    shoes = relationship("Shoe", back_populates='creator')
