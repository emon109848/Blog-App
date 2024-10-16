from typing import List, Optional
from fastapi import APIRouter, Body, Path, Query
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog']

)

class BlogModel(BaseModel):
    title:str
    content:str
    published: Optional[bool]

@router.post('/new/{id}')
def create_blog(blog:BlogModel, id: int, version: int = 1):
    return {
        'id':id,
        'data':blog,
        'version' : version
    }

@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog:BlogModel, id:int, 
                   comment_title:str=Query(None,
                                       title='Add comment',
                                       description='In the blog of id , Add new comment',
                                    #    alias='commentId',
                                       deprecated=True),
                                    #    content: str = Body('Hi how are you!')
                    content: str = Body(..., 
                                        min_length=10,
                                        max_length=50,
                                        regex='^[a-z/s]*$'
                                        ),   #Body(Ellipsis)
                    v:List[str]=Query(['1.0', '2.0', '3.0']),
                    comment_id:int=Path(..., lt=4)
    ):
    return {
        'blog': blog,
        'id': id,
        'comment_title':comment_title,
        'content':content,
        'version':v
    }

