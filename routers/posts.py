from fastapi import APIRouter, Depends, HTTPException

from bson import ObjectId

from database import posts

from dependencies import get_current_user

from schemas import PostCreate


router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.post("/")
async def create_post(
    post: PostCreate,
    current_user=Depends(get_current_user)
):
    new_post = {
        "title": post.title,
        "content": post.content,
        "category_id": ObjectId(post.category_id),
        "tags": post.tags,
        "author_id": current_user["_id"]
    }

    result = await posts.insert_one(new_post)

    return {
        "message": "Post created successfully",
        "id": str(result.inserted_id)
    }

@router.get("/")
async def get_posts():

    all_posts = await posts.find().to_list(None)

    for post in all_posts:
        post["_id"] = str(post["_id"])
        post["author_id"] = str(post["author_id"])
        post["category_id"] = str(post["category_id"])

    return all_posts

@router.get("/{post_id}")
async def get_post(post_id: str):
    post = await posts.find_one(
        {
            "_id": ObjectId(post_id)
        }
    )

    if not post:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )
    post["_id"] = str(post["_id"])
    post["author_id"] = str(post["author_id"])
    post["category_id"] = str(post["category_id"])

    return post

