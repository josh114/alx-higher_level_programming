#!/usr/bin/python3
"""Author Joshua kenedinum"""


class Square:
    """define private attribute"""
    def __init__(self, size=0):
        self.size = size
    """define property getter"""
    @property
    def size(self):
        return self.__size
    """use decorators to define setter"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
    """define public attribute"""
    def area(self):
        return self.__size * self.__size
    