#!/usr/bin/env python3

# Requires Python3

# imports
import requests
from xml.etree import ElementTree

# import username and password
import creds
keygen = creds.keygen

r = requests.get('https://pan.rollins.edu//api/?type=op&cmd=<show><system><info></info></system></show>&key=' + keygen, verify=False)
content = (r.content)
dom = ElementTree.fromstring(content)

gateway = dom.findall('result/system/default-gateway')

print (gateway)
