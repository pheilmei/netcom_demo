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

# Definitation of the regular expression
re_interface = r"^(?P<interface>Ethernet\d{1,3}/\d{1,3}|mgmt\d).*(?P<status>up|down)"
re_down_reason = r"^(Ethernet|mgmt).*\((?P<reason>.+)\)"

# empty list for the interface
interfaces = []

# function to parse the device output with Regular Expression
def extract_interface(text):
    global interfaces
    m = re.search(re_interface, text)
    if m:
        result = m.groupdict()
        result["reason"] = ""
        if m.group(2) == "down":
            reason_re = re.search(re_down_reason, text)
            result.update(reason_re.groupdict())
        return result    
    else: 
        pass

# Definition der Geräte in einzelnen Dictionaries
# replace the values with your enviroment
#  "device_type": <device type which netmiko should use> 
#  "host": <IP of the host>
#  "username": <username for device>
#  "password": <device password>
#  "port": <ssh port>
#  "secret" : <device secret>
device = {
        "device_type": "",
        "host": "",
        "username": "",
        "password": "",
        "port": 22,
        "secret": ""
    }

net_connect = ConnectHandler(**device)
response = net_connect.send_command("show interface")
net_connect.disconnect()

# loop to send each output line to parsing
for line in response.splitlines():
    int_status = extract_interface(line)
    if int_status:
        int_status["host"] = device["host"]
        interfaces.append(int_status)

#print(interfaces)

#save to csv file
csv_columns = ["host", "interface", "status", "reason"]
csv_file = "interfaces.csv"
with open(csv_file, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for interface in interfaces:
        writer.writerow(interface)

