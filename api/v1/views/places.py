#!/usr/bin/python3
''' cities.py'''

from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.city import City
from models.place import Place
from models.user import User


@app_views.route("/cities/<city_id>/places",
                 methods=["GET", "POST"],
                 strict_slashes=False)
def get_places(city_id):
    '''Retrieves the list of all Place objects of a City'''
    city_object = storage.get(City, city_id)
    if not city_object:
        abort(404)

    if request.method == "GET":
        places = [place.to_dict() for place in city_object.places]
        return jsonify(places)

    elif request.method == "POST":
        if not request.is_json:
            abort(400, description="Not a JSON")

        if "name" not in request.json:
            abort(400, description="Missing name")

        if "user_id" not in request.json:
            abort(400, description="Missing user_id")

        place_json = request.get_json()

        user = storage.get(User, place_json["user_id"])
        if not user:
            abort(404)

        place_obj = Place(user_id=place_json["user_id"],
                          city_id=city_id,
                          **place_json)
        storage.new(place_obj)
        storage.save()

        return jsonify(place_obj.to_dict()), 201


@app_views.route("/places/<place_id>",
                 methods=["GET", "DELETE", "PUT"],
                 strict_slashes=False)
def get_place_id(place_id):
    '''Retrieves a Place object'''
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    if request.method == "GET":
        return jsonify(place.to_dict())

    elif request.method == "DELETE":
        storage.delete(place)
        storage.save()
        return jsonify({}), 200

    elif request.method == "PUT":
        if not request.is_json:
            abort(400, description="Not a JSON")

        place_json = request.get_json()
        not_needed = ["id", "created_at", "updated_at", "user_id", "city_id"]
        for attr, attr_value in place_json.items():
            if attr not in not_needed:
                setattr(place, attr, attr_value)
        place.save()
        return jsonify(place.to_dict()), 200
