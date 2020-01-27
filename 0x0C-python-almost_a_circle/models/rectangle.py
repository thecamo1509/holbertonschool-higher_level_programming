#!/usr/bin/python3
""" Rectangle """
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializing """
        mydict = {"width": width, "height": height, "x": x, "y": y}
        self.validator(mydict)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter """
        a = {"width": value}
        self.validator(a)
        self.__width = value

    @property
    def height(self):
        """ Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter """
        a = {"height": value}
        self.validator(a)
        self.__height = value

    @property
    def x(self):
        """ Getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter """
        a = {"x": value}
        self.validator(a)
        self.__x = value

    @property
    def y(self):
        """ Getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter """
        a = {"y": value}
        self.validator(a)
        self.__y = value

    def validator(self, mydict):
        """ Validator """
        for key, value in mydict.items():
            if type(value) != int:
                raise TypeError("{} must be an integer".format(key))
            elif value <= 0 and (key != "x" and key != "y"):
                raise ValueError("{}  must be > 0".format(key))
            elif value < 0 and (key != "width" and key != "height"):
                raise ValueError("{} must be >= 0".format(key))

    def area(self):
        """ Getting Rectangle area """
        return self.__width * self.__height

    def display(self):
        """ Print rectangle """
        x = " " * self.__x
        y = "\n" * self.__y
        r = "#" * self.__width
        sw = self.__width
        sh = self.__height
        print(y + (sh - 1) * (x + "#" * sw + "\n") + x + r)

    def __str__(self):
        """ Str """
        mid = self.id
        mw = self.__width
        mh = self.__height
        mx = self.__x
        my = self.__y
        msg = ("[Rectangle] ({}) {}/{} - {}/{}".format(mid, mx, my, mw, mh))
        return msg

    def update(self, *args, **kwargs):
        """ Update values """
        mylist = ["id", "width", "height", "x", "y"]
        c = 0
        for i in args:
            setattr(self, mylist[c], i)
            c += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Dictionary representation """
        mid = self.id
        mx = self.x
        my = self.y
        mw = self.width
        mh = self.height
        newdt = {"id": mid, "width": mw, "height": mh, "x": mx, "y": my}
        return (newdt)
