class FileOperation(object):
    def __init__(self, status, userId, path, originalName, newName, type, mimeType, size, timestamp, command, entropy, standardDeviation):
        self.status = status
        self.userId = userId
        self.path = path
        self.originalName = originalName
        self.newName = newName
        self.size = size
        self.timestamp = timestamp
        self.command = command
        self.entropy = entropy
        self.standardDeviation = standardDeviation
        