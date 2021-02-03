from flask import request
from datetime import datetime, date
import re


def valid_date(date_in, date_out):
    """
    function to valdiate the format and day of the date

    Args:
        fechaPago ([Str]): [date of the payment]
    """
    x = re.search("^\d{2}\/\d{2}\/\d{4}$", date_in)
    y = re.search("^\d{2}\/\d{2}\/\d{4}$", date_out)
    if x and y:
        return ("Correcto", 200)
    else:
        return ("Formato de fechas incorrecto", 400)

def valid_date_in(date_in):
    today = datetime.today()
    date_in = "{}{}".format(date_in[0:6], date_in[-2:])
    date_in = datetime.strptime(date_in, '%d/%m/%y')
    if abs(date_in - today).days < 2:
        return ("La reserva debe hacerse con mínimo 2 días de anticipación", 400)
    return ("Correcto", 200)

def valid_reservation_duration(date_in, date_out):
    date_in = "{}{}".format(date_in[0:6], date_in[-2:])
    date_in = datetime.strptime(date_in, '%d/%m/%y')

    date_out = "{}{}".format(date_out[0:6], date_out[-2:])
    date_out = datetime.strptime(date_out, '%d/%m/%y')

    if abs(date_out - date_in).days > 14:
        return ("La duración de la reserva no puede superar las dos semanas", 400)
    return ("Correcto", 200)

def convert_to_db(request):
    """function to convert the dates formats

    Args:
        date_in ([type]): [description]
        date_out ([type]): [description]

    Returns:
        [type]: [description]
    """
    day_in, month_in, year_in = request.json['date_in'].split('/')
    date_in = "{}-{}-{}".format(year_in, month_in, day_in)

    day, month, year = request.json['date_out'].split('/')
    date_out = "{}-{}-{}".format(year, month, day)

    space_db = []
    space_db.append(request.json['total_value'])
    space_db.append(request.json['payed_value'])
    space_db.append(request.json['status'])
    space_db.append(date_in)
    space_db.append(date_out)

    return (space_db)