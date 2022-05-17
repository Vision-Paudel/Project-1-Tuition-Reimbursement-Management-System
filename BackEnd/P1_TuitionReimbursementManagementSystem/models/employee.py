class Employee:

    def __init__(self, employee_id: int, first_name: str, last_name: str, job_title: str, supervisor: int,
                 department: int):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.supervisor = supervisor
        self.department = department

    def __repr__(self):
        return str({
            'employee_id': self.employee_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'job_title': self.job_title,
            'supervisor': self.supervisor,
            'department': self.department
        })

    def json(self):
        return {
            'employeeId': self.employee_id,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'jobTitle': self.job_title,
            'supervisor': self.supervisor,
            'department': self.department
        }

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
