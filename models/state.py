#!/usr/bin/python3

"""State"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize State"""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')
