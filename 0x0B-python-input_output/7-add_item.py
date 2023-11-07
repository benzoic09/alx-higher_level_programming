#!/usr/bin/python3
"""
script that adds all arguments to a Python list,
and then save them to a file
"""
import json
import sys
import os.path
from load_from_json_file import load_from_json_file
from save_to_json_file import save_to_json_file


filename = "add_item.json"
if os.path.isfile(filename):
    obj = load_from_json_file(filename)
else:
    obj = []

obj.extend(sys.argv[1:])
save_to_json_file(obj, filename)
