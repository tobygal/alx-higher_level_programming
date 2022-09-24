#!/usr/bin/python3
"""a python script that takes in a URL, sends a request and returns id"""


import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    print(req.headers.get('x-request-id'))
