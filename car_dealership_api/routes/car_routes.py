
from flask import Blueprint, jsonify
from car_dealership_api.services.car_service import CarService

car_bp = Blueprint("cars", __name__)


@car_bp.route("/cars", methods=["GET"])
def get_cars():
    cars = CarService().get_all()
    return jsonify([car.__dict__ for car in cars])
