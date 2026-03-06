# GET query rnd_from и rnd_to, возвращаемый int
# в этом диапазоне
from fastapi import APIRouter, HTTPException

from random import randint

router = APIRouter(prefix="/rand")


@router.get("/")
def root(rnd_from: int = 0, rnd_to: int = 100):
    if rnd_from > rnd_to:
        raise HTTPException(400, "rnd_from не должно быть больше rnd_to")
    return randint(rnd_from, rnd_to)
