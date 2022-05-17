from abc import ABC, abstractmethod


class TuitionReimbursementProcessRepo(ABC):

    @abstractmethod
    def create_tuition_reimbursement_process(self, tuition_reimbursement_process):
        pass

    @abstractmethod
    def get_tuition_reimbursement_process(self, tr_form_data_id):
        pass

    @abstractmethod
    def get_all_tuition_reimbursement_process(self):
        pass

    @abstractmethod
    def update_tuition_reimbursement_process(self, change):
        pass

    @abstractmethod
    def delete_reimbursement_process(self, tr_form_data_id):
        pass
