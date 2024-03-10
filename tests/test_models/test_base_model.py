#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        """Test that BaseModel instance is properly instantiated with no arguments."""
        base_model = BaseModel()
        self.assertEqual(BaseModel, type(base_model))

    def test_new_instance_stored_in_objects(self):
        """Test that new instance of BaseModel is stored in objects."""
        base_model = BaseModel()
        self.assertIn(base_model, models.storage.all().values())


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    def test_save_updates_updated_at(self):
        """Test that calling save updates the updated_at attribute."""
        base_model = BaseModel()
        old_updated_at = base_model.updated_at
        sleep(0.1)
        base_model.save()
        new_updated_at = base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_save_creates_file(self):
        """Test that calling save creates a corresponding JSON file."""
        base_model = BaseModel()
        base_model.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_save_updated_objects(self):
        """Test that calling save updates the objects dictionary."""
        base_model = BaseModel()
        base_model.save()
        key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
        self.assertIn(key, models.storage.all().keys())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_returns_dict(self):
        """Test that to_dict returns a dictionary."""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertEqual(dict, type(base_model_dict))

    def test_to_dict_includes_class(self):
        """Test that the dictionary includes the class name."""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIn('__class__', base_model_dict)
        self.assertEqual('BaseModel', base_model_dict['__class__'])

    def test_to_dict_includes_updated_at(self):
        """Test that the dictionary includes updated_at attribute."""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIn('updated_at', base_model_dict)

    def test_to_dict_includes_created_at(self):
        """Test that the dictionary includes created_at attribute."""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIn('created_at', base_model_dict)

    def test_to_dict_includes_id(self):
        """Test that the dictionary includes id attribute."""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIn('id', base_model_dict)

    def test_to_dict_includes_custom_attrs(self):
        """Test that the dictionary includes custom attributes."""
        base_model = BaseModel()
        base_model.name = 'Test'
        base_model.number = 123
        base_model_dict = base_model.to_dict()
        self.assertIn('name', base_model_dict)
        self.assertIn('number', base_model_dict)


if __name__ == '__main__':
    unittest.main()
