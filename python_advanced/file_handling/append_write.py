#!/usr/bin/env python3
"""Module for appending strings to text files."""


def append_file(filename="", text=""):
    """Append a string to a UTF8 text file and return characters added."""
    with open(filename, mode="a", encoding="UTF8") as file:
        return file.write(text)
