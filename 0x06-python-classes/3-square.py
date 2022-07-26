#!/usr/bin/python3
"""Author Joshua kenedinum"""


class Square:
    """Define private method"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
    """define public class method"""
    def area(self):
        return self.__size ** 2
