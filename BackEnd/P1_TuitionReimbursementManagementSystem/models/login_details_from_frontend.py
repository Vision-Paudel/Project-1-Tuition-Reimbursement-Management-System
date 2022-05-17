class LoginDetailsFromFrontEnd:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return str({
            'username': self.username,
            'password': self.password
        })

    def json(self):
        return {
            'username': self.username,
            'password': self.password
        }