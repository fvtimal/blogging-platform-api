from pydantic import BaseModel, EmailStr

class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str

class PostCreate(BaseModel):

    title: str

    content: str

    category_id: str

    tags: list[str]

class CommentCreate(BaseModel):
    content : str

class TagCreate(BaseModel):
    name:str