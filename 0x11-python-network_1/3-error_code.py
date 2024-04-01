#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError

data_request = Request(sys.argv[1])
try:
    with urlopen(data_request) as response:
        print(response.read().decode("ascii"))
except HTTPError as e:
    print('Error code: ', e.code)
