#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    num = 0
    
    for i in range(x):
        try:
            print("{:d}".format(my_list[i], end=" "))
            num += 1
        except IndexError:
            break
    return num
my_list = [1, 2, 3, 4, 5]
# test = safe_print_list(my_list, 3)

# print(test)