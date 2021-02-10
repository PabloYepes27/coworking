from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
from app import db, ma

class Spaces(db.Model):
    """
    model of the SQL table "Spaces" to be able to make the relations

    Args:
        db ([type]): [Connection to the SQLAlchemy]
    """
    __tablename__ = 'spaces'
    space_id = db.Column(db.Integer, primary_key=True, nullable=False)
    total_value = db.Column(db.Integer, nullable=False)
    payed_value = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False)
    date_in = db.Column(db.Date, nullable=False)
    date_out = db.Column(db.Date, nullable=False)

    def __init__(self, total_value, payed_value,\
         status, date_in, date_out):
        self.total_value = total_value
        self.payed_value = payed_value
        self.status = status
        self.date_in = date_in
        self.date_out = date_out

db.create_all()

class SpaceSchema(ma.Schema):
    """
    representation of the table "spaces"

    Args:
        ma ([type]): [Connection to Marshmallow class]
    """
    class Meta:
        fields = ('space_id', 'total_value', 'payed_value',
         'status', 'date_in', 'date_out')



