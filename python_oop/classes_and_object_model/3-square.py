#!/usr/bin/env python3
"""Defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a square with a given size."""
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
