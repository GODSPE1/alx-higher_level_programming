#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    data = response.read()
    print("Body response.")
    print("\t- type:", type(data))
    print("\t- content:", repr(data))
    print("\t- utf8 content:", data.decode())

if __name__ == '__main__':
    pass
