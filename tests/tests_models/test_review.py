#!/usr/bin/python3

import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    def setUp(self):
        """Set up an instance of Review for testing"""
        self.review = Review()

    def test_inheritance(self):
        """Test that Review inherits from BaseModel"""
        self.assertIsInstance(self.review, BaseModel)

    def test_place_id_attr(self):
        """Test that Review has a class attribute 'place_id' initialized as an empty string"""
        self.assertTrue(hasattr(Review, 'place_id'))
        self.assertEqual(self.review.place_id, "")
        self.assertIsInstance(self.review.place_id, str)

    def test_user_id_attr(self):
        """Test that Review has a class attribute 'user_id' initialized as an empty string"""
        self.assertTrue(hasattr(Review, 'user_id'))
        self.assertEqual(self.review.user_id, "")
        self.assertIsInstance(self.review.user_id, str)

    def test_text_attr(self):
        """Test that Review has a class attribute 'text' initialized as an empty string"""
        self.assertTrue(hasattr(Review, 'text'))
        self.assertEqual(self.review.text, "")
        self.assertIsInstance(self.review.text, str)

    def test_to_dict_includes_attributes(self):
        """Test that the 'to_dict' method includes the 'place_id', 'user_id', and 'text' attributes"""
        self.review.place_id = "1234"
        self.review.user_id = "5678"
        self.review.text = "Great place!"
        review_dict = self.review.to_dict()
        self.assertIn('place_id', review_dict)
        self.assertIn('user_id', review_dict)
        self.assertIn('text', review_dict)
        self.assertEqual(review_dict['place_id'], "1234")
        self.assertEqual(review_dict['user_id'], "5678")
        self.assertEqual(review_dict['text'], "Great place!")

    def test_str_method(self):
        """Test the __str__ method of Review"""
        expected_str = "[Review] ({}) {}".format(self.review.id, self.review.__dict__)
        self.assertEqual(str(self.review), expected_str)

    def test_save_method(self):
        """Test the save method of Review"""
        old_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(self.review.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method of Review"""
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        expected_keys = ['id', 'created_at', 'updated_at', '__class__', 'place_id', 'user_id', 'text']
        for key in expected_keys:
            self.assertIn(key, review_dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['place_id'], "")
        self.assertEqual(review_dict['user_id'], "")
        self.assertEqual(review_dict['text'], "")


if __name__ == '__main__':
    unittest.main()
