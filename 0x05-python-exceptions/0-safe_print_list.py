#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    num = 0
    
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            num += 1
        except IndexError:
            break
    return num
my_list = [2, 4, 3, 4, 5]
nb_print = safe_print_list(my_list, 9)
print("nb_print: {:d}".format(nb_print))

