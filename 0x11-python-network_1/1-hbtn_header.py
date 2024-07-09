#!/usr/bin/python3
"""A pyhton script that takes in a URL, sends a request to the URL."""
from sys import argv
from urllib.request import urlopen


if __name__ == "__main__":
    with urlopen(argv[1]) as response:
        headers = response.headers
    print(dict(headers).get('X-Request-Id'))
