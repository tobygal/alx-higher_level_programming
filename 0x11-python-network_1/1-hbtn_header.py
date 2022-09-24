#!/usr/bin/python3
"""displays the header value found in a url"""


import sys
from urllib import request
if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        print(response.info()['X-Request-Id'])
