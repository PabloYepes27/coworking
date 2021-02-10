from flask import request, jsonify
from models.model import Spaces, SpaceSchema
from models.actions.validation_handler import handler_validations
from models.database.database import create_reservation, read_all, read_id, update_reservation, delete_reservation
from app import app, db


@app.route('/api/reservation', methods=['GET'])
def get_spaces():
    """
    Endpoint to list all the spaces

    Returns:
        [list]: [list of spaces]
    """
    result = read_all()
    return jsonify(result)

@app.route('/api/reservation', methods=['post'])
def add_reservations():
    """
    Endpoint to make a reservation

    Returns:
        [Dict]: [return a dictionary with the response message
            depending on the type of payment]
    """
    space_id = request.json['space_id']
    old = read_id(space_id)
    result, e = handler_validations(request, old)
    if e == True:
      return jsonify({'respuesta': result}), 400
    create_reservation(result, space_id)
    return jsonify({'respuesta': "Reserva correctamente añadida"})

@app.route('/api/reservation/<space_id>', methods=['delete'])
def delete_reservations(space_id):
    """
    Endpoint to delete a reservation

    Returns:
        [list]: [list of spaces]
    """
    print(space_id)
    delete_reservation(space_id)
    return jsonify({"respuesta": "Reserva correctamente eliminada"})

@app.route('/api/reservation', methods=['put'])
def update_reservations():
    """
    Endpoint to delete a reservation

    Returns:
        [list]: [list of spaces]
    """
    space_id = request.json['space_id']
    old = read_id(space_id)
    result, e = handler_validations(request, old)
    if e == True:
      return jsonify({'respuesta': result}), 400
    update_reservation(result, space_id)
    return jsonify({"respuesta": "Reserva correctamente actualizada"})