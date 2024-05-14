#!/usr/bin/python3

"""Amenity"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize Amenity"""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')
