#!/usr/bin/python3
""" instantiates the storage system """


from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
