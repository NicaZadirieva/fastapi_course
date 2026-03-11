from fastapi import FastAPI
from projects import routes as project_router
from tasks import routes as tasks_router

app = FastAPI(
    title="KanbanBoard API",
    description="API для работы приложения аналога JIRA",
    version="0.0.1",
    openapi_tags=[
        {"name": "Projects", "description": "Управление проектами"},
        {"name": "Tasks", "description": "Управление задачами"},
    ],
)
app.include_router(project_router.router)
app.include_router(tasks_router.router)
