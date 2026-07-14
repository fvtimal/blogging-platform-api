from fastapi import APIRouter, Depends, HTTPException, Query

from bson import ObjectId

from database import posts, comments, tags

from dependencies import get_current_user

from schemas import PostCreate, MessageResonse


router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


# ---------------- CREATE POST ----------------

@router.post("/",response_model = MessageResonse)
async def create_post(
    post: PostCreate,
    current_user=Depends(get_current_user)
):

    # Check tags exist
    for tag in post.tags:

        existing_tag = await tags.find_one(
            {
                "_id": ObjectId(tag)
            }
        )

        if not existing_tag:
            raise HTTPException(
                status_code=404,
                detail=f"Tag {tag} not found"
            )


    new_post = {

        "title": post.title,

        "content": post.content,

        "category_id": ObjectId(post.category_id),

        "tags": [
            ObjectId(tag)
            for tag in post.tags
        ],

        "author_id": current_user["_id"]

    }


    result = await posts.insert_one(new_post)


    return {
        "message": "Post created successfully",
        "id": str(result.inserted_id)
    }



# ---------------- GET ALL POSTS WITH PAGINATION ----------------

@router.get("/")
async def get_posts(
    page:int = Query(1, ge=1),
    limit:int = Query(10, ge=1, le=100)
):

    skip = (page - 1) * limit


    result = await posts.find() \
        .skip(skip) \
        .limit(limit) \
        .to_list(None)


    for post in result:

        post["_id"] = str(post["_id"])

        post["author_id"] = str(post["author_id"])

        post["category_id"] = str(post["category_id"])

        post["tags"] = [
            str(tag)
            for tag in post["tags"]
        ]


    return {

        "page": page,

        "limit": limit,

        "posts": result
    }



# ---------------- SEARCH POSTS ----------------

@router.get("/search")
async def search_posts(
    q:str
):

    results = await posts.find(

        {
            "$or":[

                {
                    "title":{
                        "$regex":q,
                        "$options":"i"
                    }
                },

                {
                    "content":{
                        "$regex":q,
                        "$options":"i"
                    }
                }

            ]
        }

    ).to_list(None)



    for post in results:

        post["_id"] = str(post["_id"])

        post["author_id"] = str(post["author_id"])

        post["category_id"] = str(post["category_id"])

        post["tags"] = [
            str(tag)
            for tag in post["tags"]
        ]


    return results




# ---------------- GET SINGLE POST ----------------

@router.get("/{post_id}")
async def get_post(post_id:str):

    post = await posts.find_one(
        {
            "_id":ObjectId(post_id)
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

    post["tags"] = [
        str(tag)
        for tag in post["tags"]
    ]


    return post




# ---------------- UPDATE POST ----------------

@router.put("/{post_id}")
async def update_post(
    post_id:str,
    post:PostCreate,
    current_user=Depends(get_current_user)
):

    existing_post = await posts.find_one(
        {
            "_id":ObjectId(post_id)
        }
    )


    if not existing_post:

        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )


    if existing_post["author_id"] != current_user["_id"]:

        raise HTTPException(
            status_code=403,
            detail="Not allowed"
        )


    # validate tags

    for tag in post.tags:

        existing_tag = await tags.find_one(
            {
                "_id":ObjectId(tag)
            }
        )


        if not existing_tag:

            raise HTTPException(
                status_code=404,
                detail=f"Tag {tag} not found"
            )


    await posts.update_one(

        {
            "_id":ObjectId(post_id)
        },

        {

            "$set":{

                "title":post.title,

                "content":post.content,

                "category_id":ObjectId(post.category_id),

                "tags":[
                    ObjectId(tag)
                    for tag in post.tags
                ]

            }

        }

    )


    return {
        "message":"Post updated"
    }




# ---------------- DELETE POST ----------------

@router.delete("/{post_id}")
async def delete_post(
    post_id:str,
    current_user=Depends(get_current_user)
):

    post = await posts.find_one(
        {
            "_id":ObjectId(post_id)
        }
    )


    if not post:

        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )


    if post["author_id"] != current_user["_id"]:

        raise HTTPException(
            status_code=403,
            detail="Not allowed"
        )


    # delete comments first

    await comments.delete_many(

        {
            "post_id":ObjectId(post_id)
        }

    )


    # delete post

    await posts.delete_one(

        {
            "_id":ObjectId(post_id)
        }

    )


    return {
        "message":"Post deleted"
    }