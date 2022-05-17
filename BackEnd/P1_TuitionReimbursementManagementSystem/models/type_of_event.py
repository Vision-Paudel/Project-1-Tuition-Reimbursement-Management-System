class TypeOfEvent:

    def __init(self, event_id, event_type, reimbursement_amount):
        self.event_id = event_id
        self.event_type = event_type
        self.reimbursement_amount = reimbursement_amount

    def __repr__(self):
        return str({
            'event_id': self.event_id,
            'event_type': self.event_type,
            'reimbursement_amount': self.reimbursement_amount
        })

    def json(self):
        return {
            'eventId': self.event_id,
            'eventType': self.event_type,
            'reimbursementAmount': self.reimbursement_amount
        }
