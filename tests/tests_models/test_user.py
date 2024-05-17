#!/usr/bin/python3

import unittest
import uuid
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from models.user import User
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize User instance"""
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')
        self.id = kwargs.get('id', str(uuid.uuid4()))

    def __str__(self):
        """String representation of User"""
        return "[User] ({}) {}".format(self.id, self.__dict__)

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'test@example.com',
            'password': 'password123',
            'first_name': 'Daniel',
            'last_name': 'Show'
        }
        self.user = User(**self.user_data)

    def test_user_attributes(self):
        self.assertEqual(self.user.email, self.user_data['email'])
        self.assertEqual(self.user.password, self.user_data['password'])
        self.assertEqual(self.user.first_name, self.user_data['first_name'])
        self.assertEqual(self.user.last_name, self.user_data['last_name'])

    def test_string_representation(self):
        expected_string = "[User] ({}) {}".format(
        self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), expected_string)

if __name__ == '__main__':
    unittest.main()
