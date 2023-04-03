import sys


def convert_exam_score(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


a = int(sys.stdin.readline().strip())
print(convert_exam_score(a))