from fastapi import FastAPI
from posts import routes
from rand import routes as rand_router

app = FastAPI()
app.include_router(routes.router)
app.include_router(rand_router.router)
