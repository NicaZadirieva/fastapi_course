import logging
import sys
from fastapi import FastAPI
from app.core.settings import Settings
from app.projects.routes import router as project_router
from app.tasks.routes import router as tasks_router


def create_app() -> FastAPI:
    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stdout,
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    )
    for name in ("uvicorn", "uvicorn.error", "uvicorn.access"):
        lg = logging.getLogger(name)
        lg.handlers.clear()
        lg.propagate = True

    settings = Settings()  # type: ignore[call-arg]
    new_app = FastAPI(
        title=settings.app.name,
        description="API для работы приложения аналога JIRA",
        version="0.0.1",
        openapi_tags=[
            {"name": "Projects", "description": "Управление проектами"},
            {"name": "Tasks", "description": "Управление задачами"},
        ],
    )
    new_app.state.settings = settings

    new_app.include_router(project_router)
    new_app.include_router(tasks_router)

    return new_app


app = create_app()
