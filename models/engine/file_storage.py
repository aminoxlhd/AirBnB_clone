#!/usr/bin/python3
""" FileStorage class """
import json

class FileStorage:
    """ class FileStorage """
    def _init_(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj._class.name_ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, "w") as json_file:
            json.dump(temp, json_file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as json_file:
                dict = json.load(json_file)
                for key, dict in dict.items():
                    dict_instance = models.dummy_classes[dict["__class__"]](**dict)
                    self.__objects[key] = dict_instance

        except:
            pass
