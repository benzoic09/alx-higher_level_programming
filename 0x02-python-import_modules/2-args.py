#!/usr/bin/python3
if __name__ == "__main__":
     import sys

     num_arg = len(sys.argv) - 1

     if num_arg == 0:
            print("0 arguments.")
     elif num_arg == 1:
            print("1 argument:")
     else:
            print("{} arguments:".format(num_args))

            for i in range(1, num_arg):
                print(f"{i}: {args_list[i]}")
