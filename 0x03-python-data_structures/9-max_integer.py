#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) is 0:
        return None
    max_value = my_list[0]

    for num in my_list[1:]:
         if num > max_value:
             max_value = num
    return max_value
