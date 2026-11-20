"""Integration test for user registration endpoint"""
from app import app
from car_dealership_api.routes.user_routs import service
from testing.integration.db_test_helper import db_test as db_test_fixture

def test_new_user_with_registration_endpoint(db_test_fixture, monkeypatch):
    """Test the registration endpoint"""

    monkeypatch.setattr(service.user_data, "_db_path", str(db_test_fixture.path))

    # Simulates a firebase user creation
    def firebase_user(email, password):
        assert email == "TestApiReg@gmail.com".lower()
        assert password =="TestApiReg123"
        return "firebaseuid123"


    monkeypatch.setattr(service.firebase_data, "create_user_firebase", firebase_user)

    # Creates a test client
    client = app.test_client()

    response = client.post("/registration",
        json=
        {
            "name": "TestApiReg",
            "email": "TestApiReg@gmail.com",
            "password": "TestApiReg123"
        }
    )

    # Get the response data
    data = response.get_json()

    # Expected result of HTTP status code
    assert response.status_code == 201

    # Expected return results
    assert data["firebase_uid"] == "firebaseuid123"
    assert data["name"] == "TestApiReg"
    assert data["email"] == "TestApiReg@gmail.com".lower()
    assert data["role"] == "customer"
