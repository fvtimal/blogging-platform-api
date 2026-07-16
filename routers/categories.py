from fastapi import APIRouter,   Depends, HTTPException

from database import categories

from pydantic import BaseModel
from dependencies import get_current_user


router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


class CategoryCreate(BaseModel):
    name: str

@router.post("/")
async def create_category(category: CategoryCreate, current_user=Depends(get_current_user)):

    existing = await categories.find_one(
        {
            "name": category.name
        }
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Category already exists"
        )


    result = await categories.insert_one(
        {
            "name": category.name
        }
    )


    return {
        "message": "Category created",
        "id": str(result.inserted_id)
    }

@router.get("/")
async def get_categories():

    result = await categories.find().to_list(None)


    for category in result:
        category["_id"] = str(category["_id"])


    return result



