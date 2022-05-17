from repositories.interfaces.employee_user_details_repo import EmployeeUserDetailsRepo


class EmployeeUserDetailsService:

    def __init__(self, employee_user_details_repo: EmployeeUserDetailsRepo):
        self.employee_user_details_repo = employee_user_details_repo

    def create_employee_user_details(self, register_details):
        return self.employee_user_details_repo.create_employee_user_details(register_details)

    def get_employee_user_details_by_username(self, username):
        return self.employee_user_details_repo.get_employee_user_details_by_username(username)

    def get_employee_user_details_by_employee_id(self, employee_id):
        return self.employee_user_details_repo.get_employee_user_details_by_employee_id(employee_id)

    def get_all_employee_user_details(self):
        return self.employee_user_details_repo.get_all_employee_user_details()

    def update_employee_user_details(self, employee_user_details_from_frontend):
        return self.employee_user_details_repo.update_employee_user_details(employee_user_details_from_frontend)

    def delete_employee_user_details(self, username):
        return self.employee_user_details_repo.delete_employee_user_details(username)
