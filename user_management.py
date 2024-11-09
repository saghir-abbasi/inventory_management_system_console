from data_storage import users

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class UserManager:
    def login(self, username, password):
        user_data = users.get(username)
        if user_data and user_data["password"] == password:
            return User(user_data["username"], user_data["password"], user_data["role"])
        return None
