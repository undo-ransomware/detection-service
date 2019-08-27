import uuid
from application import db

class FileOperation(db.Model):
    """Data model for file operations."""

    __tablename__ = 'file_operation'

    # unique ID assigned for that fileop
    # TODO BigInteger would be better, but SqlAlchemy doesn't want to treat that
    # as a primary key
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    # FIXME this is redundant with timestamp, except for precision and time source
    dateCreated = db.Column(db.DateTime,  default=db.func.current_timestamp())
    # FIXME columns should be immutable once created
    dateModified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())
    status = db.Column(db.String(9), default='pending')

    # user ID; 64 is from oc_users.uid
    userId = db.Column(db.String(64), index=True, nullable=False)
    # unique tracking ID for that file (fileid from oc_filecache)
    fileId = db.Column(db.BigInteger, nullable=False)
    # full path of file (unrestricted except on ancient Windows)
    path = db.Column(db.Text(), nullable=False)
    # name of file after operation; 250 is from oc_filecache.name
    name = db.Column(db.String(250), nullable=False)
    # name of file before operation, if the file was moved. null if the
    # filename didn't change.
    originalName = db.Column(db.String(250), nullable=True)
    # type of file, ie. "file", "folder" (and, in NextCloud, nothing else)
    type = db.Column(db.String(6), nullable=False)
    # mimetype according to file extension; 255 is from oc_mimetypes.mimetype
    mimeType = db.Column(db.String(255), nullable=False)
    # file size in bytes
    size = db.Column(db.Integer, nullable=False)
    # timestamp of file operation, should be at least 1ms precision. NextCloud
    # cannot restore version that precisely but several operations per second
    # are expected, and a good enough ransomware indicator that it makes sense
    # to track them precisely.
    # 26 is 20 digits for 2^64 plus 6 decimals for microsoeconds
    # FIXME semantically this should be DateTime, but there's no portable way
    # to specify subsecond precision for that?!
    timestamp = db.Column(db.Numeric(precision=26, scale=6, asdecimal=True),
			nullable=False)
    # operation performed on the file: "DELETE", "RENAME", "WRITE", "CREATE"
    command = db.Column(db.String(6), nullable=False)

    # file features. must be nullable so features being added can have missing
    # values for old files.
    entropy = db.Column(db.Float, nullable=True)
    standardDeviation = db.Column(db.Float, nullable=True)
