#!/usr/bin/python3
"""
This module defines a User class that inherits from the BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents the user class
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
