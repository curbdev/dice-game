from random import randint
import random

print("                         ")
print("╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗")
print("║║║╠─║─║─║║║║║╠─")
print("╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝")
print("                         ")

first_player = str(input("Hello first player, enter your name: "))
second_player = str(input("Hello second player, enter your name: "))
first_player_value = 0
second_player_value = 0
first_player_score = 0
second_player_score = 0
rounds_to_play = int(input("How many games you want to play?: "))

for round in range(rounds_to_play):

    first_player_value = randint(0, 6)
    second_player_value = randint(0, 6)

    print("The die rolled ", first_player_value, " for ", first_player)
    print("The die rolled ", second_player_value, " for ", second_player)

    if first_player_value > second_player_value:
        print(first_player, " won the round!")
        first_player_score = first_player_score + 1
    elif second_player_value > first_player_value:
        second_player_score = second_player_score + 1
        print(second_player, " won the round!")
    else:
        print("It's a draw")

    print("  ")
    print(input("Press any button to continue."))

print(first_player, ",", " your score is ", first_player_score)
print(second_player, ",", " your score is ", second_player_score)
if first_player_score > second_player_score:
    print("    ")
    print("So ", first_player, " is the winner!")
elif second_player_score > first_player_score:
    print("   ")
    print("So ", second_player, " is the winner!")
else:
    print("GG, that was a draw!")

print("   ")
print("Game created by Laurix:\n- GitHub: @laurixDev")
print(input("button any button to exit."))
