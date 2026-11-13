#!/usr/bin/env python3
"""Demonstrate mixins and multiple inheritance."""


class SwimMixin:
    """Provide swimming behavior."""

    def swim(self):
        """Print the creature's swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Provide flying behavior."""

    def fly(self):
        """Print the creature's flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represent a dragon with swimming and flying abilities."""

    def roar(self):
        """Print the dragon's roaring behavior."""
        print("The dragon roars!")
