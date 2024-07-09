#!/usr/bin/python3
"""A python script takes in a URL, sends a request to the URL"""
from requests import get
from sys import argv


if __name__ == "__main__":
    print(get(argv[1]).headers.get('X-Request-Id'))
