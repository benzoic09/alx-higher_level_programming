#!/usr/bin/python3
def safe_print_integer(value):
     try:
        formatted_value = "{:d}".format(int(value))
        print(formatted_value)
        print()  # Add a new line
        return True
    except (ValueError, TypeError):
        return False
