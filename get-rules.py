#!/usr/bin/env python3

# Requires Python3

# imports
import requests
from xml.etree import ElementTree

# import username and password
import creds
keygen = creds.keygen

r = requests.get('https://pan.rollins.edu//api/?type=op&cmd=<show><system><info></info></system></show>&key=' + keygen, verify=False)

root = ElementTree.fromstring(r.content)

print (root[0][0][1].text)
print (root[0][0][1].tag)
