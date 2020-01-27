#!/usr/bin/python3
""" Base Class """


import json


class Base:
    """ Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Init method """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ To json object """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Saving Json """
        with open("{}.json".format(cls.__name__), "w") as f:
            if list_objs is None:
                return []
            else:
                newlist = []
                for obj in list_objs:
                    mydict = obj.to_dictionary()
                    newlist.append(mydict)
                return f.write(cls.to_json_string(newlist))

    @staticmethod
    def from_json_string(json_string):
        """ From json file """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create instances """
        dummy = cls(1, 5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Loading from file """
        try:
            mylist = []
            with open("{}.json".format(cls.__name__), "r") as f:
                file = f.read()
                read = cls.from_json_string(file)
                for i in read:
                    dummy = cls.create(**i)
                    mylist.append(dummy)
                return mylist
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Saving csv """
        with open("{}.csv".format(cls.__name__), "w") as f:
            if list_objs is None:
                return []
            else:
                newlist = []
                for obj in list_objs:
                    mydict = obj.to_dictionary()
                    newlist.append(mydict)
                return f.write(cls.to_json_string(newlist))

    @classmethod
    def load_from_file_csv(cls):
        """ Loading CSV """
        try:
            mylist = []
            with open("{}.csv".format(cls.__name__), "r") as f:
                file = f.read()
                read = cls.from_json_string(file)
                for i in read:
                    dummy = cls.create(**i)
                    mylist.append(dummy)
                return mylist
        except FileNotFoundError:
            return []
