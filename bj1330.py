import sys


def compare_ab(arg_a, arg_b):
    difference = arg_a - arg_b

    if difference == 0:
        print("==")
    elif difference > 0:
        print(">")
    else:
        print("<")


a, b = map(int, sys.stdin.readline().strip().split())
compare_ab(a, b)
