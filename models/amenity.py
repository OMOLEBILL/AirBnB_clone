#!/usr/bin/python3
"""this module inherits from BaseModel class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """a class Amenity that inherits from BaseModel

     Attributes:
         name (str): public class attribute for Amenity's name
    """
    name = ''

    def __init__(self, *args, **kwargs):
        """init method for Amenity class

        Attributes:
            args: list with arguments
            kwargs: a dictionary with arguments
        """
        super().__init__(*args, **kwargs)
