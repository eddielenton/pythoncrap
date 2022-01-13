#!/usr/bin/env python
from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from netmiko import ConnectHandler
import csv
from csv import reader

nxosv9000 = {
    'device_type': 'cisco_nxos',
    'host':   'sandbox-nxos-1.cisco.com',
    'username': 'admin',
    'password': 'Admin_1234!',
    'port' : 22,
    'secret': 'Admin_1234!',
}

# open file in read mode
with open('input_data.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Get all rows of csv from csv_reader object as list of tuples
    migration_list = list(map(tuple, csv_reader))


for data in migration_list:
    old_switch = data[1]
    old_interface = data[2]
    new_switch = data[3]
    new_interface = data[4]
    net_connect = ConnectHandler(**old_switch)
    command = "show run int " + old_interface
    get_int_config = net_connect.send_command(command)
    trimmed_config = get_int_config[202:]
    net_connect = ConnectHandler(**new_switch)
    get_int_config = net_connect.send_command(trimmed_config)