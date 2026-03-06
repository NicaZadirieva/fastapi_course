import random
from fastapi import FastAPI, HTTPException, Path, Query, Response

app = FastAPI()


class UnauthHTTPException(HTTPException):
    def __init__(self) -> None:
        super().__init__(401, "Не авторизован")


@app.get("/")
def root(response: Response):
    num = random.random()
    if num > 0.5:
        raise UnauthHTTPException()
    # return {"Score": 10}
    else:
        response.status_code = 201
    return {"Score": num}


@app.get("/posts/{post_id}")
def get_post(post_id: int = Path(ge=5)):
    return {"id": post_id}


@app.get("/posts")
def get_posts(
    limit: int = 10,
    offset: int = Query(default=0, ge=0, alias="Offset"),
    tags: list[str] = Query([]),
):
    return {"limit": limit, "offset": offset, "tags": tags}
