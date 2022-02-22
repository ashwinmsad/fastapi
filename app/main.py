
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.vote import vote
from .database import engine
from . import models
from .routers import post,user,auth,vote


#this code id for creating database tables without alembic
#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#CORSM is for accessing this app from all the websites
# * ,Eg: www.google.com, www.youtube.com
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message":"hello world"}