#!/usr/bin/python3
def cafe_print_list(my_list[], x=0):
    c = 0
    for i in range(x):
        try:
            print(mylist[i], end="")
            c += 1
        except IndexError:
            break
        print()
        return c`
