
class Reservation:
    """Represents a reservation made by a user for a car."""

    def __init__(self, reservation_id, car_id, user_id, status):
        """Initialize a reservation with its ID, car, user and status."""
        self.reservation_id = reservation_id
        self.car_id = car_id
        self.user_id = user_id
        self.status = status
