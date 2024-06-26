import datetime
import uuid
import models


class BaseModel:
    """
    BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes BaseModel
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    if isinstance(value, str):value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """
        Returns string representation of BaseModel
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute with current date time
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts instance attributes to dictionary
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()

        return new_dict
        """ 
        Adding attributes if they exist
        """
        if hasattr(self, 'state_id'):
            new_dict['state_id'] = self.state_id
        if hasattr(self, 'name'):
            new_dict['name'] = self.name
        if hasattr(self, 'city_id'):
            new_dict['city_id'] = self.city_id
        if hasattr(self, 'description'):
            new_dict['description'] = self.description
        if hasattr(self, 'city_id'):
            new_dict['city_id'] = self.city_id
        return new_dict

        
