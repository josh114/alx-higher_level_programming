#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
last_digit = int(number[-1:])
number = int(number)
if number < 0:
    print(f'Last digit of {number:d} is {-last_digit:d} and is less than 6 and not 0')
elif last_digit > 5:
    print(f'Last digit of {number:d} is {last_digit:d} and is greater than 5')
elif last_digit == 0:
    print('Last digit of ' + str(number) + ' is ' + str(last_digit) + ' and is 0')
else:
    print('Last digit of '+ str(number) + ' is ' + str(last_digit) + ' and is less than 6 and not 0')
