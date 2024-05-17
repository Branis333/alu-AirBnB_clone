#!/usr/bin/python3

import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    def setUp(self):
        """Set up an instance of City for testing"""
        self.city = City()

    def test_inheritance(self):
        """Test that City inherits from BaseModel"""
        self.assertIsInstance(self.city, BaseModel)

    def test_state_id_attr(self):
        """Test that City has a class attribute 'state_id' initialized as an empty string"""
        self.assertTrue(hasattr(City, 'state_id'))
        self.assertEqual(self.city.state_id, "")
        self.assertIsInstance(self.city.state_id, str)

    def test_name_attr(self):
        """Test that City has a class attribute 'name' initialized as an empty string"""
        self.assertTrue(hasattr(City, 'name'))
        self.assertEqual(self.city.name, "")
        self.assertIsInstance(self.city.name, str)

    def test_to_dict_includes_attributes(self):
        """Test that the 'to_dict' method includes the 'state_id' and 'name' attributes"""
        self.city.state_id = "1234"
        self.city.name = "San Francisco"
        city_dict = self.city.to_dict()
        self.assertIn('state_id', city_dict)
        self.assertIn('name', city_dict)
        self.assertEqual(city_dict['state_id'], "1234")
        self.assertEqual(city_dict['name'], "San Francisco")

    def test_str_method(self):
        """Test the __str__ method of City"""
        expected_str = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), expected_str)

    def test_save_method(self):
        """Test the save method of City"""
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(self.city.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method of City"""
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        expected_keys = ['id', 'created_at', 'updated_at', '__class__', 'state_id', 'name']
        for key in expected_keys:
            self.assertIn(key, city_dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['state_id'], "")
        self.assertEqual(city_dict['name'], "")


if __name__ == '__main__':
    unittest.main()
