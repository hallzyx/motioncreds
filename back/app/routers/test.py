
from fastapi import APIRouter

router=APIRouter(prefix="/test")


@router.get("/")
async def read_root():
    return {"msj":"Wasaaaaaaa desde fastApi"}