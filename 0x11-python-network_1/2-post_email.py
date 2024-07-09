#!/usr/bin/python3
"""A python script takes in a URL and an email, sends a POST
request to the passed """
from sys import argv
from urllib.request import urlopen
from urllib.parse import urlencode


if __name__ == "__main__":
    params = {'email': argv[2]}
    post_data = urlencode(params).encode('ascii')

    with urlopen(argv[1], post_data) as response:
        print(response.read().decode('utf8'))
