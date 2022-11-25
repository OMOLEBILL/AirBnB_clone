#!/usr/bin/python3
"""this module inherits from BaseModel class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """a class State that inherits from BaseModel

    Attribute:
        name (str): public class attribute for State's name
    """
    name = ''

    def __init__(self, *args, **kwargs):
        """init method for State class

         Attributes:
        args: list with arguments
        kwargs: a dictionary with arguments
        """
        super().__init__(*args, **kwargs)
