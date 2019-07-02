import json
from marshmallow import pprint
from flask import Blueprint, request
from flask import Response
from application.models.file_operation_schema import FileOperationSchema
from application.models.file_operation import db, FileOperation
from application.models.analysis_status import AnalysisStatus
from application.models.command import Command

file_operation_api = Blueprint('file_operation_api', __name__)

@file_operation_api.route("")
def findAll():
    schema = FileOperationSchema(many=True)
    file_operations = FileOperation.query.all()
    return Response(schema.dumps(file_operations), status=200, mimetype='application/json')

@file_operation_api.route("/<int:id>")
def find(id):
    file_operation = FileOperation(AnalysisStatus.PENDING.value, 1, '/', 'test.txt', '', 'txt', 'txt', 300, 1561662751, Command.WRITE.value, 7.9, 0.0004)
    return Response(json.dumps(file_operation.__dict__), status=200, mimetype='application/json')

@file_operation_api.route("", methods=['POST'])
def create():
    schema = FileOperationSchema()
    request_json = request.get_json(force=True)
    file_operation = FileOperation(id = int(request_json['id']), status = int(request_json['status']), userId = int(request_json['userId']), path = request_json['path'], originalName = request_json['originalName'], newName = request_json['newName'], size = int(request_json['size']), timestamp = int(request_json['timestamp']), command = int(request_json['command']), entropy = float(request_json['entropy']), standardDeviation = float(request_json['standardDeviation']))
    db.session.add(file_operation)
    db.session.commit()
    return Response(schema.dumps(file_operation), status=200, mimetype='application/json')

@file_operation_api.route("/<int:id>", methods=['PUT'])
def update(id):
    file_operation = FileOperation(AnalysisStatus.PENDING.value, 1, '/', 'test.txt', '', 'txt', 'txt', 300, 1561662751, Command.WRITE.value, 7.9, 0.0004)
    return Response(json.dumps(file_operation.__dict__), status=200, mimetype='application/json')

@file_operation_api.route("/<int:id>", methods=['DELETE'])
def delete(id):
    return Response('', status=200, mimetype='application/json')