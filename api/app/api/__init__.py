from fastapi import APIRouter
from . import  operation

router = APIRouter()
router.include_router(operation.router)