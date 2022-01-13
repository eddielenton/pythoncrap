!/usr/bin/env python
from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from getpass import getpass
import csv

#device_list = ("")
#old_switch = ("")
#old_interface = ("")
#new_switch = ("")
#new_interface = ("")


# open file in read mode
with open('input_data.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Get all rows of csv from csv_reader object as list of tuples
    migration_list = list(map(tuple, csv_reader))

device_list = ("")
old_switch = ("")
old_interface = ("")
new_switch = ("")
new_interface = ("")


for device in device_list:
    command = device.pop("command")
    net_connect = Netmiko(**device)
    output = net_connect.send_command(command)
