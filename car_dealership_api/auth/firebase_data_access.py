"""Firebase user data handling for the car dealership"""
from firebase_admin import auth, exceptions
from car_dealership_api.auth.firebase_token_auth import initialize_firebase

class FirebaseDataAccess:
    """Handles the operations for creating and deleting a user in firebase"""

    def __init__(self):
        """initializes firebase"""
        initialize_firebase()

    def create_user_firebase(self, email:str, password:str) -> str | None:
        """Function to create a new user with email and password in firebase"""
        try:
            user = auth.create_user(
                email=email,
                password=password
            )

            return user.uid

        except exceptions.FirebaseError:
            return None


    def delete_user_firebase(self, uid:str) -> bool:
        """Function to delete a existing user in firebase"""
        try:
            auth.delete_user(uid)
            return True
        except exceptions.FirebaseError:
            return False
