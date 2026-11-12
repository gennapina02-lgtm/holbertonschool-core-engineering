#!/usr/bin/env python3
"""Defines an extended Rectangle class>"""

BaseRectangle = __import__('1-rectangle').Rectangle


class Rectangle(BaseRectangle):
    """Represent a rectangle with the area and string representation."

    def area(self):
        ""Calculate and return the rectangles area."""
        return self._Rectangle__width * self._Rectangle__height

    def __str__(self):
        """Return the rectangle description."""
        return "[Rectangle] {}/{}".format(
            self._Rectangle__width,
            self._Rectangle__height
            )
