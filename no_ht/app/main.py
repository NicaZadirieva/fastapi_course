from fastapi import FastAPI
from app.projects.routes import router as project_router
from app.tasks.routes import router as tasks_router

app = FastAPI(
    title="KanbanBoard API",
    description="API для работы приложения аналога JIRA",
    version="0.0.1",
    openapi_tags=[
        {"name": "Projects", "description": "Управление проектами"},
        {"name": "Tasks", "description": "Управление задачами"},
    ],
)
app.include_router(project_router)
app.include_router(tasks_router)
