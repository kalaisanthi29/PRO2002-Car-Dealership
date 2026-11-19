
from .db import connect


class ReservationDataAccess:
    """Handles database operations for reservations."""

    def __init__(self, db_path=None):
        """Initialize the database connection path."""
        self.db_path = db_path

    def create_reservation(self, user_id, car_id, reservation_date):
        """Create a new reservation and return its ID."""
        with connect(self.db_path) as conn:
            cursor = conn.execute(
                """
                INSERT INTO reservations
                (user_id, car_id, reservation_date)
                VALUES (?, ?, ?)
                """,
                (user_id, car_id, reservation_date)
            )
            return cursor.lastrowid

    def get_reservation_by_id(self, reservation_id):
        """Retrieve a reservation by ID, or None if not found."""
        with connect(self.db_path) as conn:
            cursor = conn.execute(
                """
                SELECT * FROM reservations
                WHERE reservation_id = ?
                """,
                (reservation_id,)
            )
            row = cursor.fetchone()
            return dict(row) if row else None

    def update_reservation_status(self, reservation_id, status):
        """Update a reservation's status and return whether it was found."""
        with connect(self.db_path) as conn:
            cursor = conn.execute(
                """
                UPDATE reservations
                SET reservation_status = ?
                WHERE reservation_id = ?
                """,
                (status, reservation_id)
            )
            return cursor.rowcount > 0
