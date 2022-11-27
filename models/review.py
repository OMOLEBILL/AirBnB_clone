#!/usr/bin/python3
"""this module inherits from BaseModel class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """a class Review that inherits from BaseModel

    Attributes:
        place_id (str): public class attribute for Review's id
        user_id (str): public class attribute for Review's id
        text (str): public class attribute for Review's text
    """
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """init method for Review class

         Attributes:
        args: list with arguments
        kwargs: a dictionary with arguments
        """
        super().__init__(*args, **kwargs)
