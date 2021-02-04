from flask import request, jsonify
from models.model import Spaces, SpaceSchema
from models.actions.validation_handler import handler_validations
from models.database.database import create, read_all, read_id, update, delete
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

@app.route('/api/reservation', methods=['Post'])
def add_space():
    """
    Endpoint to make a reservation

    Returns:
        [Dict]: [return a dictionary with the response message
            depending on the type of payment]
    """
    result, e = handler_validations(request)
    if e == True:
      return jsonify({'respuesta': result}), 400
    create(result)
    return jsonify({'respuesta': "Reserva correctamente agregada"})

@app.route('/api/reservation', methods=['delete'])
def delete_space():
    """
    Endpoint to delete a reservation

    Returns:
        [list]: [list of spaces]
    """
    space_id = request.json['space_id']
    delete(space_id)
    return jsonify({"respuesta": "Reserva correctamente eliminada"})

@app.route('/api/reservation', methods=['put'])
def update_space():
    """
    Endpoint to delete a reservation

    Returns:
        [list]: [list of spaces]
    """
    result, e = handler_validations(request)
    if e == True:
      return jsonify({'respuesta': result}), 400
    update(request.json)
    return jsonify({"respuesta": "Reserva correctamente eliminada"})