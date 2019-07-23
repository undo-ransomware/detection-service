from marshmallow import Schema, fields, pprint
from application.models.file_operation_schema import FileOperationSchema

class DetectionSchema(Schema):
    id            = fields.Int(dump_only=True)
    date_created  = fields.DateTime(dump_only=True)
    date_modified = fields.DateTime(dump_only=True)

    status = fields.Int()
    fileOperations = fields.Nested(FileOperationSchema, many=True)