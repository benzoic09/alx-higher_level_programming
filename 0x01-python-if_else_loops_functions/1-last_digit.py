#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_d = abs(number) % 10
prefix = "Last digit of"
suffix = ""
if number < 0:
    last_d *= -1
    suffix = "and is less than 6 and not 0"
elif last_d > 5:
    suffix = "and is greater than 5"
elif last_d == 0:
    suffix = "and is 0"
    print(f"{prefix} {number} is {last_d} {suffix}")
