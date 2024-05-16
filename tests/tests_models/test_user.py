#!/usr/bin/python3

import unittest
from models.user import User
from models.base_model import BaseModel


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
        expected_string = "[User] ({}) {}".format(self.user.id, self.user_data)
        self.assertEqual(str(self.user), expected_string)

if __name__ == '__main__':
    unittest.main()
