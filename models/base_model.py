#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models
""" BaseModel class"""


class BaseModel:
    """ defines all common attributes/methods for other classes """

    def __init__(self, **wkargs):
        df = '%Y-%m-%dT%H:%M:%S.%f'
        if wkargs:
            dict = wkargs.copy()
            dict['created_at'] = datetime.strptime(dict['created_at'], df)
            dict['updated_at'] = datetime.strptime(dict['updated_at'], df)
            self._dict_ = dict
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dict = self.__dict__.copy()
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        dict['__class__'] = self.__class__.__name__
        return dict
