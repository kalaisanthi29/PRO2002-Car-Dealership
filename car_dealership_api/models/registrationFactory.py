"""Central place to validate the user registration"""
import re
from car_dealership_api.models.users import User
from car_dealership_api.types.roles import Roles

class RegistrationFactory:
    """Registration factory"""

    @staticmethod
    def validate_registration(payload: dict) -> None:
        """
        Purpose: Validate the required fields in registration
        Checks name, email, and password.
        """
        required = ("name", "email", "password")

        missing = [key for key in required if key not in payload]

        if missing:
            raise ValueError(f"missing name,email or password: {', '.join(missing)}"
            )

        for key in required:
            value = payload[key]

            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"Invalid or empty: {key}")

        email_format = payload["email"].strip()

        # Regex for checking the email format.
        if not re.fullmatch(r"[^@\s]+@[^@.\s]+\.[^@.\s]+", email_format):
            raise ValueError("Invalid email submitted")

    @staticmethod
    def create_user(user_id: int, firebase_uid: str, name:str, email: str) -> User:
        """
        Note! Remember to fill out docstring
        """
        return User(
            user_id = user_id,
            firebase_uid = firebase_uid,
            name = name,
            email = email,
            role = Roles.CUSTOMER
        )
