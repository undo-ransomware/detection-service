import json
from flask import Blueprint
from flask import Response

status_api = Blueprint('status', __name__)

@status_api.route("")
def status():
    data = {
        'status' : 'UP'
    }
    return Response(json.dumps(data), status=200, mimetype='application/json')