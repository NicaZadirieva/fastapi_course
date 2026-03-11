def get_project_service():
    return ProjectService()


class ProjectRepository:
    def get_by_id(self, id: int):
        pass


class ProjectService:
    def get_project(self, project_id: int):
        return project_id
