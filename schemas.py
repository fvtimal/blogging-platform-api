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

class MessageResonse(BaseModel):
    message: str
    id: str

class PostResponse(BaseModel):
    id: str
    title: str
    content: str
    categor_id: str
    tags: list[str]
    author_id: str