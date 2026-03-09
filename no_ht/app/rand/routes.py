# GET query rnd_from и rnd_to, возвращаемый int
# в этом диапазоне
from fastapi import APIRouter, Depends, HTTPException

from random import randint

from .schema import RandQuery

router = APIRouter(prefix="/rand")


@router.get("/")
def root(query: RandQuery = Depends()):
    return {"value": randint(query.rnd_from, query.rnd_to)}
