"""User registration service"""
from firebase_admin import exceptions
from car_dealership_api.models.users import User
from car_dealership_api.models.registrationFactory import RegistrationFactory

class UserRegistrationService:
    """Handles the business logic of user registration"""

    def __init__(self, firebase_data, user_data):
        self.firebase_data =firebase_data
        self.user_data = user_data

    def register_user(self, payload: dict) -> User:
        """Validate the registration and return a new user with a Firebase UID."""

        RegistrationFactory.validate_registration(payload)

        name = payload["name"].strip()
        email = payload["email"].strip().lower()
        password = payload["password"].strip()

        # Creates a Firebase user
        firebase_uid = self.firebase_data.create_user_firebase(email, password)

        try:
            # Creates a new user in the database with the firebase uid
            user_id = self.user_data.create_user(firebase_uid, name, email)

            if user_id is None:
                raise RuntimeError("Failed to create user")

        except exceptions.FirebaseError:

            deleted = self.firebase_data.delete_user_firebase(firebase_uid)

            if not deleted:
                raise RuntimeError("Failed to create and delete Firebase user")

            raise

        # Create and return user obj
        return RegistrationFactory.create_user(
            user_id=user_id,
            firebase_uid= firebase_uid,
            name=name,
            email=email,)
