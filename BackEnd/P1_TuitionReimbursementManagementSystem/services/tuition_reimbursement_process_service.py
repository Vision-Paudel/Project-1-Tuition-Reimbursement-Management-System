from repositories.interfaces.tuition_reimbursement_process_repo import TuitionReimbursementProcessRepo


class TuitionReimbursementProcessService:

    def __init__(self, tuition_reimbursement_process_repo: TuitionReimbursementProcessRepo):
        self.tuition_reimbursement_process_repo = tuition_reimbursement_process_repo

    def create_tuition_reimbursement_process(self, tuition_reimbursement_process):
        return self.tuition_reimbursement_process_repo.create_tuition_reimbursement_process(tuition_reimbursement_process)

    def get_tuition_reimbursement_process(self, tr_form_data_id):
        return self.tuition_reimbursement_process_repo.get_tuition_reimbursement_process(tr_form_data_id)

    def get_all_tuition_reimbursement_process(self):
        return self.tuition_reimbursement_process_repo.get_all_tuition_reimbursement_process()

    def update_tuition_reimbursement_process(self, change):
        return self.tuition_reimbursement_process_repo.update_tuition_reimbursement_process(change)

    def delete_reimbursement_process(self, tr_form_data_id):
        return self.tuition_reimbursement_process_repo.delete_reimbursement_process(tr_form_data_id)

