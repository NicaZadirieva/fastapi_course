class ProjectRepository:
    def get_by_id(self, id: int):
        pass


class ProjectService:
    def get_project(self, id: int, repo: ProjectRepository):
        repo.get_by_id(id)
