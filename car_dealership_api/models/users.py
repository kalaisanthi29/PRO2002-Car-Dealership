"""This defines the User module"""
class User:
    """A user or admin in the car dealership"""
    def __init__(self, user_id, name, mail, password_hash, role):
        self.user_id = user_id
        self.name = name
        self.mail = mail
        self.password_hash = password_hash
        self.role = role
