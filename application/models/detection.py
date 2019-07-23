from application import db
from application.models.file_operation import FileOperation

class Detection(db.Model):
    """Data model for detections."""

    __tablename__ = 'detection'

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())
    
    userId = db.Column(db.String(256), index=False, unique=False, nullable=False)
    fileOperations = db.relationship('FileOperation')