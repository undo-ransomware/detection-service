import json
from marshmallow import pprint
from flask import Blueprint, request
from flask import Response
from sqlalchemy import exc
from application.models.file_operation_schema import FileOperationSchema
from application.models.file_operation import db, FileOperation
from application.models.analysis_status import AnalysisStatus
from application.models.command import Command

file_operation_api = Blueprint('file_operation_api', __name__)

@file_operation_api.route("")
def findAll(userId = None):
    schema = FileOperationSchema(exclude=['detectionId'], many=True)
    userId = request.args.get('userId', default = None)
    if userId is not None:
        file_operations = FileOperation.query.all()
    else:
        file_operations = FileOperation.query.filter_by(userId = userId)
    return Response(schema.dumps(file_operations), status=200, mimetype='application/json')


@file_operation_api.route("/<int:id>")
def find(id):
    schema = FileOperationSchema()
    file_operation = FileOperation.query.get(id)
    if file_operation is None:
        return Response(status=404, mimetype='application/json')
    else:
        return Response(schema.dumps(file_operation), status=200, mimetype='application/json')

@file_operation_api.route("", methods=['POST'])
def create():
    schema = FileOperationSchema()
    request_json = request.get_json(force=True)
    file_operation = FileOperation(id = int(request_json['id']), status = int(request_json['status']), userId = request_json['userId'], path = request_json['path'], originalName = request_json['originalName'], newName = request_json['newName'], type = request_json['type'], mimeType = request_json['mimeType'], size = int(request_json['size']), timestamp = int(request_json['timestamp']), command = int(request_json['command']), entropy = float(request_json['entropy']), standardDeviation = float(request_json['standardDeviation']))
    try:
        db.session.add(file_operation)
        db.session.commit()
        return Response(schema.dumps(file_operation), status=200, mimetype='application/json')
    except exc.IntegrityError as e:
        db.session().rollback()
        return Response(status=409, mimetype='application/json')

@file_operation_api.route("/<int:id>", methods=['DELETE'])
def delete(id):
    file_operation = FileOperation.query.get(id)
    if file_operation is None:
        return Response(status=404, mimetype='application/json')
    else:
        db.session.delete(file_operation)
        db.session.commit()
        return Response('', status=200, mimetype='application/json')