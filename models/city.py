#!/usr/bin/python3
"""
Describes the City lass, a subclass of BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents the City class
    """
    state_id = ""
    name = ""
