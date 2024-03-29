#!/usr/bin/env python3

# requires Python3, requests and xmltodict

# imports
import requests
import json
import xmltodict
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# import keygen
import creds

# definitions
keygen = creds.keygen
url = 'https://pan.rollins.edu'
command = '<show><system><info></info></system></show>'

# disables SSL cert warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# send command
r = requests.get(url+ '/api/?type=op&cmd=' +command+ '&key=' +keygen, verify=False)
content =  r.content

# parses XML straigh to JSON format
dict = xmltodict.parse(content, dict_constructor=dict)

# combines headers so we can search for the data inside system
system = dict['response']['result']['system']

print (system['wildfire-release-date'])

# XML with installing another library
# from xml.etree import ElementTree
# root = ElementTree.fromstring(r.content)
#
# gateway = root[0][0][4]
# print (gateway.text)
# print (gateway.tag)
# print (gateway.attrib)
