import json
import os
from models.base_model import BaseModel
""" module to store all class objects
"""
whole_dict = {"BaseModel": BaseModel}
class FileStorage():
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
            data = {key:value.to_dict() for key,value in FileStorage.__objects.items()}
            json.dump(data, write)
     
     def reload(self): 
        """deserializes the JSON file to __objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as read:
            load_dict = json.load(read)
            obj_dict = {k:whole_dict[v["__class__"]](**v) for k, v in load_dict.items()}
            FileStorage.__objects = obj_dict

