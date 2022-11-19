#!/usr/bin/python3
''' index.py '''

from flask import jsonify
from api.v1.views import app_views


@app_views.route("/status")
def index():
    return jsonify({"status": "OK"})
