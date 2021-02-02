from flask import request
from app import app, db
from datetime import datetime, date
from models.use_cases.validation_payments import check_payment
from models.use_cases.validation_dates import valid_date, valid_date_in, valid_reservation_duration, convert_to_db

def handler_validations(request):
    """
    function to handle the different validations of the bussiness logic

    Returns:
        [List]: [List with the space for add or a message in case of error]
    """

    total_value = request.json['total_value']
    payed_value = request.json['payed_value']
    # status = request.json['status']
    date_in = request.json['date_in']
    date_out = request.json['date_out']

    # result, e = check_status(status)
    # if e == 400:
    #     return (result, e)
    result, e = check_payment(total_value, payed_value)
    if e == 400:
        return (result, e)
    result, e = valid_date(date_in, date_out)
    if e == 400:
        return (result, e)
    result, e = valid_date_in(date_in)
    if e == 400:
        return (result, e)
    result, e = valid_reservation_duration(date_in, date_out)
    if e == 400:
        return (result, e)
    space = convert_to_db(request)
    return(space, 200)
