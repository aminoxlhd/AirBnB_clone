#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class review(BaseModel):
    """
    Class representing reviews associated with places.

    Attributes:
        place (str): ID of the place being reviewed.
        user_id (str): ID of the user who created the review.
        comment (str): The text content of the review.
    """
    place = ""
    user_id = ""
    comment = ""
