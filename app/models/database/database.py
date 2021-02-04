from models.model import Spaces, SpaceSchema
from app import db


def create(result: list):
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

def update(result):
    space_id = result["space_id"]
    space = Spaces.query.get(space_id)
    space.payed_value = result["payed_value"]
    space.status = result["status"]
    space.date_out = result["date_out"]
    db.session.commit()

def delete(space_id):
    space = read_id(space_id)
    db.session.delete(space)
    db.session.commit()