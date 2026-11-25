
from car_dealership_api.models.reservation import Reservation


def test_create_reservation():
    reservation = Reservation(1, 10, 5, "Pending")

    assert reservation.reservation_id == 1
    assert reservation.car_id == 10
    assert reservation.user_id == 5
    assert reservation.status == "Pending"
