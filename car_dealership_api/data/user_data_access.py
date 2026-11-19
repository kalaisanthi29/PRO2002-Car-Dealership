"""Handles data access for users in the database"""
from car_dealership_api.data.db import connect
class UserDataAccess:
    """Handles database operations for user data"""

    def __init__(self, db_path: str |None = None):
        """initialize data access"""
        self. _db_path = db_path

    # NOTE! We might remove this if the email check from db is not necessary. Discuss in the next meeting
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


    def create_user(self, firebase_uid:str, name:str, email:str) -> int | None:
        """Inserting a new user to the User table in dealership db"""

        conn = connect(self._db_path)

        try:
            with conn:
                cursor = conn.execute(
                    "INSERT INTO users (firebase_uid, name, email) VALUES (?, ?, ?)",
                    (firebase_uid, name, email)
                )
            return cursor.lastrowid
        finally:
            conn.close()
            