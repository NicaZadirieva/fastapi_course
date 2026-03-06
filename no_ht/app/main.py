from fastapi import FastAPI
from posts import routes

app = FastAPI()
app.include_router(routes.router)
