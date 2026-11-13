#!/usr/bin/env python3
"""Define abstract shapes and demonstrate duck typing."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Represent a circle."""

    def __init__(self, radius):
        """Initialize a circle with the given radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the circle's area."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate and return the circle's circumference."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Represent a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle with its width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the rectangle's area."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the rectangle's perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of any compatible shape."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
