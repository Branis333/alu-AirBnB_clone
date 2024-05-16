#!/usr/bin/python3

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    def setUp(self):
        """Set up an instance of Amenity for testing"""
        self.amenity = Amenity()

    def test_inheritance(self):
        """Test that Amenity inherits from BaseModel"""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_name_attr(self):
        """Test that Amenity has a class attribute 'name' initialized as an empty string"""
        self.assertTrue(hasattr(Amenity, 'name'))
        self.assertEqual(self.amenity.name, "")
        self.assertIsInstance(self.amenity.name, str)

    def test_to_dict_includes_name(self):
        """Test that the 'to_dict' method includes the 'name' attribute"""
        self.amenity.name = "Wi-Fi"
        amenity_dict = self.amenity.to_dict()
        self.assertIn('name', amenity_dict)
        self.assertEqual(amenity_dict['name'], "Wi-Fi")

    def test_str_method(self):
        """Test the __str__ method of Amenity"""
        expected_str = "[Amenity] ({}) {}".format(self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_str)

    def test_save_method(self):
        """Test the save method of Amenity"""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(self.amenity.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method of Amenity"""
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        expected_keys = ['id', 'created_at', 'updated_at', '__class__', 'name']
        for key in expected_keys:
            self.assertIn(key, amenity_dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['name'], "")


if __name__ == '__main__':
    unittest.main()
