import sys
import math


def number_split(arg):
    number_length = len(str(arg))
    max_square_number = number_length - 1

    result_list = list()
    dividend = arg

    for square_number in list(range(max_square_number, 0, -1)):
        # 나눌 수 (10의 제곱 수)
        divisor = math.pow(10, square_number)

        # 몫
        quotient = int(dividend // divisor)
        result_list.append(quotient)

        # 나머지
        remainder = int(dividend % divisor)
        dividend = remainder

        if square_number == 1:
            result_list.append(remainder)
            return result_list


a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())

b_num_list = number_split(b)
result1 = b_num_list.pop() * a
result2 = b_num_list.pop() * a
result3 = b_num_list.pop() * a
result4 = result1 + (result2 * 10) + (result3 * 100)

print(result1)
print(result2)
print(result3)
print(result4)
