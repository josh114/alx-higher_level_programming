#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
ld = int(number[-1:])
number = int(number)
if number < 0:
    print(f'Last digit of {number:d} is {-ld:d} and is less than 6 and not 0')
elif ld > 5:
    print(f'Last digit of {number:d} is {ld:d} and is greater than 5')
elif ld == 0:
    print(f'Last digit of {number:d} is {ld:d} and is 0')
else:
    print(f'Last digit of {number:d} is {ld:d} and is less than 6 and not 0')
