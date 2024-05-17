#!/usr/bin/python3

# Import modules and classes to make them available when the package is imported
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from models.base_model import BaseModel

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
