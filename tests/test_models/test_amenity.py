#!/usr/bin/python3
"""Defines unittests for models/amenity.py.

Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_no_args_instantiates(self):
        """Test that Amenity instance is properly instantiated with no arguments."""
        amenity = Amenity()
        self.assertEqual(Amenity, type(amenity))

    def test_new_instance_stored_in_objects(self):
        """Test that new instance of Amenity is stored in objects."""
        amenity = Amenity()
        self.assertIn(amenity, models.storage.all().values())


class TestAmenity_save(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

    def test_save_updates_updated_at(self):
        """Test that calling save updates the updated_at attribute."""
        amenity = Amenity()
        old_updated_at = amenity.updated_at
        sleep(0.1)
        amenity.save()
        new_updated_at = amenity.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_save_creates_file(self):
        """Test that calling save creates a corresponding JSON file."""
        amenity = Amenity()
        amenity.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_save_updated_objects(self):
        """Test that calling save updates the objects dictionary."""
        amenity = Amenity()
        amenity.save()
        key = "{}.{}".format(amenity.__class__.__name__, amenity.id)
        self.assertIn(key, models.storage.all().keys())


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_returns_dict(self):
        """Test that to_dict returns a dictionary."""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertEqual(dict, type(amenity_dict))

    def test_to_dict_includes_class(self):
        """Test that the dictionary includes the class name."""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIn('__class__', amenity_dict)
        self.assertEqual('Amenity', amenity_dict['__class__'])

    def test_to_dict_includes_updated_at(self):
        """Test that the dictionary includes updated_at attribute."""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIn('updated_at', amenity_dict)

    def test_to_dict_includes_created_at(self):
        """Test that the dictionary includes created_at attribute."""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIn('created_at', amenity_dict)

    def test_to_dict_includes_id(self):
        """Test that the dictionary includes id attribute."""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIn('id', amenity_dict)

    def test_to_dict_includes_custom_attrs(self):
        """Test that the dictionary includes custom attributes."""
        amenity = Amenity()
        amenity.name = 'Test'
        amenity.number = 123
        amenity_dict = amenity.to_dict()
        self.assertIn('name', amenity_dict)
        self.assertIn('number', amenity_dict)


if __name__ == '__main__':
    unittest.main()
