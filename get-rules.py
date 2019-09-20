#!/usr/bin/env python3

# Requires Python3

# imports
import requests

# import username and password
import creds
keygen = creds.keygen
print (keygen)

r = requests.get('https://pan.rollins.edu//api/?type=op&cmd=<show><system><info></info></system></show>&output-format=json&key=' + keygen, verify=False)
print (r.content)
