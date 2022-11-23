#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
"""this module defines all common attributes used in this project"""


class BaseModel:
    """This class defines all common attributes used in this project"""
    def __init__(self, *args, **kwargs):
        if kwargs != None and kwargs != {}:
            for key in kwargs.keys():
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """prints [<class name>] (<self.id>) <self.__dict__>
        """
        return (f"[{type(self).__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates the public instance attribute updated_at with
           the current datetime """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
           of __dict__ of the instance"""
        tempdict = self.__dict__.copy()
        tempdict["__class__"] = type(self).__name__
        tempdict["created_at"] = tempdict["created_at"].isoformat()
        tempdict["updated_at"] = tempdict["updated_at"].isoformat()
        return tempdict
