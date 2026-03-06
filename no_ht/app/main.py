import random
from fastapi import FastAPI, HTTPException, Path, Response

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
