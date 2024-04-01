#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request
import sys

data = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(data) as response:
    data_response = response.getheader('X-Request-Id')
    print(data_response)

if __name__ == '__main__':
    pass
