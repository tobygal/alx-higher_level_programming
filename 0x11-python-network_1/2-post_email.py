#!/usr/bin/python3
"""this script takes two params and passes it as a post"""


import sys
from urllib import request, parse

if __name__ == "__main__":
    params = {'email': sys.argv[2]}
    data = parse.urlencode(params)
    data = data.encode('utf-8')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
