
from car_dealership_api.data.db import connect
from car_dealership_api.models.car import Car


class CarDataAccess:
    """Handles database operations for cars."""

    def get_all(self):
        """Retrieve all cars from the database as Car objects."""
        with connect() as conn:
            cursor = conn.execute("SELECT * FROM cars")
            rows = cursor.fetchall()

        return [Car(**dict(row)) for row in rows]

    def update_car_status(self, car_id, status):
        """Update a car's availability status in the database.

        Args:
            car_id: The ID of the car to update.
            status: The new availability status (1 or 0).

        Returns:
            True if a car was updated, otherwise False.
        """
        with connect() as conn:
            cursor = conn.execute(
                """
                UPDATE cars
                SET car_status = ?
                WHERE car_id = ?
                """,
                (status, car_id)
            )
            return cursor.rowcount > 0
