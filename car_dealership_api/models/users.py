"""This defines the User module"""
from car_dealership_api.types.roles import Roles
class User:
    """This is a customer or admin in the car dealership"""
    def __init__(self, user_id: int, firebase_uid: str, name:str, email: str, role: Roles):
        self.user_id = user_id
        self.firebase_uid = firebase_uid
        self.name = name
        self.email = email
        self.role = role

    def to_dict(self) -> dict:
        """
        Converts User entity into a dictionary for JSON serialization.
        """
        return {
            "user_id": self.user_id,
            "firebase_uid": self.firebase_uid,
            "name": self.name,
            "email": self.email,
            "role": self.role,
        }
