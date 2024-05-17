#!/usr/bin/python3
"""This module creates a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __str__(self):
        """String representation of User"""
        return "[User] ({}) {}".format(self.id, self.user_data)
