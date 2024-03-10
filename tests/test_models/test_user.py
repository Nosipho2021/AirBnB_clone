#!/usr/bin/python3
"""Defines unittests for models/user.py.

Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User

class TestUserInstantiation(unittest.TestCase):
    """Test instantiation of User class."""

    def test_instantiation(self):
        """Test that User instance is properly instantiated."""
        user = User()
        self.assertTrue(isinstance(user, User))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


class TestUserSave(unittest.TestCase):
    """Test save method of User class."""

    def test_save(self):
        """Test that save method updates the updated_at attribute."""
        user = User()
        old_updated_at = user.updated_at
        sleep(0.1)
        user.save()
        self.assertNotEqual(user.updated_at, old_updated_at)


class TestUserToDict(unittest.TestCase):
    """Test to_dict method of User class."""

    def test_to_dict(self):
        """Test that to_dict method returns dictionary representation."""
        user = User()
        user_dict = user.to_dict()
        self.assertTrue(isinstance(user_dict, dict))
        self.assertTrue('__class__' in user_dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertTrue('created_at' in user_dict)
        self.assertTrue('updated_at' in user_dict)
        self.assertTrue('id' in user_dict)

if __name__ == '__main__':
    unittest.main()
