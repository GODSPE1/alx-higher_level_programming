#!/bin/bash
#takes in a URL, sends a request to that URL.
curl -sL "$1" -H "X-School-User-Id: 98"
