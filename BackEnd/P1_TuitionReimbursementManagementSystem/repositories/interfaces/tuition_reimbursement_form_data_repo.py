from abc import ABC, abstractmethod


class TuitionReimbursementFormDataRepo(ABC):

    @abstractmethod
    def create_tuition_reimbursement_form_data(self, tuition_reimbursement_form_data):
        pass

    @abstractmethod
    def get_tuition_reimbursement_form_data(self, tuition_reimbursement_form_data_id):
        pass

    @abstractmethod
    def get_all_tuition_reimbursement_form_data(self):
        pass

    @abstractmethod
    def get_all_tuition_reimbursement_form_data_by_employee(self, employee_id):
        pass

    @abstractmethod
    def update_tuition_reimbursement_form_data(self, change):
        pass

    @abstractmethod
    def delete_event_grading_format(self, tuition_reimbursement_form_data_id):
        pass
