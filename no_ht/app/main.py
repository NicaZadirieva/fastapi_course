from fastapi import FastAPI
from projects import routes as project_router

app = FastAPI()
app.include_router(project_router.router)
