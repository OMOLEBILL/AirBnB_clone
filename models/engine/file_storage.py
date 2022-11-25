#!/usr/bin/python3
""" module to store all class objects
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.Review import Review
whole_dict = {"BaseModel": BaseModel}


class FileStorage():
    """a class that serializes instances to a JSON
       file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the objects"""
        return self.__objects

    def new(self, obj):
        """sets in all objects with key"""
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as write:
            data = {key: value.to_dict() for key, value in
                    FileStorage.__objects.items()}
            json.dump(data, write)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as read:
            load_dict = json.load(read)
            obj_dict = {k: whole_dict[v["__class__"]](**v)
                        for k, v in load_dict.items()}
            FileStorage.__objects = obj_dict
