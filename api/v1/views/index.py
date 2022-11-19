#!/usr/bin/python3
''' index.py '''

from flask import jsonify
from api.v1.views import app_views
from models import storage

classes = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}


@app_views.route("/status")
def index():
    """Endpoint to return status of the api"""
    return jsonify({"status": "OK"})


@app_views.route("/stats")
def stats():
    """An endpoint that retrieves the number of each objects by type"""
    stats = {}
    for name, cls in classes.items():
        stats[name] = storage.count(cls)

    return jsonify(stats)
