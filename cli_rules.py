#!/usr/bin/env python3

# requires Python3

# imports
from netmiko import Netmiko

# import credentials
import creds

# definitions
username = creds.username
password = creds.password
host = creds.host

# connect to FW
myDevice = {
'host': host,
'username': username,
'password': password,
'device_type': 'paloalto_panos'
}
net_connect = Netmiko(**myDevice)
net_connect.enable()

show_run = net_connect.send_command("show config running")

# write config to txt
f = open('config.txt', 'w')
f.write(show_run)
f.close

# load in variables address, address_group and rulebase

# iterate over rulebase

    # iterate over address and address_group

        # if rulebase['source'] is equal to address or address_group skip

        # else write to file
