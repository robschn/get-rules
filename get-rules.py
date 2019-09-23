#!/usr/bin/env python3

# Requires Python3, requests and xmltodict

# imports
import requests
import json
import xmltodict
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# import username and password
import creds
keygen = creds.keygen

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

r = requests.get('https://pan.rollins.edu//api/?type=op&cmd=<show><system><info></info></system></show>&key=' + keygen, verify=False)
content =  r.content

dict = xmltodict.parse(content, dict_constructor=dict)

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
