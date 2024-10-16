from fastapi import APIRouter, Response

router = APIRouter(
    prefix='/product',
    tags=['product']
)

product = ['watch', 'camera', 'phone']

@router.get('/all')
def get_all_product():
    # return product
    data = " ".join(product)
    return Response(content=data, media_type="text/plain")