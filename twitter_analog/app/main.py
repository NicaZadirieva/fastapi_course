from fastapi import FastAPI
from app.posts.routes import router as posts_router
from app.core.settings import Settings


def create_app() -> FastAPI:
    settings = Settings()  # type: ignore[call-arg]
    new_app = FastAPI(
        title="Posts API",
        description="API для работы приложения аналога Twitter",
        version="0.0.1",
        openapi_tags=[{"name": "Posts", "description": "Управление постами"}],
    )
    new_app.state.settings = settings

    new_app.include_router(posts_router)

    return new_app


app = create_app()
