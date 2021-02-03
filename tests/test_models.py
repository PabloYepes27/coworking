import unittest
from unittest import mock
import os
import json
from flask import jsonify
from datetime import datetime, timedelta
import sys


from models.use_cases.validation_payments import check_payment
from models.use_cases.validation_dates import (
    valid_date,
    valid_date_in,
    valid_reservation_duration,
    convert_to_db
)

def format_dates(date):
    if len(str(date.day)) == 1:
        day = "0{}".format(str(date.day))
    else:
        day = str(date.day)
    if len(str(date.month)) == 1:
        month = "0{}".format(str(date.month))
    else:
        month = str(date.month)
    date = "{}/{}/{}".format(day, month, date.year)
    return (date)

class BussinessLogicTestCase(unittest.TestCase):
    """Unittests for the domaing layer"""


    def test_valid_date_passed(self):
        good_date_in = "12/05/2019"
        bad_date_in = "2019/05/21"
        good_date_out = "05/12/2018"
        bad_date_out = "15/02/21"

        message1, e1 = valid_date(good_date_in, good_date_out)
        message2, e2 = valid_date(bad_date_in, bad_date_out)

        self.assertEqual(e1, 200)

    def test_valid_date_failed(self):
        good_date_in = "12/05/2019"
        bad_date_in = "2019/05/21"
        good_date_out = "05/12/2018"
        bad_date_out = "15/02/21"

        message1, e1 = valid_date(good_date_in, good_date_out)
        message2, e2 = valid_date(bad_date_in, bad_date_out)

        self.assertEqual(e2, 400)

    def test_valid_date_message(self):
        good_date_in = "12/05/2019"
        bad_date_in = "2019/05/21"
        good_date_out = "05/12/2018"
        bad_date_out = "15/02/21"
        expected_bad_message = "Formato de fechas incorrecto"

        message1, e1 = valid_date(good_date_in, good_date_out)
        message2, e2 = valid_date(bad_date_in, bad_date_out)

        self.assertEqual(message2, expected_bad_message)


    def test_valid_date_in(self):
        today = datetime.today()
        good_date_in = format_dates(today + timedelta(5))
        bad_date_in = format_dates(today + timedelta(1))

        expected_bad_message = "La reserva debe hacerse con mínimo 2 días de anticipación"

        message1, e1 = valid_date_in(good_date_in)
        message2, e2 = valid_date_in(bad_date_in)

        self.assertEqual(e1, 200)
        self.assertEqual(e2, 400)
        self.assertEqual(message2, expected_bad_message)


    def test_valid_reservation_duration_passed(self):
        today = datetime.today()
        good_date_in = format_dates(today + timedelta(4))
        good_date_out = format_dates(today + timedelta(6))
        bad_date_out = format_dates(today + timedelta(4) + timedelta(15))
  

        message1, e1 = valid_reservation_duration(good_date_in, good_date_out)
        message2, e2 = valid_reservation_duration(good_date_in, bad_date_out)

        self.assertEqual(e1, 200)

    def test_valid_reservation_duration_failed(self):
        today = datetime.today()
        good_date_in = format_dates(today + timedelta(4))
        good_date_out = format_dates(today + timedelta(6))
        bad_date_out = format_dates(today + timedelta(4) + timedelta(15))

        message1, e1 = valid_reservation_duration(good_date_in, good_date_out)
        message2, e2 = valid_reservation_duration(good_date_in, bad_date_out)

        self.assertEqual(e2, 400)

    def test_valid_reservation_duration_message(self):
        today = datetime.today()
        good_date_in = format_dates(today + timedelta(4))
        good_date_out = format_dates(today + timedelta(6))
        bad_date_out = format_dates(today + timedelta(4) + timedelta(15))

        expected_bad_message = "La duración de la reserva no puede superar las dos semanas"   

        message1, e1 = valid_reservation_duration(good_date_in, good_date_out)
        message2, e2 = valid_reservation_duration(good_date_in, bad_date_out)

        self.assertEqual(message2, expected_bad_message)


    def test_check_payment_passed(self):
        total_value = 50000
        good_payed_value = 7000
        bad_payed_value = 2000

        message1, e1 = check_payment(total_value, good_payed_value)
        message2, e2 = check_payment(total_value, bad_payed_value)

        self.assertEqual(e1, 200)

    def test_check_payment_failed(self):
        total_value = 50000
        good_payed_value = 7000
        bad_payed_value = 2000  

        message1, e1 = check_payment(total_value, good_payed_value)
        message2, e2 = check_payment(total_value, bad_payed_value)

        self.assertEqual(e2, 400)

    def test_check_payment_failed_message(self):
        total_value = 50000
        good_payed_value = 7000
        bad_payed_value = 2000

        expected_bad_message = "El valor de la reserva debe ser mayor al 10% del valor del espacio"  

        message1, e1 = check_payment(total_value, good_payed_value)
        message2, e2 = check_payment(total_value, bad_payed_value)

        self.assertEqual(message2, expected_bad_message)

    # @mock.patch("validation_date.valid_date", return_value=[])
    # def test_convert_to_db(mock_response):
        # mock_response.return_value = []

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()