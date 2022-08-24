#!/usr/bin/python3
import random
number = random.randint(-1000, 10000)

if number > 0:
    id = number % 10
else:
    id = number % -10

    if id > 5:
        print("Last digit of {:d is {:d and is greater \ than 5" .format(number, id))
    elseif id < 6 and id != 0:
        print("Last digit of {:d} is {:d} and is less than 6 \ and not 0" .format(number, id))
    else:
        print("Last digit of {:d} is {:d} and is 0".format(number, ld))
