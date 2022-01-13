#!/usr/bin/env python
from __future__ import print_function, unicode_literals
from netmiko import Netmiko
import csv
from csv import reader

# open file in read mode
with open('input_data.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Get all rows of csv from csv_reader object as list of tuples
    migration_list = list(map(tuple, csv_reader))


for data in migration_list:
    old_switch = data[0]
    old_interface = data[1]
    command = data.pop("command")
    net_connect = Netmiko(**data)
    output = net_connect.send_command(command)

print(old_switch)
print(old_interface)