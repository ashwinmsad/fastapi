from datetime import datetime
from pydantic import BaseModel,EmailStr, conint
from typing import Optional

class PostBase(BaseModel):
    title:str
    content:str
    published:bool=True
    #rating:Optional[int]=0

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class Post(PostBase):
    id:int
    create_at:datetime
    owner_id:int
    Owner:UserOut
    #rating:Optional[int]=0

    class Config:
        orm_mode = True

class PostOut(BaseModel):
    post: Post
    votes: int

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email:EmailStr
    password:str


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)

