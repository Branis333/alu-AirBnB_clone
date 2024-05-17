#!/usr/bin/python3
"""This module creates a Place class"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Class for managing place objects"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def to_dict(self):
        """
        Converts instance attributes to dictionary
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['city_id'] = self.city_id
        new_dict['user_id'] = self.user_id
        new_dict['name'] = self.name
        new_dict['description'] = self.description
        new_dict['number_rooms'] = self.number_rooms
        new_dict['number_bathrooms'] = self.number_bathrooms
        new_dict['max_guest'] = self.max_guest
        new_dict['price_by_night'] = self.price_by_night
        new_dict['latitude'] = self.latitude
        new_dict['longitude'] = self.longitude
        new_dict['amenity_ids'] = self.amenity_ids
        return new_dict
