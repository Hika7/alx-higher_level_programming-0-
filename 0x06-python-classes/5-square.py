#!/usr/bin/python3
"""
Square Class: defines a square by : (based on 4-square.py)
"""


class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setters
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)
    def my_print(self):
        print("#")
        if (size = 0):
            print()
