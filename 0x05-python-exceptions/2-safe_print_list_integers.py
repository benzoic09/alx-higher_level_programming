#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    integers_printed = 0
    try:
        for value in my_list:
            try:
                integer_value = int(value)
                print("{:d}".format(integer_value), end=' ')
                integers_printed += 1
            except ValueError:
                pass  # Ignore non-integer values
            if integers_printed >= x:
                break
    except TypeError:
    return integers_printed
