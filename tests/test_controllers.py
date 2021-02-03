import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import sys

from app import app, db
from models.model import Spaces
from test_models import format_dates


URL = "http://localhost:5000/api/reservation"


class ControllersTestCase(unittest.TestCase):
    """ Integration tests for the controller layer """

    def setUp(self):
        """ initialize the app and the db"""
        self.app = app
        app.config['TESTING'] = True
        self.app = app.test_client()
        db.create_all()

    def test_get_spaces(self):
        """test the GET method"""
        res = self.app.get(URL)
        self.assertEqual(res.status_code, 200)

    def test_add_space(self):
        """test the GET method"""
        today = datetime.today()
        date_in = format_dates(today + timedelta(3))
        date_out = format_dates(today + timedelta(5))

        reservation = {
            "total_value": 20000,
            "payed_value": 4200,
            "status": 1,
            "date_in": date_in,
            "date_out": date_out
        }
        res = self.app.post(URL, json=reservation)
        self.assertEqual(res.status_code, 200)

    # def test_delete_space(self):
    #     """test the GET method"""
    #     today = datetime.today()
    #     date_in = format_dates(today + timedelta(3))
    #     date_out = format_dates(today + timedelta(5))

    #     reservation = {
    #         "total_value": 20000,
    #         "payed_value": 4200,
    #         "status": 1,
    #         "date_in": date_in,
    #         "date_out": date_out
    #     }
    #     self.app.post(URL, json=reservation)

    #     res = self.app.get(URL)
    #     response = json.loads(res.get_data().decode(sys.getdefaultencoding()))

    #     reservation = {"space_id": 1}
    #     res = self.app.delete(URL,
    #                           data=reservation,
    #                           headers={'Content-Type': 'application/JSON'})
    #     self.assertEqual(res.status_code, 400)

    def tearDown(self):
        """ restart the tables"""
        db.session.remove()
        db.drop_all()
        db.create_all()

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()