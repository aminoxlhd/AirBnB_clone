#!/usr/bin/python3
from models.base_model import BaseModel
""" Defines 'user' class"""


class user(BaseModel):
    """Attributes that represents the user:
            first_name(str): the user's first name.
            last_name(str): the user's last name.
            email(str): the user's email.
            password: the user's password.
    """
    first_name = ""
    last_name = ""
    email = ""
    password = ""
