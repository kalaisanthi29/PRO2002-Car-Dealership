"""User registration route for the car dealership"""
from flask import Blueprint, request, jsonify
from firebase_admin import auth
from car_dealership_api.services.user_registration_service import UserRegistrationService
from car_dealership_api.auth.firebase_data_access import FirebaseDataAccess
from car_dealership_api.data.user_data_access import UserDataAccess

# Makes a user registration blueprint
user_registration_bp = Blueprint("registration",__name__, url_prefix="/registration")

# Uses the data access from data and auth
service = UserRegistrationService(FirebaseDataAccess(), UserDataAccess())

@user_registration_bp.post("")
def registration():
    """Registration endpoints for creating a new user"""

    payload = request.get_json(silent=True) or {}

    try:
        user = service.register_user(payload)

        # Uses HTTP status code 201 instead of 200. "201" is correct for created resources
        return jsonify(user.to_dict()), 201

    except ValueError as error:
        return jsonify({"Error": str(error)}), 400

    # EmailAlreadyExistsError from firebase package
    except auth.EmailAlreadyExistsError:

        # Using HTTP 409 for conflict error
        return jsonify({"Error": "Email exists in the system"}), 409
    