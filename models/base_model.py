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

    def __int__(self):
        """
        Initialize a new instance of BaseModel.

        Returns:
            A new instance of BaseModel
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            A string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class.__name__,
                                     self.id, self.__dict__)

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
        dic = self.__dic__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__

        return dic
