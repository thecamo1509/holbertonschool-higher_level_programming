#!/usr/bin/python3
import json
import csv


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
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
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1, 5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
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
        with open("{}.csv".format(cls.__name__), "w") as f:
            file = csv.writer(f)
            for i in list_objs:
                file.writerow(i)
            return file

    @classmethod
    def load_from_file_csv(cls):
        mylist = []
        with open("{}.csv".format(cls.__name__), "r") as f:
            file = csv.reader(f)
            for i in file:
                mylist.append(i)
            return mylist
