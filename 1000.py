"""
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
EX)
1 2

첫째 줄에 A+B를 출력한다.
"""
import sys

def adder(num_list):
    total = 0

    for num in num_list:
        if num == '':
            num = 0

        total += int(num)

    return total


if __name__ == '__main__':
    # inputValue = input().split(' ')
    inputValue = sys.stdin.readline().split(' ')
    resultValue = adder(inputValue)

    print(resultValue)

