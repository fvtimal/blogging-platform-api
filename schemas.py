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