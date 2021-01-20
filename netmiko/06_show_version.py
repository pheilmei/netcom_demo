#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""netcom_demo Console Script.

Copyright (c) 2021 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

__author__ = "Paul Heilmeier"
__email__ = "pheilmei@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2021 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

# library import
from netmiko import ConnectHandler
import csv
import re

# leeres dictionary
version_info = {}

# device definition
# set the path to your device CSV file
file_path = "netmiko/devices.csv"
# open the csv file and read/parse it to the dictionary devices
with open(file_path) as f:
    reader = csv.DictReader(f)
    devices = [row for row in reader]

def parse_version_general(device):
    version_regex = ".+Version.(.+)"

    net_connect = ConnectHandler(**device)
    response = net_connect.send_command("show version | inc Version")
    hostname = net_connect.send_command('show run | inc hostname')
    hostname = hostname.replace('\n','')
    net_connect.disconnect()
    
    search = re.search(version_regex, response)
    print(f"\n{device['device_type']+f' {hostname}':_^100}")
    print(response)
    print(f"{'end':_^100}")
    
    return [hostname, search.group(1)]


def parse_version_asa(device):
    version_regex = ".+Version.(.+)"

    net_connect = ConnectHandler(**device)
    response = net_connect.send_command("show version | inc Version")
    hostname = net_connect.send_command('show hostname')
    hostname = hostname.strip('/n')

    net_connect.disconnect()
    
    search = re.search(version_regex, response)
    print(f"\n{device['device_type']+f' {hostname}':_^100}")
    print(response)
    print(f"{'end':_^100}")
    
    return [hostname, search.group(1)]

def parse_version_nxos(device):
    version_regex = "+NXOS:.version.(.+)"

    net_connect = ConnectHandler(**device)
    response = net_connect.send_command("show version | inc version")
    hostname = net_connect.send_command('show hostname ').strip('/n')
    hostname = hostname.strip('/n')

    net_connect.disconnect()
    
    search = re.search(version_regex, response)
    print(f"\n{device['device_type']+f' {hostname}':_^100}")
    print(response)
    print(f"{'end':_^100}")

    return [hostname, search.group(1)]

def do_update(host):
    pass

# iterate thru all devices
for device in devices:
    ip = str(device['host'])

    if device['device_type'] == "cisco_xe":
       version_info[ip] = parse_version_general(device)
    elif device['device_type'] == "cisco_asa":
       version_info[ip] = parse_version_asa(device)
    elif device['device_type'] == "cisco_nxos":
       version_info[ip] = parse_version_nxos(device)
  
print(version_info)


