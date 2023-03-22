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

