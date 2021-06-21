from fastapi import (
    APIRouter,
    Depends,
)
from starlette import status

from ..models import common
from ..service.Operation import get_operations_add

router = APIRouter(
    prefix='/operation',
    tags=['operation'],
)


@router.post('/calc',
             response_model=common.ResultOperation,
             status_code=status.HTTP_200_OK,
             name="operation:calc",
             )
def add(
        result: common.ResultOperation= Depends(get_operations_add)
        ):
    return result
