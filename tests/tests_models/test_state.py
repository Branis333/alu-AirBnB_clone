#!/usr/bin/python3

import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    def setUp(self):
        """Set up an instance of State for testing"""
        self.state = State()

    def test_inheritance(self):
        """Test that State inherits from BaseModel"""
        self.assertIsInstance(self.state, BaseModel)

    def test_name_attr(self):
        """Test that State has a class attribute 'name' initialized as an empty string"""
        self.assertTrue(hasattr(State, 'name'))
        self.assertEqual(self.state.name, "")
        self.assertIsInstance(self.state.name, str)

    def test_to_dict_includes_attributes(self):
        """Test that the 'to_dict' method includes the 'name' attribute"""
        self.state.name = "California"
        state_dict = self.state.to_dict()
        self.assertIn('name', state_dict)
        self.assertEqual(state_dict['name'], "California")

    def test_str_method(self):
        """Test the __str__ method of State"""
        expected_str = "[State] ({}) {}".format(self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), expected_str)

    def test_save_method(self):
        """Test the save method of State"""
        old_updated_at = self.state.updated_at
        self.state.save()

    def test_to_dict_method(self):
        """Test the to_dict method of State"""
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        expected_keys = ['id', 'created_at', 'updated_at', '__class__', 'name']
        self.assertEqual(state_dict['__class__'], 'State')


if __name__ == '__main__':
    unittest.main()
