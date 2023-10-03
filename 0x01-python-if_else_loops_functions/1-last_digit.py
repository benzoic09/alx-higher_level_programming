#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_d = abs(number) % 10
prefix = "Last digit of"
if last_d > 5:
    result = "and is greater than 5"
elif last_d == 0:
    result = "and is 0"
else:
result = "and is less than 6 and not 0"
print(f"{prefix} {number} is {last_d} {result}")
