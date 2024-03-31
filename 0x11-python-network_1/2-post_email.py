#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}

data = urllib.parse.urlencode(data)

data = data.encode('ascii')

with urllib.request.urlopen(url, data=data) as response:
    data_response = response.read().decode('utf-8')
    print(data_response)
