from repositories.interfaces.tuition_reimbursement_form_data_repo import TuitionReimbursementFormDataRepo


class TuitionReimbursementFormDataService:

    def __init__(self, tuition_reimbursement_form_data_repo: TuitionReimbursementFormDataRepo):
        self.tuition_reimbursement_form_data_repo = tuition_reimbursement_form_data_repo()

    def create_tuition_reimbursement_form_data(self, tuition_reimbursement_form):
        return self.tuition_reimbursement_form_data_repo.create_tuition_reimbursement_form_data(tuition_reimbursement_form_data=tuition_reimbursement_form)

    def get_tuition_reimbursement_form_data(self, tuition_reimbursement_form_data_id):
        return self.tuition_reimbursement_form_data_repo.get_tuition_reimbursement_form_data(tuition_reimbursement_form_data_id=tuition_reimbursement_form_data_id)

    def get_all_tuition_reimbursement_form_data(self):
        return self.tuition_reimbursement_form_data_repo.get_all_tuition_reimbursement_form_data()

    def get_all_tuition_reimbursement_form_data_by_employee(self, employee_id):
        return self.tuition_reimbursement_form_data_repo.get_all_tuition_reimbursement_form_data_by_employee(employee_id)

    def update_tuition_reimbursement_form_data(self, change):
        return self.tuition_reimbursement_form_data_repo.update_tuition_reimbursement_form_data(change)

    def delete_event_grading_format(self, tuition_reimbursement_form_data_id):
        return self.tuition_reimbursement_form_data_repo.delete_event_grading_format(tuition_reimbursement_form_data_id)

