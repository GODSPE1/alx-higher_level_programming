#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

data = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(data) as response:
    data_response = response.read()
    print("Body response:")
    print("\t- type:", type(data_response))
    print("\t- content:", repr(data_response))
    print("\t- utf8 content:", data_response.decode())

if __name__ == '__main__':
    pass
