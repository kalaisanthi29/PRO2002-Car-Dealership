
from car_dealership_api.data.db import connect
from car_dealership_api.models.car import Car


class CarDataAccess:
    def get_all(self):
        with connect() as conn:
            cursor = conn.execute("SELECT * FROM cars")
            rows = cursor.fetchall()

        return [Car(**dict(row)) for row in rows]


    def update_car_status(self, car_id, status):
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
