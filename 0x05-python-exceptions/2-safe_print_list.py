#!/usr/bin/python3
def cafe_print_list_integers(mylist=[], x=0):
    c = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            continue
        print()
        return c
