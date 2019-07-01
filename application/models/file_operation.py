from application import db
from serializer import Serializer

class FileOperation(db.Model, Serializer):
    """Data model for file operations."""

    __tablename__ = 'file_operation'

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())
    status = db.Column(db.Integer, index=False, unique=False, nullable=False)
    userId = db.Column(db.Integer, index=False, unique=False, nullable=False)
    path = db.Column(db.String(256), index=False, unique=False, nullable=False)
    originalName = db.Column(db.String(256), index=False, unique=False, nullable=False)
    newName = db.Column(db.String(256), index=False, unique=False, nullable=False)
    size = db.Column(db.Integer, index=False, unique=False, nullable=False)
    timestamp = db.Column(db.Integer, index=False, unique=False, nullable=False)
    command = db.Column(db.Integer, index=False, unique=False, nullable=False)
    entropy = db.Column(db.Float, index=False, unique=False, nullable=False)
    standardDeviation = db.Column(db.Float, index=False, unique=False, nullable=False)

    def serialize(self):
        return Serializer.serialize(self)
        