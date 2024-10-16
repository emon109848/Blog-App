from typing import Optional
from fastapi import APIRouter,status, Response
from enum import Enum

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


class BlogType(str,Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@router.get(
        '/all',
        summary='Retrive all Blogs',
        description="this api accl simulates fatching all the blogs",
        response_description="the list of available blogs"
)
async def get_all_blogs(page=1, page_size:Optional[int]=None):
    return {"message": f'All {page_size} blogs on page {page}'}


@router.get('/{id}/commants/{comment_id}',tags=['comment'])
async def get_comment(id,comment_id,valid:bool = True, username: Optional[str]=None):
    """
    Simulates retraving a comment of a blog

    - **id** mandatory path parameter
    - **comments_id** mandatory path parameter
    - **valid** optional query parameter
    - **username** optional queary parameter
    """
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}


@router.get("/type/{type}")
async def get_blog_type(type:BlogType):
    return {'message': f"this blog is {type} type"}


@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'Error': f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id {id}'}

