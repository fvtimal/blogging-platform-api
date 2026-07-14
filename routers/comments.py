from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from database import comments, posts
from schemas import CommentCreate
from dependencies import get_current_user
from utils import is_valid_object_id

router = APIRouter(
    prefix="/posts",
    tags=["Comments"]
)

@router.post("/{post_id}/comments")
async def add_comment(
    post_id: str,
    comment: CommentCreate,
    current_user=Depends(get_current_user)
):
    if not is_valid_object_id(post_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid post id"
        )

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

    new_comment = {

        "content": comment.content,

        "post_id": ObjectId(post_id),

        "author_id": current_user["_id"]

    }

    result = await comments.insert_one(
        new_comment
    )
    return {

        "message": "Comment added",

        "id": str(result.inserted_id)

    }


@router.get("/{post_id}/comments")
async def get_comments(post_id:str):

    if not is_valid_object_id(post_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid post id"
        )

    result = await comments.find(
        {
            "post_id": ObjectId(post_id)
        }
    ).to_list(None)
    for comment in result:
        comment["_id"] = str(comment["_id"])

        comment["post_id"] = str(comment["post_id"])

        comment["author_id"] = str(comment["author_id"])

    return result

@router.delete("/comments/{comment_id}")
async def delete_comment(
    comment_id:str,
    current_user=Depends(get_current_user)
):
    if not is_valid_object_id(comment_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid comment id"
        )

    comment = await comments.find_one(
        {
            "_id": ObjectId(comment_id)
        }
    )
    if not comment:
        raise HTTPException(
            status_code=404,
            detail="Comment not found"
        )
    if comment["author_id"] != current_user["_id"]:
        raise HTTPException(
            status_code=403,
            detail="Not allowed"
        )

    await comments.delete_one(
        {
            "_id": ObjectId(comment_id)
        }
    )

    return {
        "message":"comment deleted"
    }