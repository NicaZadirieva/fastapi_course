from fastapi import FastAPI
from app.posts.routes import router as posts_router


def create_app() -> FastAPI:
    new_app = FastAPI(
        title="Posts API",
        description="API для работы приложения аналога Twitter",
        version="0.0.1",
        openapi_tags=[{"name": "Posts", "description": "Управление постами"}],
    )

    new_app.include_router(posts_router)

    return new_app


app = create_app()
