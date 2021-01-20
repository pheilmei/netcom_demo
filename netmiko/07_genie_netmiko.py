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

interfaces_list = []

# Definition der Geräte in einzelnen Dictionaries
# replace the values with your enviroment
#  "device_type": <device type which netmiko should use> 
#  "host": <IP of the host>
#  "username": <username for device>
#  "password": <device password>
#  "port": <ssh port>
#  "secret" : <device secret>
device  = {
            "device_type": "cisco_nxos",
            "host": "",
            "username": "",
            "password": "",
            "port": 22
}


net_connect = ConnectHandler(**device)


interfaces = net_connect.send_command("show interface", use_genie=True) #use use_genie=True if you want to parse the output to a YANG similar data modell
net_connect.disconnect()

for interface in interfaces:
    temp_dict = {
        "host": device['host'],
        "interface": interface,
        "status": interfaces[interface]['link_state'],
        "reason": "Administrative down" if interfaces[interface]['admin_state'] == "down" else ""
    }
    interfaces_list.append(temp_dict)


csv_columns = ["host", "interface", "status", "reason"]
csv_file = "interfaces.csv"
with open(csv_file, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for interface in interfaces_list:
        writer.writerow(interface)

