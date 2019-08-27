from application import db
from application.models.file_operation import FileOperation

det_fileop_table = db.Table('detection_file_operations', db.Model.metadata,
	db.Column('detectionId', db.Integer, db.ForeignKey('detection.id'), index=True),
	db.Column('fileOperationId', db.String(36), db.ForeignKey('file_operation.id'), unique=True))

class Detection(db.Model):
    """Data model for detections."""

    __tablename__ = 'detection'

    id = db.Column(db.Integer, primary_key=True)
    dateCreated = db.Column(db.DateTime,  default=db.func.current_timestamp())
    dateModified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())
    userId = db.Column(db.String(256), index=True, nullable=False)
    fileOperations = db.relationship('FileOperation', secondary=det_fileop_table)
