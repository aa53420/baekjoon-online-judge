import sys

DAY_MINUTE = 1440


def calc_cooking_end_time(current_hour, current_minute, cooking_time):
    current_total_minute = (current_hour * 60) + current_minute
    cooking_over_time = current_total_minute + cooking_time

    if cooking_over_time >= DAY_MINUTE:
        cooking_over_time -= DAY_MINUTE

    cooking_over_hour = cooking_over_time // 60
    cooking_over_minute = cooking_over_time % 60

    return f'{cooking_over_hour} {cooking_over_minute}'


input_current_hour, input_current_minute = map(int, sys.stdin.readline().strip().split())
input_cooking_time = int(sys.stdin.readline().strip())

print(calc_cooking_end_time(current_hour=input_current_hour,
                            current_minute=input_current_minute,
                            cooking_time=input_cooking_time))
