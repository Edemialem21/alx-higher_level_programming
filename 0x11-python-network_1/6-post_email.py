#!/usr/bin/python3
"""A python  script that takes in a URL and an email address"""
from sys import argv
from requests import post


if __name__ == "__main__":
    payload = {'email': argv[2]}
    result = post(argv[1], data=payload)
    print(result.text)
