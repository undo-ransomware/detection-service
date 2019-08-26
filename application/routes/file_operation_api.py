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

@file_operation_api.route('')
def findAll(userId = None):
    schema = FileOperationSchema(many=True)
    userId = request.args.get('userId', default=None)
    # FIXME this needs to be tested with thousands of fileops.
    # a single non-paginated query is more efficient but no good if it crashes something.
    if userId is not None:
        file_operations = FileOperation.query.filter_by(userId=userId)
    else:
        file_operations = FileOperation.query.all()
    return Response(schema.dumps(file_operations), status=200, mimetype='application/json')

@file_operation_api.route('/<int:id>')
def find(id):
    schema = FileOperationSchema()
    file_operation = FileOperation.query.get(id)
    if file_operation is None:
        return Response(status=404, mimetype='application/json')
    return Response(schema.dumps(file_operation), status=200, mimetype='application/json')

@file_operation_api.route('', methods=['POST'])
def create():
    schema = FileOperationSchema()
    request_json = schema.load(request.get_json(force=True))
    file_operation = FileOperation(**request_json)
    try:
        db.session.add(file_operation)
        db.session.commit()
        return Response(schema.dumps(file_operation), status=200, mimetype='application/json')
    except exc.IntegrityError as e:
        db.session().rollback()
        return Response(schema.dumps({ 'exception': repr(e) }), status=409, mimetype='application/json')

@file_operation_api.route('/<int:id>', methods=['DELETE'])
def delete(id):
    file_operation = FileOperation.query.get(id)
    if file_operation is not None:
        db.session.delete(file_operation)
        db.session.commit()
    # immutable DELETE paradigm: it doesn't matter as long as it's gone afterwards...
    return Response(status=204, mimetype='application/json')
