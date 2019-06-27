from enum import Enum

class Command(int,Enum):
     DELETE = 1
     RENAME = 2
     WRITE = 3
     READ = 4
     CREATE = 5