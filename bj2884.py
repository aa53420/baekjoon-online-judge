import sys

DAY_MINUTE = 1440


def calc_alarm_time(hour, minute):

    wakeUpTimeMinute = (hour * 60) + minute
    alarmTimeMinute = wakeUpTimeMinute - 45

    if alarmTimeMinute < 0:
        alarmTimeMinute = DAY_MINUTE - abs(alarmTimeMinute)

    alarmHour = alarmTimeMinute // 60
    alarmMinute = alarmTimeMinute % 60

    return f'{alarmHour} {alarmMinute}'


h, m = map(int, sys.stdin.readline().split())
print(calc_alarm_time(h, m))


