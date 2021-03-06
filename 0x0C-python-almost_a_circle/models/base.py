#!/usr/bin/python3
""" Base Class """


import json
import turtle


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
            newlist = []
            if list_objs is not None:
                for obj in list_objs:
                    mydict = obj.to_dictionary()
                    newlist.append(mydict)
                f.write(cls.to_json_string(newlist))
            else:
                f.write(cls.to_json_string(newlist))

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
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 5)
        elif cls.__name__ == "Square":
            dummy = cls(1)
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

    @staticmethod
    def draw(list_rectangles, list_squares):
        turtle.color('#EB0045')
        ms = "Hello, this is rectangle drawing"
        font = "Courier"
        turtle.write(ms, move=False, align="center", font=(font, 30, "normal"))
        turtle.delay(200)
        turtle.up()
        turtle.goto(0, -20)
        turtle.forward(100)
        turtle.clear()
        turtle.up()
        turtle.pensize(4)
        turtle.delay(0)
        for obj in list_rectangles:
            mydict = obj.to_dictionary()
            turtle.goto(mydict["x"], mydict["y"])
            turtle.down()
            for i in range(2):
                turtle.forward(mydict["width"])
                turtle.left(90)
                turtle.forward(mydict["height"])
                turtle.left(90)
            turtle.up()
        turtle.clear()
        ms = "Now, let's take a look at the Squares"
        font = "Courier"
        turtle.goto(0, 0)
        turtle.write(ms, move=False, align="center", font=(font, 30, "normal"))
        turtle.delay(200)
        turtle.up()
        turtle.goto(0, -20)
        turtle.forward(100)
        turtle.clear()
        turtle.up()
        turtle.pensize(4)
        turtle.delay(0)
        for obj in list_squares:
            mydict = obj.to_dictionary()
            turtle.goto(mydict["x"], mydict["y"])
            turtle.down()
            for i in range(4):
                turtle.forward(mydict["size"])
                turtle.left(90)
            turtle.up()
        turtle.exitonclick()
