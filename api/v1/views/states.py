#!/usr/bin/python3
''' states.py'''

from flask import jsonify, abort
from api.v1.views import app_views
from models import storage


@app_views.route("/states", methods=["GET"], strict_slashes=False)
def get_states():
    '''Retrieves the list of all State objects'''
    objects = storage.all("State")
    list_states = []
    for k, state_obj in objects.items():
        list_states.append(state_obj.to_dict())
    return jsonify(list_states)


@app_views.route("/states/<id>", methods=["GET"], strict_slashes=False)
def get_state_id(id):
    '''Retrieves a State object'''
    state_obj = storage.get("State", id)
    if state_obj:
        return jsonify(state_obj.to_dict())
    return abort(404)


@app_views.route("/states/<id>", methods=["DELETE"], strict_slashes=False)
def delete_state_id(id):
    '''Deletes a State object'''
    state_obj = storage.get("State", id)
    if state_obj:
        storage.delete(state_obj)
        return jsonify({}), 200
    
    return abort(400)
