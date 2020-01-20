#!/usr/bin/python3
BaseGeometry = __import__('7-base_geomety').BaseGeometry


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
