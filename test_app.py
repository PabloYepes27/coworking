import unittest
import os
import json
from flask import jsonify
from datetime import datetime, timedelta
from app import app, db

URL = "http://localhost:5000/api/reservation"

class SpaceTestCase(unittest.TestCase):
    """ This classs represents the reservation test case """

    def setUp(self):
        """ initialize the app and the db"""
        self.app = app
        app.config['TESTING'] = True
        self.app = app.test_client()
        db.create_all()
    
    def test_check_payment(self):
        """ Test for the payed_value """
        today = datetime.today()
        good_date_in = today + timedelta(3)
        good_date_out = today + timedelta(5)

        date_in = "{}/{}/{}".format(good_date_in.day, good_date_in.month, good_date_in.year)
        date_out = "{}/{}/{}".format(good_date_out.day, good_date_out.month, good_date_out.year)

        payment = {
            "total_value": 20000,
            "payed_value": "1520",
            "status": 1,
            "date_in": date_in,
            "date_out": date_out
        }
        res = self.app.post(URL, json=payment)
        data = json.loads(res.data)
        self.assertEqual("El valor de la reserva debe ser "
        "mayor al 10% del valor del espacio", data["respuesta"])

    # def test_valid_date(self):
    #     """ Test for the payed_value """
    #     today = datetime.today()
    #     good_date_in = today + timedelta(3)
    #     good_date_out = today + timedelta(5)
    #     bad_date_in = today + timedelta(1)
    #     bad_date_out = good_date_out + timedelta(15)
        
    #     good_payment = {
    #         "total_value": 20000,
    #         "payed_value": "2520",
    #         "status": 1,
    #         "date_in": "06/02/2021",
    #         "date_out": "08/02/2021"
    #     }
    #     bad_payment = {
    #         "total_value": 20000,
    #         "payed_value": "1520",
    #         "status": 1,
    #         "date_in": "06/02/2021",
    #         "date_out": "08/02/2021"
    #     }


    def tearDown(self):
        """ restart the tables"""
        db.session.remove()
        db.drop_all()
        db.create_all()

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()