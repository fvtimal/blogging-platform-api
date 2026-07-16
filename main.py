from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


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

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(req, exc):
    return JSONResponse(status_code=422, content={"detail": exc.errors()})

app.include_router(users.router)

app.include_router(posts.router)

app.include_router(comments.router)

app.include_router(categories.router)

app.include_router(tags.router)