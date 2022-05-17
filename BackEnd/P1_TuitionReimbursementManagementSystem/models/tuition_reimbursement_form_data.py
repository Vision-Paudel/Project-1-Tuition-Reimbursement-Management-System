class TuitionReimbursementFormData:

    def __init__(self, tuition_reimbursement_form_data_id: int, attending_employee: int, event_date_time,
                 event_location, event_description, event_cost, event_grading_format, type_of_event,
                 event_related_attachment=None, approvals_already_provided=None):
        self.tuition_reimbursement_form_data_id = tuition_reimbursement_form_data_id
        self.attending_employee = attending_employee
        self.event_date_time = event_date_time
        self.event_location = event_location
        self.event_description = event_description
        self.event_cost = event_cost
        self.event_grading_format = event_grading_format
        self.type_of_event = type_of_event
        self.event_related_attachment = event_related_attachment
        self.approvals_already_provided = approvals_already_provided

    def __repr__(self):
        return str({
            'tuition_reimbursement_form_data_id': self.tuition_reimbursement_form_data_id,
            'attending_employee': self.attending_employee,
            'event_date_time': self.event_date_time,
            'event_location': self.event_location,
            'event_description': self.event_description,
            'event_cost': self.event_cost,
            'event_grading_format': self.event_grading_format,
            'type_of_event': self.type_of_event,
            'event_related_attachment': self.event_related_attachment,
            'approvals_already_provided': self.approvals_already_provided
        })

    def json(self):
        return {
            'tuitionReimbursementFormDataId': self.tuition_reimbursement_form_data_id,
            'attendingEmployee': self.attending_employee,
            'eventDateTime': self.event_date_time,
            'eventLocation': self.event_location,
            'eventDescription': self.event_description,
            'eventCost': self.event_cost,
            'eventGradingFormat': self.event_grading_format,
            'typeOfEvent': self.type_of_event,
            'eventRelatedAttachment': self.event_related_attachment,
            'approvalsAlreadyProvided': self.approvals_already_provided
        }
