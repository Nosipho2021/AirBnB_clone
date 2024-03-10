#!/usr/bin/python3
"""Define unittests for console.py"""

Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""

import unittest
from console import HBNBCommand

class TestHBNBCommand_prompting(unittest.TestCase):
    def test_prompting(self):
    """Test if the prompt is correctly displayed."""
    pass

class TestHBNBCommand_help(unittest.TestCase):
    def test_help(self):
    """Test help command."""
    pass

class TestHBNBCommand_exit(unittest.TestCase):
    def test_exit(self):
    """Test exit command."""
    pass

class TestHBNBCommand_create(unittest.TestCase):
    def test_create(self):
    """Test create command."""
    pass

class TestHBNBCommand_show(unittest.TestCase):
    def test_show(self):
    """Test show command."""
    pass

class TestHBNBCommand_all(unittest.TestCase):
    def test_all(self):
    """Test all command."""
    pass

class TestHBNBCommand_destroy(unittest.TestCase):
    def test_destroy(self):
    """Test destroy command."""
    pass

class TestHBNBCommand_update(unittest.TestCase):
    def test_update(self):
    """Test update command."""
    pass

if __name__ == '__main__':
    unittest.main()
