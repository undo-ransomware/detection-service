from marshmallow import Schema, fields, pprint

class InfoSchema(Schema):
    status = fields.Str()