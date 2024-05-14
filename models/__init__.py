#!/usr/bin/python3

# Import modules and classes to make them available when the package is imported
from .base_model import BaseModel

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
