import unittest
from unittest import mock, TestCase
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import sys

from app import app, db
from models.model import Spaces
from controllers.controller import get_spaces, add_space, delete_space
from test_models import format_dates


URL = "http://localhost:5000/api/reservation"


class ControllersTestCase(TestCase):
    """ Integration tests for the controller layer """

    def setUp(self):
        """ initialize the app and the db"""
        today = datetime.today()
        date_in = format_dates(today + timedelta(3))
        date_out = format_dates(today + timedelta(5))

        self.reservation = {
            "total_value": 20000,
            "payed_value": 4200,
            "status": 1,
            "date_in": date_in,
            "date_out": date_out
        }
        self.app = app
        app.config['TESTING'] = True
        self.app = app.test_client()
        db.create_all()

    @mock.patch("controller.get_spaces")
    def test_get_spaces(self, mock_response):
        """test the GET method"""
        expected_response = [
            {
                "date_in": date_in,
                "date_out": date_out,
                "payed_value": 4200,
                "status": true,
                "total_value": 20000
            }
        ]
        mock_response.return_value = expected_response
        res = self.app.get(URL)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res, expected_response)

    def test_add_space(self):
        """test the GET method"""
        res = self.app.post(URL, json=reservation)
        self.assertEqual(res.status_code, 200)

    def test_delete_space(self):
        """test the GET method"""
        self.app.post(URL, json=reservation)
        res = self.app.get(URL)
        response = json.loads(res.get_data().decode(sys.getdefaultencoding()))
        reserv = {'space_id': response["space_id"]}
        res = self.app.delete(URL,
                              data=reserv,
                              headers={'Content-Type': 'application/JSON'})
        self.assertEqual(res.status_code, 400)

    def tearDown(self):
        """ restart the tables"""
        db.session.remove()
        db.drop_all()
        db.create_all()

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()