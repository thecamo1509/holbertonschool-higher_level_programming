#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        mid = self.id
        mx = self.x
        my = self.y
        ms = self.width
        return ("[Square] ({}) {}/{} - {}".format(mid, mx, my, ms))

    def update(self, *args, **kwargs):
        mylist = ["id", "size", "x", "y"]
        c = 0
        for i in args:
            setattr(self, mylist[c], i)
            c += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
