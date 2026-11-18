#!/usr/bin/env python3
"""Module for reading and printing text files."""


def read_file(filename=""):
    """Read a UTF8 text file and print its contents."""
    with open(filename, encoding="UTF8") as file:
        print(file.read(), end="")
