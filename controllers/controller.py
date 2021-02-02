from flask import request, jsonify
from app import app, db
from models.model import Spaces, SpaceSchema
from models.use_cases.validation_handler import handler_validations


@app.route('/api/reservation', methods=['GET'])
def get_spaces():
    """
    Endpoint to list all the spaces

    Returns:
        [list]: [list of spaces]
    """
    all_spaces = Spaces.query.all()
    result = SpaceSchema(many=True).dump(all_spaces)
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
    if e == 400:
      return jsonify({'respuesta': result}), 400
    new_reservation = Spaces(result[0], result[1], result[2], result[3], result[4])
    db.session.add(new_reservation)
    db.session.commit()
    return jsonify({'respuesta': "Reserva correctamente agregada"})

@app.route('/api/reservation', methods=['delete'])
def delete_space():
    """
    Endpoint to delete a reservation

    Returns:
        [list]: [list of spaces]
    """
    space_id = request.json['space_id']
    space = Spaces.query.get(space_id)
    db.session.delete(space)
    db.session.commit()
    return jsonify({"respuesta": "Reserva correctamente eliminada"})