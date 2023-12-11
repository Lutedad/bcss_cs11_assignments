#######################################
############PART_Extensions############
#######################################
import os
# Clear the terminal
os.system("cls")
# Simple Intro
print("Welcome to connect 3!\nYou can choose the board size.\nMake sure to stay focused!\n")
# Ask the player whether to change the setting or to use the default setting
user_input = input("Do you want to use default settings? (y/n): ")

# If the answer is yes, set the default setting
if user_input.lower() == "y":
    board_size = 4
elif user_input.lower() == "n":
    board_size = int(input("Choose your board size (4 ~ 9): "))
# If the answer is invalid, go with the default setting
else:
    input("Eh! Wrong input, starting with the default setting...\nPress Enter to continue...")
    board_size = 4

#######################################
#################PART1#################
#######################################

map_game = []

# printBoard function / To print the list in board format
def printBoard():
    os.system("cls")
    msg = ""
    print(f"{'ㅡ'*board_size*2}\n|{board_marker}  |")
    for i in range(len(map_game)):
        msg += "|"
        for j in range(len(map_game[i])):
            msg += "  "
            msg += (map_game[i][j])
        msg += "  |\n"
    print(msg)

board_marker = ""

#[for loop]
for i in range(board_size):
    map_game.append([])
    board_marker += f"  {i+1}"

# To make a list of (_) x (_) [Nested for loop]
for i in range(board_size):
    for j in range(board_size):
        map_game[i].append("_")

# Call printBoard function
printBoard()


#######################################
#################PART2#################
#######################################

import sys

# turn function / To place a marker at the lowest level row possible in the chosen column
def turn(count):
    # The purpose of this "if" statement is to check whether the board is fully filled or not.
    if count < board_size ** 2:
        while True:
            i = 0
            user_input = int(input(f"Player turn : {user_id}\nWhich column do you want to place a marker? ({board_marker}  ): "))

            if user_input <= board_size:
                j = user_input - 1
            else:
                input("Wrong input! Please try again.\nPress Enter to continue...")
                os.system("cls")
                printBoard()
                # The main purpose of the outer while loop is to use the continue method, which makes the process go back to the start of the while loop.
                # So that the user could type in the valid input once again.
                continue

            # Same as here, it checks if the column is empty or not.
            while True:
                # If there's no marker, place the user's marker.
                # And use the return method to execute turn() function. ( Which will close all while loops. )
                if map_game[len(map_game)-i-1][j] == "_":
                    map_game[len(map_game)-i-1][j] = user_id
                    count += 1
                    return
                # If the column has no space for a new marker, break the inner loop so that the process could go to the
                # start of the outer while loop. (Which will make the user choose the column once again.)
                elif i >= len(map_game):
                    input("ERROR!! You cannot place the marker in this column anymore. Please try again!!\nPress Enter to continue...")
                    os.system("cls")
                    printBoard()
                    break
                # If there is a marker, add 1 to i to move the current row.
                else:
                    i += 1
                    # Again, one of the biggest reasons why I used a while loop. If there is a marker in the column,
                    # increase i by 1 to check if there's a space. And by using the continue method, the process will go back to the
                    # start of the inner while loop, so that it can go through the checking process once more (with an updated row).
                    continue

    # If the board is fully filled (which means there is no winner) print the draw message and shut down the whole program using sys.exit()
    else:
        input("* * * DRAW!* * *\nPress Enter to exit...")
        sys.exit()

# Calling a turn function with a user identity (i.e. X, O)
# turn("O")
# Call the printBoard function
# printBoard()

#######################################
#################PART4#################
#######################################
def win_check():
    for i in range(len(map_game)):
        for j in range(len(map_game[i])):
            try:
                # HORIZONTAL WIN
                if map_game[i][j] == map_game[i][j + 1] == map_game[i][j + 2] == user_id:
                    return True
                # VERTICAL WIN
                elif map_game[i][j] == map_game[i + 1][j] == map_game[i + 2][j] == user_id:
                    return True
                # DIAGONAL WIN /
                elif map_game[i][j] == map_game[i + 1][j + 1] == map_game[i + 2][j + 2] == user_id:
                    return True
                # DIAGONAL WIN \
                elif map_game[3 - i][j] == map_game[2 - i][j + 1] == map_game[1 - i][j + 2] == user_id:
                    return True
                else:
                    pass
            except:
                pass

#######################################
#################PART3#################
#######################################
user_id = "X"
count = 0

while True:

    # We are calling the turn function right here.
    # The turn function always be executed as soon as the player placed a marker.
    turn(count)
    printBoard()
    count += 1

    if win_check():
        input(f"Player {user_id} won!\nPress Enter to exit...")
        break
    else:
        pass

    if user_id == "X":
        user_id = "O"
    else:
        user_id = "X"