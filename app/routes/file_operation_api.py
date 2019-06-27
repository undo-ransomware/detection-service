import json
from flask import Blueprint
from flask import Response
from models.file_operation import FileOperation
from models.analysis_status import AnalysisStatus
from models.command import Command

file_operation_api = Blueprint('file_operation_api', __name__)

@file_operation_api.route("")
def findAll():
    file_operation = FileOperation(AnalysisStatus.PENDING.value, 1, '/', 'test.txt', '', 'txt', 'txt', 300, 1561662751, Command.WRITE.value, 7.9, 0.0004)
    return Response(json.dumps(file_operation.__dict__), status=200, mimetype='application/json')

@file_operation_api.route("/<int:id>")
def find(id):
    file_operation = FileOperation(AnalysisStatus.PENDING.value, 1, '/', 'test.txt', '', 'txt', 'txt', 300, 1561662751, Command.WRITE.value, 7.9, 0.0004)
    return Response(json.dumps(file_operation.__dict__), status=200, mimetype='application/json')

@file_operation_api.route("", methods=['POST'])
def create():
    file_operation = FileOperation(AnalysisStatus.PENDING.value, 1, '/', 'test.txt', '', 'txt', 'txt', 300, 1561662751, Command.WRITE.value, 7.9, 0.0004)
    return Response(json.dumps(file_operation.__dict__), status=200, mimetype='application/json')

@file_operation_api.route("/<int:id>", methods=['PUT'])
def update(id):
    file_operation = FileOperation(AnalysisStatus.PENDING.value, 1, '/', 'test.txt', '', 'txt', 'txt', 300, 1561662751, Command.WRITE.value, 7.9, 0.0004)
    return Response(json.dumps(file_operation.__dict__), status=200, mimetype='application/json')

@file_operation_api.route("/<int:id>", methods=['DELETE'])
def delete(id):
    return Response('', status=200, mimetype='application/json')