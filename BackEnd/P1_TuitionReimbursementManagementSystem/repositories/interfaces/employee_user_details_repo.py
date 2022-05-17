from abc import ABC, abstractmethod


class EmployeeUserDetailsRepo(ABC):

    @abstractmethod
    def create_employee_user_details(self, register_details):
        pass

    @abstractmethod
    def get_employee_user_details_by_username(self, username):
        pass

    @abstractmethod
    def get_employee_user_details_by_employee_id(self, employee_id):
        pass

    @abstractmethod
    def get_all_employee_user_details(self):
        pass

    @abstractmethod
    def update_employee_user_details(self, employee_user_details_from_frontend):
        pass

    @abstractmethod
    def set_new_last_successful_log_in_for_employee_details(self, username):
        pass

    @abstractmethod
    def delete_employee_user_details(self, username):
        pass
