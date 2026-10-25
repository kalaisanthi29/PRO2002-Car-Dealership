from .db import connect
class UserDataAccess:
    """Handles reading and writing user data in the database"""

    def __init__(self, db_path: str |None = None):
        """"""
        self. _db_path = db_path

    def create_user(self, name:str, mail:str, password_hash:str,role:str) -> int |None:
        """Inserting a new user to the User table in dealership db"""
        with connect(self._db_path) as conn:
            cursor = conn.execute(
                "INSERT INTO users (name, mail, password_hash, role) VALUES (?, ?, ?, ?)",
                (name, mail, password_hash, role)
            )
        return cursor.lastrowid
