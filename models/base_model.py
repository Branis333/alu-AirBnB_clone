#!/usr/bin/python3

import datetime
import uuid

import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initializes BaseModel
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "update_at":
                    value = datetime.datetime.strptime(value,
                                                       "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):

       return "[{}] ({}) {}".format(self.__class__.__name__,
                                self.id, self.__dict__)

    def save(self):
        """ 
        Updates the public instance attribute with current date time
        """
       self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Converts instance attributes to dictionary
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
