from marshmallow import Schema, fields, pprint

class FileOperationSchema(Schema):
    id            = fields.Int(dump_only=True)
    date_created  = fields.DateTime(dump_only=True)
    date_modified = fields.DateTime(dump_only=True)
    status = fields.Int(dump_only=True)

    userId = fields.Str()
    # TBD does this misbehave for 64-bit values?
    # JavaScript tends to use float for large integers, because JavaScript.
    # thus it cannot precisely represent 64-bit integers. should not be a
    # problem here though, mostly because this isn't JavaScript.
    fileid = fields.Int()
    path = fields.Str()
    name = fields.Str()
    originalName = fields.Str()
    type = fields.Str()
    mimeType = fields.Str()
    size = fields.Int()
    # TBD if there's a good way to make this ISO8601 in PHP, we should.
    timestamp = fields.Float()
    command = fields.Str()

    entropy = fields.Float()
    standardDeviation = fields.Float()
