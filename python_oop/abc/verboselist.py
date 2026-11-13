#!/usr/bin/env python3
"""Define a list subclass that prints notifications for modifications."""


class VerboseList(list):
    """A list that announces when items are added or removed."""

    def append(self, item):
        """Add an item and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list and report the number of items added."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Print a notification before removing an item."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return an item, printing a notification."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
