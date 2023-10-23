#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    integers_printed = 0
    try:
        for value in my_list:
            if count >= x:
                break
            if isinstance(item, int):
                print("{:d}".format(integer_value), end=' ')
                integers_printed += 1
    except TypeError as err:
        print(err)
    else:
        return integers_printed
