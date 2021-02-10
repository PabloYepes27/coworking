from flask import request
from app import app, db
from models.model import Spaces, SpaceSchema
import re


def check_status(space_id):
    """
    Function to check the status of a space

    """
    space = Spaces.query.get(space_id)
    if (space.space_id == 1):
        return ("El espacio se encuentra reservado", 400)
    else:
        return ("correcto", 200)