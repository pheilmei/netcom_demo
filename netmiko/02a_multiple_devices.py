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

# import der Geräte Credentials aus der CSV

# set the path to your device CSV file
file_path = "netmiko/devices.csv"
# open the csv file and read/parse it to the dictionary devices
with open(file_path) as f:
    reader = csv.DictReader(f)
    devices = [row for row in reader]


# iterate thru all the devices
# if you have need to use different commands for different <device_types> please use a if condition
for device in devices:
    net_connect = ConnectHandler(**device)
    if device['device_type'] == 'cisco_nxos':
        output = net_connect.send_command("show ip interface brief vrf all")
    elif device['device_type'] == 'cisco_asa':
        output = net_connect.send_command("show ip address")
    else:
        output = net_connect.send_command("show ip interface brief")
    print("*"*100)
    print(output)
    print("*"*100)
