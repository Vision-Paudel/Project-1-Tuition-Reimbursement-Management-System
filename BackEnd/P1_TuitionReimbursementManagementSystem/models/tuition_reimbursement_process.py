class TuitionReimbursementProcess:

    def __init__(self, tr_form_data_id, approved_by_supervisor="Pending", approved_by_department_head="Pending",
                 approved_by_benefits_coordinator="Pending", presented="Pending", grade_received="", confirmed="Pending", reimbursed="Pending"):
        self.tr_form_data_id = tr_form_data_id
        self.approved_by_supervisor = approved_by_supervisor
        self.approved_by_department_head = approved_by_department_head
        self.approved_by_benefits_coordinator = approved_by_benefits_coordinator
        self.presented = presented
        self.grade_received = grade_received
        self.confirmed = confirmed
        self.reimbursed = reimbursed

    def __repr__(self):
        return str({
            'tr_form_data_id': self.tr_form_data_id,
            'approved_by_supervisor': self.approved_by_supervisor,
            'approved_by_department_head': self.approved_by_department_head,
            'approved_by_benefits_coordinator': self.approved_by_benefits_coordinator,
            'presented': self.presented,
            'grade_received': self.grade_received,
            'confirmed': self.confirmed,
            'reimbursed': self.reimbursed
        })

    def json(self):
        return {
            'trFormDataId': self.tr_form_data_id,
            'approvedBySupervisor': self.approved_by_supervisor,
            'approvedByDepartmentHead': self.approved_by_department_head,
            'approvedByBenefitsCoordinator': self.approved_by_benefits_coordinator,
            'presented': self.presented,
            'gradeReceived': self.grade_received,
            'confirmed': self.confirmed,
            'reimbursed': self.reimbursed
        }
