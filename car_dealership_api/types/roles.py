"""Module that define the user roles in the car dealership system"""
from enum import Enum

class Roles(str, Enum):
    """The type of roles in the car dealership system"""

    ADMIN = "admin"
    CUSTOMER = "customer"
