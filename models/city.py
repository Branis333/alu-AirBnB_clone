#!/usr/bin/python3

"""city"""

from models.base_model import BaseModel

class City(BaseModel):
    """City class inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize City"""
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get('state_id', '')
        self.name = kwargs.get('name', '')
