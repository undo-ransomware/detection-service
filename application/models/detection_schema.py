from marshmallow import Schema, fields, pprint
from application.models.file_operation_schema import FileOperationSchema

class DetectionSchema(Schema):
    id            = fields.Int(dump_only=True)
    dateCreated  = fields.DateTime(dump_only=True)
    dateModified = fields.DateTime(dump_only=True)
    userId = fields.Str()
    fileOperations = fields.Nested(FileOperationSchema, many=True)
