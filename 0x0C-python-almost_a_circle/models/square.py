#!/usr/bin/python3
""" Square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size, x=0, y=0, id=None):
        """Init"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter """
        a = {"width": value}
        self.validator(a)
        self.width = value
        self.height = value

    def __str__(self):
        """ String Representation """
        mid = self.id
        mx = self.x
        my = self.y
        ms = self.width
        return ("[Square] ({}) {}/{} - {}".format(mid, mx, my, ms))

    def update(self, *args, **kwargs):
        """ Update value """
        mylist = ["id", "size", "x", "y"]
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
        ms = self.size
        newdt = {"id": mid, "size": ms, "x": mx, "y": my}
        return (newdt)
