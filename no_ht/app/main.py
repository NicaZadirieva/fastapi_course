import random
from fastapi import FastAPI, HTTPException, Response

app = FastAPI()


@app.get("/")
def root(response: Response):
    num = random.random()
    if num > 0.5:
        raise HTTPException(401, "Не авторизован")
    # return {"Score": 10}
    else:
        response.status_code = 201
    return {"Score": num}
