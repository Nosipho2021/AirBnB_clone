#!/usr/bin/python3
"""Defines unittests for models/state.py.

Unittest classes:
    TestStateInstantiation
    TestStateSave
    TestStateToDict
"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestStateInstantiation(unittest.TestCase):
    """Test instantiation of State class."""

    def test_instantiation(self):
        """Test that State instance is properly instantiated."""
        state = State()
        self.assertTrue(isinstance(state, State))
        self.assertTrue(hasattr(state, 'name'))
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertEqual(state.name, "")


class TestStateSave(unittest.TestCase):
    """Test save method of State class."""

    def test_save(self):
        """Test that save method updates the updated_at attribute."""
        state = State()
        old_updated_at = state.updated_at
        sleep(0.1)
        state.save()
        self.assertNotEqual(state.updated_at, old_updated_at)


class TestStateToDict(unittest.TestCase):
    """Test to_dict method of State class."""

    def test_to_dict(self):
        """Test that to_dict method returns dictionary representation."""
        state = State()
        state_dict = state.to_dict()
        self.assertTrue(isinstance(state_dict, dict))
        self.assertTrue('__class__' in state_dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertTrue('created_at' in state_dict)
        self.assertTrue('updated_at' in state_dict)
        self.assertTrue('id' in state_dict)
        self.assertTrue('name' in state_dict)

if __name__ == '__main__':
    unittest.main()
