#!/usr/bin/env python3

# Requires Python3

# imports
import requests

# import username and password
# import creds
# keygen = creds.keygen
# print (keygen)

r = requests.get('https://github.com/timeline.json')
print (r.json())
