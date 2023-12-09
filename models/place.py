#!/usr/bin/python3
from models.base_model import BaseModel
"""Defines the Place class."""


class place(BaseModel):
    """
    Class representing places available for booking.

    Attributes:
        city (str): The ID of the city where the place is located.
        user_id (str): The ID of the user who owns the place.
        name (str): The name of the place.
        description (str): A brief description of the place.
        number_of_rooms (int): The number of rooms in the place.
        number_of_bathrooms (int): The number of bathrooms in the place.
        maximum_guests (int): The maximum number of guests the place can accommodate.
        price_by_night (int): The price per night for booking the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        amenity_ids (list): A list of amenity IDs associated with the place.
    """

    city = ""
    user_id = ""
    name = ""
    description = ""
    number_of_rooms = 0
    number_of_bathrooms = 0
    maximum_guests = 0
    price_by_night = 0
    lat = 0.0
    lon = 0.0
    amenity_ids = []
