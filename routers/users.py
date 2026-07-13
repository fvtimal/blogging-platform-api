from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/")
async def test():
    return {
        "message": "Users router working!"
    }