#!/usr/bin/python3
"""this module inherits from BaseModel class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """a class User that inherits from BaseModel

     Attributes:
         email (str): public class attribute for User's email
         password (str):public class attribute for User's password
         first_name (str): public class attribute for User's first_name
         last_name (str): public class attribute for User's last_name
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """init method for User class

        Attributes:
            args: list with arguments
            kwargs: a dictionary with arguments
        """
        super().__init__(*args, **kwargs)
