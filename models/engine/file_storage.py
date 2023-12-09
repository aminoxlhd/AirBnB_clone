#!/usr/bin/python3
""" FileStorage class """
import json
from models.base_model import BaseModel
from models.user import user
from models.state import state
from models.city import city
from models.place import place
from models.amenity import amenity
from models.review import review


class FileStorage:
    """ class FileStorage """
    def _init_(self):
        """Constructor for FileStorage."""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Return the dictionary of stored objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to the dictionary."""
        key = obj._class.name_ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serialize objects and save to the JSON file."""
        with open(self.__file_path, "w") as json_file:
            json.dump(temp, json_file)

    def reload(self):
        """Deserialize objects from the JSON file and reload into __objects."""
        try:
            with open(self.__file_path, "r", encoding="UFTF8") as json_file:
                dict = json.load(json_file)
                for key, dict in dict.items():
                    dict_instance = models.dummy_classes[dict["__class__"]](**dict)
                    self.__objects[key] = dict_instance

        except FileNotFoundError:
            pass
