from marshmallow import Schema, fields, pprint

class FileOperationSchema(Schema):
    id            = fields.Int(dump_only=True)
    date_created  = fields.DateTime(dump_only=True)
    date_modified = fields.DateTime(dump_only=True)

    status = fields.Int()
    userId = fields.Int()
    path = fields.Str()
    originalName = fields.Str()
    newName = fields.Str()
    size = fields.Int()
    timestamp = fields.Int()
    command = fields.Int()
    entropy = fields.Float()
    standardDeviation = fields.Float()