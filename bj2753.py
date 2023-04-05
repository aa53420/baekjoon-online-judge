import sys


def is_leaf_year(target_year):
    leaf_year_condition_1 = (target_year % 4) == 0 and not (target_year % 100) == 0
    leaf_year_condition_2 = (target_year % 400) == 0

    return leaf_year_condition_1 or leaf_year_condition_2


year = int(sys.stdin.readline().strip())
print(int(is_leaf_year(target_year=year)))