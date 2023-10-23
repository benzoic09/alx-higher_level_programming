#!/usr/bin/python3
def safe_print_integer(value):
    try:
    interger_value = int(value)
    print("{:d}".format(interger_value))
    except:
        return False
    else:

        return True
