#!/usr/bin/python3
"""
Defines unittests for BaseModel

Unitest classes:
    TestBaseModel_initialization
    TestBaseModel_save
    TestBaseModel_to_dict
    TestBaseModel_str_representation
"""
import models_path
from models.base_model import BaseModel
import unittest
from datetime import datetime
from time import sleep


class TestBaseModel_initialization(unittest.TestCase):
    """Unit tests to BaseModel Initialization"""

    def test_default_init(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_two_model_unique_id(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)
    
    def test_id_is_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_updated_at_and_created_at_are_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_two_models_create_at_are_different(self):
        bm1 = BaseModel()
        sleep(0.01)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)


class TestBaseModel_save(unittest.TestCase):
    """Unit tests for BaseModel save"""

    def test_model_upated_at_changed(self):
        base_model = BaseModel();
        init_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(init_updated_at, base_model.updated_at)


class TestBaseModel_to_dict(unittest.TestCase):
    """Unit tests for BaseModel to dict"""
    
    def test_model_to_dict_has__class__key(self):
        bm_dict = BaseModel().to_dict()
        self.assertIn("__class__", bm_dict)
    
    def test_model_to_dict__class__equal_class_name(self):
        bm_dict = BaseModel().to_dict()
        self.assertEqual(bm_dict["__class__"], "BaseModel")


class TestBaseModel_str_representation(unittest.TestCase):
    """Unit test to test string representation of BaseModel"""

    def test_class_name_str_representation(self):
        self.assertIn("[BaseModel]", BaseModel().__str__())

if __name__ == "__main__":
    unittest.main()
