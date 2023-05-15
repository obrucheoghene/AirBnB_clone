#!/usr/bin/python3
"""
Defines the FileStorage to save instances to file
"""
import json
import os
from models.base_model import BaseModel


class FileStorage():
    """
    Saves instances of BaseModel to file

    Class Attributes:
        __file_path: string - path to the JSON file
        __objects: dictionary - empty but will store all objects

    Instance Methods:
        all: returns the dictionary
        new: sets in __objects the obj
        save: serializes __objects to the JSON file
        reload: deserializes the JSON file to __objects
    """

    __file_path = "airbnb_db.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        objects_dict = {}
        for key, obj in self.__objects.items():
            objects_dict[key] = obj.to_dict()
        with open(self.__file_path, "w", encoding="UTF-8") as file:
            json.dump(objects_dict, file)

    def reload(self):
        """
        deserializes the JSON file
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="UTF-8") as file:
                objects_dict = json.load(file)
                for obj_dict in objects_dict.values():
                    self.new(eval(obj_dict["__class__"])(**obj_dict))
