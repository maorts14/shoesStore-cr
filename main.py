from fastapi import FastAPI

from routers import shoes, users, authentication
import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(authentication.router)
app.include_router(shoes.router)
app.include_router(users.router)


