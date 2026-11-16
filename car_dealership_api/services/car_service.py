
from car_dealership_api.data.car_data_access import CarDataAccess


class CarService:
    def get_all(self):
        return CarDataAccess().get_all()
