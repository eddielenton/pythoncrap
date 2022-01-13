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

x = 1

for data in migration_list:
    old_switch = data[x]
    old_interface = data[2]
    new_switch = data[3]
    new_interface = data[4]
    print(old_switch)

