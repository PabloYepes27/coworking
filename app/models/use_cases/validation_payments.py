from flask import request
import re


def check_payment(total_value, payed_value):
    """
    Function to add check the payment reservation

    Args:
        idUser ([Int]): [lessee ID]
        idInmueble ([Str]): [property ID]
        valorPagado ([Int]): [value paid]
        fechaPago ([Str]): [date]
    """
    if (int(payed_value) < int(total_value) * 0.1):
        return ("El valor de la reserva debe ser mayor al 10% del valor del espacio", 400)
    else:
        return ("correcto", 200)


# def update_payment(pago, valorPagado, fechaPago):
#     """
#     function to update the data of an existing payment

#     Args:
#         pago ([Spaces]): [Spaces object]
#         valorPagado ([Int]): [value paid]
#         fechaPago ([Str]): [date]
#     """
#     pago.valorPagado = valorPagado
#     pago.fechaPago = fechaPago
#     db.session.commit()



