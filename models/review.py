#!/usr/bin/python3
"""This module creates a Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class for managing review objects"""

    place_id = ""
    user_id = ""
    text = ""

    def to_dict(self):
        """
        Converts instance attributes to dictionary
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['place_id'] = self.place_id
        new_dict['user_id'] = self.user_id
        new_dict['text'] = self.text
        return new_dict
