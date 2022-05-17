class RegisterUserDetailsFromFrontEnd:

    def __init__(self, username, password, email, employee_id):
        self.username = username
        self.password = password
        self.email = email
        self.employee_id = employee_id

    def __repr__(self):
        return str({
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'employee_id': self.employee_id
        })

    def json(self):
        return {
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'employeeId': self.employeeId
        }