import json
from flask import Blueprint
from flask import Response
from application.models.info import Info

info_api = Blueprint('info_api', __name__)

@info_api.route("")
def health():
    info = Info()
    return Response(json.dumps(info.__dict__), status=200, mimetype='application/json')