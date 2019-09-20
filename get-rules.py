#!/usr/bin/env python3

# Requires Python3

# imports
import requests
from xml.etree import ElementTree
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# import username and password
import creds
keygen = creds.keygen

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

r = requests.get('https://pan.rollins.edu//api/?type=op&cmd=<show><system><info></info></system></show>&key=' + keygen, verify=False)

root = ElementTree.fromstring(r.content)

gateway = root[0][0][4]
print (gateway.text)
print (gateway.tag)
print (gateway.attrib)
