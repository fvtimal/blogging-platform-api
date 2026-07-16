from pydantic import BaseModel, EmailStr, field_validator

class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def password_strength(cls,v:str) -> str:
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")
        return v


class PostCreate(BaseModel):

    title: str

    content: str

    category_id: str

    tags: list[str]

class CommentCreate(BaseModel):
    content : str

class TagCreate(BaseModel):
    name:str

class MessageResponse(BaseModel):
    message: str
    id: str

class PostResponse(BaseModel):
    id: str
    title: str
    content: str
    category_id: str
    tags: list[str]
    author_id: str