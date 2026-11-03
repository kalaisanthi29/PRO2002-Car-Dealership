"""This defines the User module"""
class User:
    """A user or admin in the car dealership"""
    def __init__(self, user_id: int, firebase_uid: str, name:str, mail: str, role: str):
        self.user_id = user_id
        self.firebase_uid = firebase_uid
        self.name = name
        self.mail = mail
        self.role = role
