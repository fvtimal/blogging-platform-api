from fastapi import APIRouter, HTTPException

from database import tags

from schemas import TagCreate

router = APIRouter(

    prefix="/tags",

    tags=["Tags"]

)

@router.post("/")
async def create_tag(tag:TagCreate):


    existing = await tags.find_one(
        {
            "name":tag.name
        }
    )


    if existing:

        raise HTTPException(
            status_code=400,
            detail="Tag already exists"
        )


    result = await tags.insert_one(
        {
            "name":tag.name
        }
    )


    return {

        "message":"Tag created",

        "id":str(result.inserted_id)

    }

@router.get("/")
async def get_tags():

    result = await tags.find().to_list(None)


    for tag in result:

        tag["_id"]=str(tag["_id"])


    return result