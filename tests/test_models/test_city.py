#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_no_args_instantiates(self):
        """Test that City instance is properly instantiated with no arguments."""
        city = City()
        self.assertEqual(City, type(city))

    def test_new_instance_stored_in_objects(self):
        """Test that new instance of City is stored in objects."""
        city = City()
        self.assertIn(city, models.storage.all().values())


class TestCity_save(unittest.TestCase):
    """Unittests for testing save method of the City class."""

    def test_save_updates_updated_at(self):
        """Test that calling save updates the updated_at attribute."""
        city = City()
        old_updated_at = city.updated_at
        sleep(0.1)
        city.save()
        new_updated_at = city.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_save_creates_file(self):
        """Test that calling save creates a corresponding JSON file."""
        city = City()
        city.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_save_updated_objects(self):
        """Test that calling save updates the objects dictionary."""
        city = City()
        city.save()
        key = "{}.{}".format(city.__class__.__name__, city.id)
        self.assertIn(key, models.storage.all().keys())


class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_returns_dict(self):
        """Test that to_dict returns a dictionary."""
        city = City()
        city_dict = city.to_dict()
        self.assertEqual(dict, type(city_dict))

    def test_to_dict_includes_class(self):
        """Test that the dictionary includes the class name."""
        city = City()
        city_dict = city.to_dict()
        self.assertIn('__class__', city_dict)
        self.assertEqual('City', city_dict['__class__'])

    def test_to_dict_includes_updated_at(self):
        """Test that the dictionary includes updated_at attribute."""
        city = City()
        city_dict = city.to_dict()
        self.assertIn('updated_at', city_dict)

    def test_to_dict_includes_created_at(self):
        """Test that the dictionary includes created_at attribute."""
        city = City()
        city_dict = city.to_dict()
        self.assertIn('created_at', city_dict)

    def test_to_dict_includes_id(self):
        """Test that the dictionary includes id attribute."""
        city = City()
        city_dict = city.to_dict()
        self.assertIn('id', city_dict)

    def test_to_dict_includes_custom_attrs(self):
        """Test that the dictionary includes custom attributes."""
        city = City()
        city.name = 'Test'
        city.number = 123
        city_dict = city.to_dict()
        self.assertIn('name', city_dict)
        self.assertIn('number', city_dict)


if __name__ == '__main__':
    unittest.main()
