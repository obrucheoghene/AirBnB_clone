#!/usr/bin/python3
"""
Place class, a subclass of BaseModel class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents the Place class
    Public class attributes:
        city_id:             (str) will be City.id
        user_id:             (str) will be User.id
        name:                (str)
        description:         (str)
        number_rooms:        (int) number of rooms
        number_bathrooms:    (int) number of bathrooms
        max_guest:           (int) max number of guet
        price_by_night:      (int) price by night
        latitude:            (float) latitude
        longitude:           (float) longitude
        amenity_ids:         (list) will be Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
