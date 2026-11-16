
from .db import connect


class ReservationDataAccess:
    def __init__(self, db_path=None):
        self.db_path = db_path

    def create_reservation(self, user_id, car_id, reservation_date):
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
