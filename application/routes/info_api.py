import json
from flask import Blueprint
from flask import Response
from application.models.info import Info
from application.models.info_schema import InfoSchema

info_api = Blueprint('info_api', __name__)

@info_api.route("")
def health():
    schema = InfoSchema()
    info = Info()
    return Response(schema.dumps(info), status=200, mimetype='application/json')