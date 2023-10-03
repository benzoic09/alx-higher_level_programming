#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 97 <= ord(char) <= 122:
            c = chr(ord(c) - 32)
             print("{}".format(c), end="")
             print("")
