from car_dealership_api.data.db import connect
from car_dealership_api.models.users import User

class UserDataAccess:
    """Handles reading and writing user data in the database"""

    def __init__(self, db_path: str |None = None):
        self. _db_path = db_path
        