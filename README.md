# 1. netcom_demo

*Sample Network Automation Scripts*

---

This repo is a brief introduction for network automation tasks.

It contains some basic scripts for 

- netmiko
- ansible

It is not a demonstration for coding skills, it should only demonstrate how to use it on an easy way.

---

# 2. Setup your environment

*Please consider, ansible and pyats running only on Mac OS X or Unix, Linux enviroments, not on Windows. 
If you working with a Windows OS, possibly the scripts will not work. 
In this introduction it is not covered, how to run it on Windows OS.*

Prerequests: 
Install and use Python 3.4 or newer

clone this repo to your project folder



## 2.1. Virtual environment

It is a good practice to create a python virtual environment

open your terminal, go to your project folder and create a virtual environment 

`python3 -m venv venv`

activate this virtual environment

`source  venv/bin/activate`

## 2.2. Install python packages

you can use `pip install -r requirements.txt` to install the required packages.
Make sure, you activated the virtual environment, see above [Virtual Enviroment](#2.1.-virtual-environment)

## 2.3. Netmiko 

You will find some basic scripts for the netmiko usage in the directory netmiko. Befor you can use it, you need to adjust / specify the device credentials for your lab.

In some scripts you can do it inside the script, you need to adjust the python dictionary <devices>

- 01_Basic_Structure.py
- 02_multiple_devices.py
- 04_export_csv.py
- 09_genie_netmiko.pyi

In the other netmiko scripts, you will find a code which opens the file [devices.csv](netmiko/devices.csv) and parsing it to a python dictionary called "devices".

``` PYTHON 
# set the path to your device CSV file
file_path = "netmiko/devices.csv"
# open the csv file and read/parse it to the dictionary devices
with open(file_path) as f:
    reader = csv.DictReader(f)
    devices = [row for row in reader]
    
```
You need to adjust the file [devices.csv](netmiko/devices.csv). Make sure, your script can access this file

## 2.4. Ansible
You will find some basic playbooks for the ansible demo, inside the directory [Ansible](./Ansible)

To run the scripts, you need to adjust following

file: [host](./Ansible/hosts)
define the hosts in your environment


file: [group_vars/router](./Ansible/group_vars/router)
file: [group_vars/switch](./Ansible/group_vars/switch)

you need to provide the credentials to your devices

If you want to run the playbook [Ansible/04_create_vlan.yaml](./Ansible/04_create_vlan.yaml)

you need to define the variable *trunk_interface* inside your host file.
Otherwise the playbook will not work, cause the variable is not defined.


# 3. Authors & Maintainers


- Paul Heilmeier <pheilmei@cisco.com>

## 3.1. Credits

This repo is inspired by
### Netmiko 
- https://pynet.twb-tech.com/blog/automation/netmiko.html
- https://github.com/ktbyers/netmiko

### Ansible
- https://developer.cisco.com/automation-ansible/

## 3.2. License

This project is licensed to you under the terms of the [Cisco Sample
Code License](./LICENSE).
