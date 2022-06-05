#!/usr/bin/python3

def print_list_integer(my_list=[]):
    count = len(my_list)
    for i in range(count):
        print("{}".format(my_list[i], end=""))
