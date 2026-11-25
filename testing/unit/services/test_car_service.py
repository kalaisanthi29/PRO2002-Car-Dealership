
from unittest.mock import patch

from car_dealership_api.services.car_service import CarService


def test_get_all_cars():
    fake_cars = ["Car 1", "Car 2"]

    with patch(
        "car_dealership_api.services.car_service.CarDataAccess"
    ) as mock_data_access:
        mock_data_access.return_value.get_all.return_value = fake_cars

        service = CarService()
        result = service.get_all()

        assert result == fake_cars
        mock_data_access.return_value.get_all.assert_called_once_with()
