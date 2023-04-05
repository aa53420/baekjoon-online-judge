import sys


def find_quadrant(arg_x, arg_y):
    if arg_x > 0 and arg_y > 0:
        return 1
    elif arg_x < 0 and arg_y > 0:
        return 2
    elif arg_x < 0 and arg_y < 0:
        return 3
    else:
        return 4


x = int(sys.stdin.readline().strip())
y = int(sys.stdin.readline().strip())

print(find_quadrant(arg_x=x, arg_y=y))
