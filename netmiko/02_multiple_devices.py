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

# Definition der Geräte in einzelnen Dictionaries
# replace the values with your enviroment
#  "device_type": <device type which netmiko should use> 
#  "host": <IP of the host>
#  "username": <username for device>
#  "password": <device password>
#  "port": <ssh port>
#  "secret" : <device secret>
device1 = {
        "device_type": "",
        "host": "",
        "username": "",
        "password": "",
        "port": 22,
        "secret": ""
    }

device2 = {
        "device_type": "",
        "host": "",
        "username": "",
        "password": "",
        "port": 22,
        "secret": ""
    }
device3 = {
        "device_type": "",
        "host": "",
        "username": "",
        "password": "",
        "port": 22,
        "secret": ""
    }

# generate a list with all device dictionary definitions

devices = [device1, device2, device3]

# iterate thru all devices
for device in devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show ip interface brief")
    net_connect.disconnect()
    print("*"*100)
    print(output)
    print("*"*100)

