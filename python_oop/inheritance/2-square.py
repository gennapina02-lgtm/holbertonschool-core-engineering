#!/usr/bin/env python3
"""Defines an extended Square class."""

BaseSquare = __import__('1-square').Square


class Square(BaseSquare):
    """Represent a square."""

    def __str__(self):
        """Return the square description."""
        return "[Square] {}/{}".format(
            self._Square__size,
            self._Square__size
            )
