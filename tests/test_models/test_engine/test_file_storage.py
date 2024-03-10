#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import json
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_no_args_instantiates(self):
        """Test that FileStorage instance is properly instantiated with no arguments."""
        storage = FileStorage()
        self.assertEqual(FileStorage, type(storage))

    def test_objects_empty_dict(self):
        """Test that objects attribute is an empty dictionary."""
        storage = FileStorage()
        self.assertEqual({}, storage._FileStorage__objects)

    def test_file_path_is_str(self):
        """Test that file_path attribute is a string."""
        storage = FileStorage()
        self.assertEqual(str, type(storage._FileStorage__file_path))

    def test_file_path_exists(self):
        """Test that file_path attribute exists."""
        storage = FileStorage()
        self.assertTrue(hasattr(storage, '_FileStorage__file_path'))

    def test_file_path_default_value(self):
        """Test that file_path attribute has default value."""
        storage = FileStorage()
        self.assertEqual('file.json', storage._FileStorage__file_path)

    def test_file_path_env_var(self):
        """Test that file_path attribute gets value from environment variable."""
        os.environ['HBNB_ENV'] = 'test'
        storage = FileStorage()
        self.assertEqual('file_test.json', storage._FileStorage__file_path)

    def test_empty_dict_created(self):
        """Test that an empty dictionary is created if file doesn't exist."""
        if os.path.exists('file.json'):
            os.remove('file.json')
        storage = FileStorage()
        self.assertEqual({}, storage.all())

    def test_all_method(self):
        """Test that all method returns the __objects attribute."""
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__objects, storage.all())


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    def test_new_method(self):
        """Test that new method adds object to __objects."""
        storage = FileStorage()
        user = User()
        storage.new(user)
        key = "{}.{}".format(user.__class__.__name__, user.id)
        self.assertIn(key, storage._FileStorage__objects.keys())
        self.assertEqual(user, storage._FileStorage__objects[key])

    def test_new_method_with_args(self):
        """Test that new method adds object with specific key to __objects."""
        storage = FileStorage()
        user = User()
        key = "{}.{}".format(user.__class__.__name__, user.id)
        storage.new(user)
        self.assertIn(key, storage.all().keys())

    def test_save_method(self):
        """Test that save method serializes __objects to JSON file."""
        if os.path.exists('file.json'):
            os.remove('file.json')
        storage = FileStorage()
        user = User()
        storage.new(user)
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_save_method_with_args(self):
        """Test that save method serializes specific object to JSON file."""
        if os.path.exists('file.json'):
            os.remove('file.json')
        storage = FileStorage()
        user = User()
        storage.new(user)
        storage.save()
        with open('file.json', 'r') as file:
            data = json.load(file)
            key = "{}.{}".format(user.__class__.__name__, user.id)
            self.assertIn(key, data.keys())


if __name__ == '__main__':
    unittest.main()





