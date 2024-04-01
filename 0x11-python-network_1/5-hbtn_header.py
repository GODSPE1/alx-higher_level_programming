#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to
the URL and displays the value of the variable
X-Request-Id in the response header
"""

import requests
import sys

url = sys.argv[1]
rq  = requests.get(url)
print(rq.headers.get('X-Request-Id'))

if __name__ == "__main__":
    pass
