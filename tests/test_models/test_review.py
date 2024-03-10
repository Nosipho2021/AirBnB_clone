#!/usr/bin/python3
"""Defines unittests for models/review.py.

Unittest classes:
    TestReview_instantiation
    TestReview_save
    TestReview_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_no_args_instantiates(self):
        """Test that Review instance is properly instantiated with no arguments."""
        review = Review()
        self.assertEqual(Review, type(review))

    def test_new_instance_stored_in_objects(self):
        """Test that new instance of Review is stored in objects."""
        review = Review()
        self.assertIn(review, models.storage.all().values())


class TestReview_save(unittest.TestCase):
    """Unittests for testing save method of the Review class."""

    def test_save_updates_updated_at(self):
        """Test that calling save updates the updated_at attribute."""
        review = Review()
        old_updated_at = review.updated_at
        sleep(0.1)
        review.save()
        new_updated_at = review.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_save_creates_file(self):
        """Test that calling save creates a corresponding JSON file."""
        review = Review()
        review.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_save_updated_objects(self):
        """Test that calling save updates the objects dictionary."""
        review = Review()
        review.save()
        key = "{}.{}".format(review.__class__.__name__, review.id)
        self.assertIn(key, models.storage.all().keys())


class TestReview_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Review class."""

    def test_to_dict_returns_dict(self):
        """Test that to_dict returns a dictionary."""
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(dict, type(review_dict))

    def test_to_dict_includes_class(self):
        """Test that the dictionary includes the class name."""
        review = Review()
        review_dict = review.to_dict()
        self.assertIn('__class__', review_dict)
        self.assertEqual('Review', review_dict['__class__'])

    def test_to_dict_includes_updated_at(self):
        """Test that the dictionary includes updated_at attribute."""
        review = Review()
        review_dict = review.to_dict()
        self.assertIn('updated_at', review_dict)

    def test_to_dict_includes_created_at(self):
        """Test that the dictionary includes created_at attribute."""
        review = Review()
        review_dict = review.to_dict()
        self.assertIn('created_at', review_dict)

    def test_to_dict_includes_id(self):
        """Test that the dictionary includes id attribute."""
        review = Review()
        review_dict = review.to_dict()
        self.assertIn('id', review_dict)

    def test_to_dict_includes_custom_attrs(self):
        """Test that the dictionary includes custom attributes."""
        review = Review()
        review.text = 'Test'
        review.rating = 5
        review_dict = review.to_dict()
        self.assertIn('text', review_dict)
        self.assertIn('rating', review_dict)


if __name__ == '__main__':
    unittest.main()
