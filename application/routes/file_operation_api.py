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
    schema = FileOperationSchema()
    file_operation = FileOperation.query.get(id)
    return Response(schema.dumps(file_operation), status=200, mimetype='application/json')

@file_operation_api.route("", methods=['POST'])
def create():
    schema = FileOperationSchema()
    request_json = request.get_json(force=True)
    file_operation = FileOperation(id = int(request_json['id']), status = int(request_json['status']), userId = request_json['userId'], path = request_json['path'], originalName = request_json['originalName'], newName = request_json['newName'], type = request_json['type'], mimeType = request_json['mimeType'], size = int(request_json['size']), timestamp = int(request_json['timestamp']), command = int(request_json['command']), entropy = float(request_json['entropy']), standardDeviation = float(request_json['standardDeviation']))
    db.session.add(file_operation)
    db.session.commit()
    return Response(schema.dumps(file_operation), status=200, mimetype='application/json')

@file_operation_api.route("/<int:id>", methods=['PUT'])
def update(id):
    schema = FileOperationSchema()
    request_json = request.get_json(force=True)
    file_operation = FileOperation.query.get(id)
    file_operation.status = int(request_json['status'])
    file_operation.userId = request_json['userId']
    file_operation.path = request_json['path']
    file_operation.originalName = request_json['originalName']
    file_operation.newName = request_json['newName']
    file_operation.type = request_json['type']
    file_operation.mimeType = request_json['mimeType']
    file_operation.size = int(request_json['size'])
    file_operation.timestamp = int(request_json['timestamp'])
    file_operation.command = int(request_json['command'])
    file_operation.entropy = float(request_json['entropy'])
    file_operation.standardDeviation = float(request_json['standardDeviation'])
    db.session.commit()
    return Response(schema.dumps(file_operation), status=200, mimetype='application/json')

@file_operation_api.route("/<int:id>", methods=['DELETE'])
def delete(id):
    file_operation = FileOperation.query.get(id)
    db.session.delete(file_operation)
    db.session.commit()
    return Response('', status=200, mimetype='application/json')