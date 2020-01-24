#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        mydict = {"width": width, "height": height, "x": x, "y": y}
        self.validator(mydict)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        a = {"width": value}
        self.validator(a)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        a = {"height": value}
        self.validator(a)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        a = {"x": value}
        self.validator(a)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        a = {"y": value}
        self.validator(a)
        self.__y = value

    def validator(self, mydict):
        for key, value in mydict.items():
            if type(value) != int:
                raise TypeError("{} must be an integer".format(key))
            elif value <= 0 and (key != "x" and key != "y"):
                raise ValueError("{}  must be > 0".format(key))
            elif value < 0 and (key != "width" and key != "height"):
                raise ValueError("{} must be >= 0".format(key))

    def area(self):
        return self.__width * self.__height

    def display(self):
        x = " " * self.__x
        y = "\n" * self.__y
        r = "#" * self.__width
        sw = self.__width
        sh = self.__height
        print(y + (sh - 1) * (x + "#" * sw + "\n") + x + r)

    def __str__(self):
        mid = self.id
        mw = self.__width
        mh = self.__height
        mx = self.__x
        my = self.__y
        msg = ("[Rectangle] ({}) {}/{} - {}/{}".format(mid, mx, my, mw, mh))
        return msg

    def update(self, *args, **kwargs):
        mylist = ["id", "width", "height", "x", "y"]
        c = 0
        for i in args:
            setattr(self, mylist[c], i)
            c += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
