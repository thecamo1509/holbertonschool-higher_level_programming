#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dictionary = {}
        if type(attrs) == list:
            for i in range(len(attrs)):
                if type(attrs[i]) == str:
                    try:
                        dictionary[attrs[i]] = getattr(self, attrs[i])
                    except AttributeError:
                        continue
            return dictionary
        else:
            return (self.__dict__)
