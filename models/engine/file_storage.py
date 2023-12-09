#!/usr/bin/python3
""" FileStorage class """

import json


class FileStorage:
    """ class FileStorage """
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}


    def all(self):
        return self.__objects


    def new(self, obj):
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

