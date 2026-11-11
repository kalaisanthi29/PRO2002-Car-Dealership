"""This defines the User module"""
from car_dealership_api.types.roles import Roles
class User:
    """A user or admin in the car dealership"""
    def __init__(self, user_id: int, firebase_uid: str, name:str, email: str, role: Roles):
        self.user_id = user_id
        self.firebase_uid = firebase_uid
        self.name = name
        self.email = email
        self.role = role
