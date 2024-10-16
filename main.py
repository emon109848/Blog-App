from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from exception import StroyException
from router import blog_get,blog_post,user, article, product, file
from auth import authentication
from db import models
from db.database import engine
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(authentication.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router) 
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(file.router)

models.Base.metadata.create_all(engine)

@app.exception_handler(StroyException)
def story_exception_handler(request: Request, exc: StroyException):
    return JSONResponse(
        status_code=418,
        content={'detail':exc.name}
    )


app.mount("/files", StaticFiles(directory="files"), name="files")