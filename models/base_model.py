#!/usr/bin/python3
import uuid
import datetime
"""this module defines all common attributes used in this project"""


class BaseModel:
    """This class defines all common attributes used in this project"""
    def __init__(self, id=None, created_at=None, updated_at=None):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """prints [<class name>] (<self.id>) <self.__dict__>
        """
        return (f"[{__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates the public instance attribute updated_at with
           the current datetime """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values 
           of __dict__ of the instance
        """
        self.__dict__['__class__'] = f"{__class__.__name__}"
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()
        return self.__dict__
