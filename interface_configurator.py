#!/usr/bin/env python
from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from netmiko import ConnectHandler
import csv
from csv import reader

# open csv file
with open('input_data.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    # Create a list of tuples from the rows in the csv file
    migration_list = list(map(tuple, csv_reader))

for data in migration_list:
    #populate vars from each set of tuples
    old_switch = data[1]
    old_interface = data[2]
    new_switch = data[3]
    new_interface = data[4]
    # Connection details for the old switch
    net_connect = ConnectHandler(device_type='cisco_nxos', host=old_switch, port=22, username='admin', password='Admin_1234!') 
    # Prepare config to run on the old switch
    get_config_command = "show run int " + old_interface + " | grep ^\s"
    # Send config to run on the old switch
    old_int_config = net_connect.send_command(get_config_command)
    # Connection details for the new switch
    net_connect2 = ConnectHandler(device_type='cisco_nxos', host=new_switch, port=22, username='admin', password='Admin_1234!') 
    # Prepare config to run on the old switch 
    set_config_command = "Interface " + new_interface + "\n" + old_int_config
    # Convert multiline string to list
    list = []
    for line in set_config_command.split("\n"):
        list.append(line.lstrip())
    # Send config to run on the new switch
    new_int_config = net_connect2.send_config_set(list)
    print(new_int_config)
