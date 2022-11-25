#!/usr/bin/python3
"""this module inherits from BaseModel class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """a class State that inherits from BaseModel

    Attribute:
        state_id (str): public class attribute for City's id
        name (str): public class attribute for City's name
    """
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        """init method for City class

         Attributes:
        args: list with arguments
        kwargs: a dictionary with arguments
        """
        super().__init__(*args, **kwargs)
