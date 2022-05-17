class EmployeeUserDetailsFromFrontend:

    def __init__(self, username, password, email, security_token, last_successful_log_in, employee_id):
        self.username = username
        self.password = password
        self.email = email
        self.security_token = security_token
        self.last_successful_log_in = last_successful_log_in
        self.employee_id = employee_id

    def __repr__(self):
        return str({
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'security_token': self.security_token,
            'last_successful_log_in': self.last_successful_log_in,
            'employee_id': self.employee_id
        })

    def json(self):
        return {
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'securityToken': self.security_token,
            'lastSuccessfulLogIn': self.last_successful_log_in,
            'employeeId': self.employee_id
        }


