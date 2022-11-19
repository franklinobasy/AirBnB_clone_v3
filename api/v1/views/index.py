#!/usr/bin/python3
''' index.py '''

from flask import jsonify
from api.v1.views import app_views


@app_views.route("/status")
def index():
    """Endpoint to return status of the api"""
    return jsonify({"status": "OK"})


@app_views.route("/stats")
def stats():
    """An endpoint that retrieves the number of each objects by type"""
    pass
