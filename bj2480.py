import sys


def is_triple_match(dice1, dice2, dice3):
    return dice1 == dice2 == dice3


def find_double_match(dice_list=None):
    if dice_list is None:
        dice_list = []

    if len(dice_list) == 0:
        return -1

    for base_index in range(len(dice_list) - 1):
        next_index = base_index + 1
        base_dice = dice_list[base_index]
        for compare_index in range(len(dice_list) - next_index):
            compare_dice = dice_list[compare_index + next_index]
            if base_dice == compare_dice:
                return base_dice

    return -1


# def find_max_dice(dice_list=None):
#     if dice_list is None:
#         dice_list = []
#
#     if len(dice_list) == 0:
#         return 0
#
#     max_dice = dice_list[0]
#
#     for base_index in range(len(dice_list) - 1):
#         next_index = base_index + 1
#         compare_dice = dice_list[next_index]
#         if max_dice < compare_dice:
#             max_dice = compare_dice
#
#     return max_dice

def find_max_dice(dice_list=None):
    if dice_list is None:
        dice_list = []

    if len(dice_list) == 0:
        return 0

    return max(dice_list)


def calc_reward(dice1, dice2, dice3):
    bonus_reward = 0
    base_dice_eye = 1
    reward = 0

    # 같은 눈 2개가 있는지? 있다면 그 값은?
    double_match_dice = find_double_match([dice1, dice2, dice3])

    # 같은 눈 3개일 때
    if is_triple_match(dice1, dice2, dice3):
        bonus_reward = 10000
        reward = 1000
        base_dice_eye = dice1
    elif double_match_dice > 0:
        bonus_reward = 1000
        reward = 100
        base_dice_eye = double_match_dice
    else:
        bonus_reward = 0
        reward = 100
        base_dice_eye = find_max_dice([dice1, dice2, dice3])

    return bonus_reward + (base_dice_eye * reward)


a, b, c = map(int, sys.stdin.readline().strip().split())
print(calc_reward(dice1=a, dice2=b, dice3=c))
