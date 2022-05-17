from repositories.interfaces.department_repo import DepartmentRepo


class DepartmentServiceImpl:

    def __init__(self, department_repo: DepartmentRepo):
        self.department_repo = department_repo

    def create_department(self, department):
        return self.department_repo.create_department(department)

    def get_department(self, department_id):
        return self.department_repo.get_department(department_id)

    def get_all_departments(self):
        return self.department_repo.get_all_departments()

    def update_department(self, change):
        return self.department_repo.update_department(change)

    def delete_department(self, department_id):
        return self.department_repo.delete_department(department_id)
