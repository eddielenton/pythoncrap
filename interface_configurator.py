#!/usr/bin/env python
from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from netmiko import ConnectHandler
import csv
from csv import reader

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
    net_connect = ConnectHandler(device_type='cisco_nxos', host='sandbox-nxos-1.cisco.com', port=22, username='admin', password='Admin_1234!') 
    get_config_command = "show run int " + old_interface + " | grep ^\s"
    old_int_config = net_connect.send_command(get_config_command)
    net_connect2 = ConnectHandler(device_type='cisco_nxos', host='sandbox-nxos-1.cisco.com', port=22, username='admin', password='Admin_1234!') 
    set_config_command = "Interface " + new_interface + "\n" + old_int_config
    list = []
    for line in set_config_command.split("\n"):
        list.append(line.lstrip())
    new_int_config = net_connect2.send_config_set(list)
    print(new_int_config)
