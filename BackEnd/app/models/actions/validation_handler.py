from app import app, db
from datetime import datetime, date
from models.actions.validation_payments import check_payment
from models.actions.validation_dates import valid_date, valid_date_in, valid_reservation_duration, convert_to_db
from models.database.database import read_id
from flask import jsonify

def handler_validations(new_request, old):
    """
    function to handle the different validations of the bussiness logic

    Returns:
        [List]: [List with the space for add or a message in case of error]
    """


    total_value = old.total_value
    payed_value = new_request.json['payed_value']
    # status = new_request.json['status']
    date_in = new_request.json['date_in']
    date_out = new_request.json['date_out']

    # result, e = check_status(status)
    # if e == True:
    #     return (result, e)
    result, e = check_payment(total_value, payed_value)
    if e == True:
        return (result, e)
    result, e = valid_date(date_in, date_out)
    if e == True:
        return (result, e)
    result, e = valid_date_in(date_in)
    if e == True:
        return (result, e)
    result, e = valid_reservation_duration(date_in, date_out)
    if e == True:
        return (result, e)
    space = convert_to_db(new_request)
    return(space, False)
