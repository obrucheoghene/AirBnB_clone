#!/usr/bin/python3
"""
This module defines all common attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    The model that defines all common attributes and methods
    of other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of BaseModel.

        Args:
            args(tuple): Variable arguments
            kwargs(dict): Variable keyword arguments

        Returns:
            A new instance of BaseModel
        """
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        date_format)
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        date_format)
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            A string representation of the BaseModel instance.
        """
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        __dict__ of the instance.

        Returns:
            Returns __dict__ keys/values of the instance
        """
        c_dict = self.__dict__.copy()
        c_dict["created_at"] = self.created_at.isoformat()
        c_dict["updated_at"] = self.updated_at.isoformat()
        c_dict["__class__"] = self.__class__.__name__

        return c_dict
