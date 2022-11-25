#!/usr/bin/python3
"""this module inherits from BaseModel class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """a class Place that inherits from BaseModel

     Attributes:
         city_id (str): public class attribute for Place's city_id
         user_id (str):public class attribute for Place's user_id
         name (str): public class attribute for Place's name
         description (str): public class attribute for Place's description
         number_rooms (int): public class attribute for Place's number_rooms
         number_bathrooms (int):public class attribute for Place's
         number_bathrooms
         max_guest (int): public class attribute for Place's max_guest
         price_by_night (int): public class attribute for Place's
         price_by_night
         latitude (float):public class attribute for Place's latitude
         longitude (float): public class attribute for Place's longitude
         amenity_ids (str): public class attribute for Place's amenity_ids
    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """init method for Place class

        Attributes:
            args: list with arguments
            kwargs: a dictionary with arguments
        """
        super().__init__(*args, **kwargs)
