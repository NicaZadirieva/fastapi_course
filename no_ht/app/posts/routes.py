from enum import Enum
from fastapi import APIRouter, Path, Query, Request, Response

router = APIRouter(prefix="/posts")


@router.get("/{post_id}")
def get_post(post_id: int = Path(ge=5)):
    return {"id": post_id}


class SortOrder(str, Enum):
    asc = "asc"
    desc = "desc"


@router.get("/")
def get_posts(
    limit: int = 10,
    offset: int = Query(default=0, ge=0, alias="Offset"),
    tags: list[str] = Query([]),
    order: SortOrder = SortOrder.asc,
):
    return {"limit": limit, "offset": offset, "tags": tags, "order": order}


@router.post("/")
async def create_post(
    request: Request,
    # body: dict = Body()
):
    data = await request.json()
    return data
