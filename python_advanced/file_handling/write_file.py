#!/usr/bin/env python3
"""Module for writing strings to text files."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file and return."""
    with open(filename, mode="w", encoding="UTF8") as file:
        return file.write(text)
