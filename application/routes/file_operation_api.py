import json
from flask import Blueprint
from flask import Response
from application.models.file_operation import db, FileOperation
from application.models.analysis_status import AnalysisStatus
from application.models.command import Command

file_operation_api = Blueprint('file_operation_api', __name__)

@file_operation_api.route("")
def findAll():
    file_operations = FileOperation.query.all()
    return Response(json.dumps(FileOperation.serialize_list(file_operations)), status=200, mimetype='application/json')

@file_operation_api.route("/<int:id>")
def find(id):
    file_operation = FileOperation(AnalysisStatus.PENDING.value, 1, '/', 'test.txt', '', 'txt', 'txt', 300, 1561662751, Command.WRITE.value, 7.9, 0.0004)
    return Response(json.dumps(file_operation.__dict__), status=200, mimetype='application/json')

@file_operation_api.route("", methods=['POST'])
def create():
    file_operation = FileOperation(status = AnalysisStatus.PENDING.value, userId = 1, path = '/', originalName = 'test.txt', newName = '', size = 300, timestamp = 1561662751, command = Command.WRITE.value, entropy = 7.9, standardDeviation = 0.0004)
    db.session.add(file_operation)
    db.session.commit()
    return Response(json.dumps(file_operation.serialize()), status=200, mimetype='application/json')

@file_operation_api.route("/<int:id>", methods=['PUT'])
def update(id):
    file_operation = FileOperation(AnalysisStatus.PENDING.value, 1, '/', 'test.txt', '', 'txt', 'txt', 300, 1561662751, Command.WRITE.value, 7.9, 0.0004)
    return Response(json.dumps(file_operation.__dict__), status=200, mimetype='application/json')

@file_operation_api.route("/<int:id>", methods=['DELETE'])
def delete(id):
    return Response('', status=200, mimetype='application/json')