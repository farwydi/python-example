import random

MR = 101


def lap(player_choice):
    bot_choice = random.randint(1, MR)

    if player_choice == bot_choice:
        return 0

    # b - 2, a - 1
    # a + 1 to a + 48

    if player_choice + 1 < bot_choice < player_choice + 48:
        return 1

    return -1

    # r = (bot_choice - player_choice) % MR
    #
    # return r + MR if r < 0 else r


while True:
    you_choice = random.randint(1, MR)
    result = lap(you_choice)

    # print(result)

    if result == 0:
        print("\rНичья", end="")
    elif result == 1:
        print("\rYou win", end="")
    elif result == -1:
        print("\rBot win", end="")

    # print(f"\r {}", end='')
