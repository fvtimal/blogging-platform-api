from fastapi import APIRouter, HTTPException
from database import users
from schemas import UserRegister
from utils import hash_password
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from utils import verify_password
from auth import create_access_token



router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/")
async def test():
    return {
        "message": "Users router working!"
    }

@router.post("/register")
async def register(user: UserRegister):

    existing_user = await users.find_one(
        {"email": user.email}
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    hashed = hash_password(user.password)

    new_user = {
        "username": user.username,
        "email": user.email,
        "password": hashed
    }

    result = await users.insert_one(new_user)

    return {
        "message": "User registered successfully",
        "id": str(result.inserted_id)
    }
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await users.find_one(
        {
            "email": form_data.username
        }
    )

    if (
        not user
        or
        not verify_password(
            form_data.password,
            user["password"]
        )
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        {
            "sub": str(user["_id"])
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
