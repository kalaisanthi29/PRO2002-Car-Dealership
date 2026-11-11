"""Unit test for the Users model"""
from car_dealership_api.models.users import User, Roles


def test_users_model():
    """Checking if a new user is created with the correct content and role"""

    # Arrange: Creating a user with test data
    user1 = User(
        user_id=1,
        name="AdminTest",
        firebase_uid="abcX1f23",
        email="AdminTest@mail.com",
        role= Roles.ADMIN
    )

    user2 = User(
        user_id=2,
        name="CustomerTest",
        firebase_uid="a19xdgb2",
        email="CustomerTest@mail.com",
        role= Roles.CUSTOMER
    )

    # Assert: Test checks that the values is as expected
    assert  user1.user_id == 1
    assert  user1.name == "AdminTest"
    assert  user1.firebase_uid == "abcX1f23"
    assert  user1.email == "AdminTest@mail.com"
    assert  user1.role == Roles.ADMIN

    assert  user2.user_id == 2
    assert  user2.name == "CustomerTest"
    assert  user2.firebase_uid == "a19xdgb2"
    assert  user2.email == "CustomerTest@mail.com"
    assert  user2.role == Roles.CUSTOMER
