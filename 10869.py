"""
두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.

두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
EX)
7 3

첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
"""
import sys

a, b = map(int, sys.stdin.readline().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
