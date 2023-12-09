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
<<<<<<< HEAD
    def _init_(self):
        """Constructor for FileStorage."""
=======
    def __init__(self):
>>>>>>> a09e8153b8e7a4ea1fbab4c9d881c9736fc844b2
        self.__file_path = "file.json"
        self.__objects = {}


    def all(self):
        """Return the dictionary of stored objects."""
        return self.__objects


    def new(self, obj):
<<<<<<< HEAD
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
=======
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj.to_dict()


    def save(self):
        list_objects = {}
        for key, value in self.__objects.items():
            list_objects[key] = value
        with open(self.__file_path, 'w') as file:
            json.dump(list_objects, file)

    def reload(self):
        with open(self.__file_path, 'r') as file:
            objects_json = json.loads(file.read())
            for obj in objects_json.values():
                self.__objects[f"{obj['__class__']}.{obj['id']}"] = obj


    def destroy(self, obj):
        obj_key = f"{obj['__class__']}.{obj['id']}"
        del self.__objects[obj_key]

    def update(self, obj, attribute_key, attribute_value):
        obj_key = f"{obj['__class__']}.{obj['id']}"
        obj[attribute_key] = attribute_value
        self.__objects[obj_key] = obj

>>>>>>> a09e8153b8e7a4ea1fbab4c9d881c9736fc844b2
