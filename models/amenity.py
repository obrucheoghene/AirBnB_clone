#!/usr/bin/python3
"""
Describes amenity class that inherits from Base model
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represensts amentity
    Public class attribute:
        name: (str)
    """
    name = ""
