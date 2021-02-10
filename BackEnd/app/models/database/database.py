from models.model import Spaces, SpaceSchema
from app import db
from datetime import datetime


def create_space(result: list):
    new_reservation = Spaces(result[0], result[1], result[2], result[3], result[4])
    db.session.add(new_reservation)
    db.session.commit()

def read_all():
    all_spaces = Spaces.query.all()
    result = SpaceSchema(many=True).dump(all_spaces)
    return result

def read_id(space_id):
    space = Spaces.query.get(space_id)
    return space

def update_reservation(result, space_id):
    space = Spaces.query.get(space_id)
    space.payed_value = result["payed_value"]
    space.status = result["status"]
    space.date_in = result["date_in"]
    space.date_out = result["date_out"]
    db.session.commit()

def create_reservation(result, space_id):
    space = Spaces.query.get(space_id)
    space.payed_value = result["payed_value"]
    space.status = True
    space.date_in = result["date_in"]
    space.date_out = result["date_out"]
    db.session.commit()

def update_space(result):
    space_id = result["space_id"]
    space = Spaces.query.get(space_id)
    space.payed_value = result["payed_value"]
    space.status = result["status"]
    space.date_out = result["date_out"]
    db.session.commit()

def delete_reservation(space_id):
    space = read_id(space_id)
    space.status = False
    space.payed_value = 0
    space.date_in = datetime.today()
    space.date_out = datetime.today()
    db.session.commit()

def delete_space(space_id):
    space = read_id(space_id)
    db.session.delete(space)
    db.session.commit()