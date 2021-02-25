class User:
    username: str
    password: str
    email: str

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
