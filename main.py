from fastapi import FastAPI

from routers import (
    users,
    posts,
    comments,
    categories,
    tags
)

app = FastAPI(
    title="Blog API"
)

app.include_router(users.router)

app.include_router(posts.router)

app.include_router(comments.router)

app.include_router(categories.router)

app.include_router(tags.router)