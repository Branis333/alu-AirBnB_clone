#!/usr/bin/python3

import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    def setUp(self):
        """Set up an instance of Place for testing"""
        self.place = Place()

    def test_inheritance(self):
        """Test that Place inherits from BaseModel"""
        self.assertIsInstance(self.place, BaseModel)

    def test_city_id_attr(self):
        """Test that Place has a class attribute 'city_id' initialized as an empty string"""
        self.assertTrue(hasattr(Place, 'city_id'))
        self.assertEqual(self.place.city_id, "")
        self.assertIsInstance(self.place.city_id, str)

    def test_user_id_attr(self):
        """Test that Place has a class attribute 'user_id' initialized as an empty string"""
        self.assertTrue(hasattr(Place, 'user_id'))
        self.assertEqual(self.place.user_id, "")
        self.assertIsInstance(self.place.user_id, str)

    def test_name_attr(self):
        """Test that Place has a class attribute 'name' initialized as an empty string"""
        self.assertTrue(hasattr(Place, 'name'))
        self.assertEqual(self.place.name, "")
        self.assertIsInstance(self.place.name, str)

    def test_description_attr(self):
        """Test that Place has a class attribute 'description' initialized as an empty string"""
        self.assertTrue(hasattr(Place, 'description'))
        self.assertEqual(self.place.description, "")
        self.assertIsInstance(self.place.description, str)

    def test_number_rooms_attr(self):
        """Test that Place has a class attribute 'number_rooms' initialized as 0"""
        self.assertTrue(hasattr(Place, 'number_rooms'))
        self.assertEqual(self.place.number_rooms, 0)
        self.assertIsInstance(self.place.number_rooms, int)

    def test_number_bathrooms_attr(self):
        """Test that Place has a class attribute 'number_bathrooms' initialized as 0"""
        self.assertTrue(hasattr(Place, 'number_bathrooms'))
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertIsInstance(self.place.number_bathrooms, int)

    def test_max_guest_attr(self):
        """Test that Place has a class attribute 'max_guest' initialized as 0"""
        self.assertTrue(hasattr(Place, 'max_guest'))
        self.assertEqual(self.place.max_guest, 0)
        self.assertIsInstance(self.place.max_guest, int)

    def test_price_by_night_attr(self):
        """Test that Place has a class attribute 'price_by_night' initialized as 0"""
        self.assertTrue(hasattr(Place, 'price_by_night'))
        self.assertEqual(self.place.price_by_night, 0)
        self.assertIsInstance(self.place.price_by_night, int)

    def test_latitude_attr(self):
        """Test that Place has a class attribute 'latitude' initialized as 0.0"""
        self.assertTrue(hasattr(Place, 'latitude'))
        self.assertEqual(self.place.latitude, 0.0)
        self.assertIsInstance(self.place.latitude, float)

    def test_longitude_attr(self):
        """Test that Place has a class attribute 'longitude' initialized as 0.0"""
        self.assertTrue(hasattr(Place, 'longitude'))
        self.assertEqual(self.place.longitude, 0.0)
        self.assertIsInstance(self.place.longitude, float)

    def test_amenity_ids_attr(self):
        """Test that Place has a class attribute 'amenity_ids' initialized as an empty list"""
        self.assertTrue(hasattr(Place, 'amenity_ids'))
        self.assertEqual(self.place.amenity_ids, [])
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_to_dict_includes_attributes(self):
        """Test that the 'to_dict' method includes the correct attributes"""
        place_dict = self.place.to_dict()
        self.assertIn('city_id', place_dict)
        self.assertIn('user_id', place_dict)
        self.assertIn('name', place_dict)
        self.assertIn('description', place_dict)
        self.assertIn('number_rooms', place_dict)
        self.assertIn('number_bathrooms', place_dict)
        self.assertIn('max_guest', place_dict)
        self.assertIn('price_by_night', place_dict)
        self.assertIn('latitude', place_dict)
        self.assertIn('longitude', place_dict)
        self.assertIn('amenity_ids', place_dict)

    def test_str_method(self):
        """Test the __str__ method of Place"""
        expected_str = "[Place] ({}) {}".format(self.place.id, self.place.__dict__)
        self.assertEqual(str(self.place), expected_str)

    def test_save_method(self):
        """Test the save method of Place"""
        old_updated_at = self.place.updated_at
        self.place.save()

    def test_to_dict_method(self):
        """Test the to_dict method of Place"""
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict, dict)
        expected_keys = [
            'id', 'created_at', 'updated_at', '__class__', 'city_id',
            'user_id', 'name', 'description', 'number_rooms',
            'number_bathrooms', 'max_guest', 'price_by_night', 'latitude',
            'longitude', 'amenity_ids'
        ]
        for key in expected_keys:
            self.assertIn(key, place_dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['city_id'], "")
        self.assertEqual(place_dict['user_id'], "")
        self.assertEqual(place_dict['name'], "")
        self.assertEqual(place_dict['description'], "")
        self.assertEqual(place_dict['number_rooms'], 0)
        self.assertEqual(place_dict['number_bathrooms'], 0)
        self.assertEqual(place_dict['max_guest'], 0)
        self.assertEqual(place_dict['price_by_night'], 0)
        self.assertEqual(place_dict['latitude'], 0.0)
        self.assertEqual(place_dict['longitude'], 0.0)
        self.assertEqual(place_dict['amenity_ids'], [])


if __name__ == '__main__':
    unittest.main()
