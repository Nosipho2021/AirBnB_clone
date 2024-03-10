#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_args_instantiates(self):
        """Test that Place instance is properly instantiated with no arguments."""
        place = Place()
        self.assertEqual(Place, type(place))

    def test_new_instance_stored_in_objects(self):
        """Test that new instance of Place is stored in objects."""
        place = Place()
        self.assertIn(place, models.storage.all().values())


class TestPlace_save(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

    def test_save_updates_updated_at(self):
        """Test that calling save updates the updated_at attribute."""
        place = Place()
        old_updated_at = place.updated_at
        sleep(0.1)
        place.save()
        new_updated_at = place.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_save_creates_file(self):
        """Test that calling save creates a corresponding JSON file."""
        place = Place()
        place.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_save_updated_objects(self):
        """Test that calling save updates the objects dictionary."""
        place = Place()
        place.save()
        key = "{}.{}".format(place.__class__.__name__, place.id)
        self.assertIn(key, models.storage.all().keys())


class TestPlace_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""

    def test_to_dict_returns_dict(self):
        """Test that to_dict returns a dictionary."""
        place = Place()
        place_dict = place.to_dict()
        self.assertEqual(dict, type(place_dict))

    def test_to_dict_includes_class(self):
        """Test that the dictionary includes the class name."""
        place = Place()
        place_dict = place.to_dict()
        self.assertIn('__class__', place_dict)
        self.assertEqual('Place', place_dict['__class__'])

    def test_to_dict_includes_updated_at(self):
        """Test that the dictionary includes updated_at attribute."""
        place = Place()
        place_dict = place.to_dict()
        self.assertIn('updated_at', place_dict)

    def test_to_dict_includes_created_at(self):
        """Test that the dictionary includes created_at attribute."""
        place = Place()
        place_dict = place.to_dict()
        self.assertIn('created_at', place_dict)

    def test_to_dict_includes_id(self):
        """Test that the dictionary includes id attribute."""
        place = Place()
        place_dict = place.to_dict()
        self.assertIn('id', place_dict)

    def test_to_dict_includes_custom_attrs(self):
        """Test that the dictionary includes custom attributes."""
        place = Place()
        place.name = 'Test'
        place.number = 123
        place_dict = place.to_dict()
        self.assertIn('name', place_dict)
        self.assertIn('number', place_dict)


if __name__ == '__main__':
    unittest.main()
