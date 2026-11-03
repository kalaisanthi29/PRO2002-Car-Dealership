"""Module handling UserDataAccess"""
from car_dealership_api.data.db import connect
class UserDataAccess:
    """Handles reading and writing user data in the database"""

    def __init__(self, db_path: str |None = None):
        """"""
        self. _db_path = db_path


    def get_user_by_email (self, email:str) -> str | None:
        """Get user email from DB, returns None if not in DB"""
        with connect(self._db_path) as conn:
            cursor = conn.execute(
                "SELECT email FROM users WHERE email = ?",
                (email,)
            )
            #Using fetchone to return one row
            row = cursor.fetchone()
        return row ["email"] if row else None


    def create_user(self, name:str, firebase_uid:str, email:str, role:str) -> int | None:
        """Inserting a new user to the User table in dealership db"""
        with connect(self._db_path) as conn:
            cursor = conn.execute(
                "INSERT INTO users (name, firebase_uid, email, role) VALUES (?, ?, ?, ?)",
                (name, firebase_uid, email, role)
            )
        return cursor.lastrowid
