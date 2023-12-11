import time
import random
import os
import sys

# Function that prints animated text.
def print_animated_str(text, time_to_sleep):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(time_to_sleep)

# Intro to Monty Hall game
os.system('cls')
print_animated_str("Welcome to Monty Hall Game!\nYou will have to choose one door.\nTwo have a goat behind...Only one has a fancy car.", 0.05)
os.system('cls')
print("\n\n#####\nGood luck!\n#####")
time.sleep(0.5)
os.system('cls')

# Print doors
print("   🚪   🚪   🚪   \n    1    2    3")

door_num = int(input("\n\nWhich door would you like to open? (1, 2, 3): "))
time.sleep(0.5)
os.system('cls')

behind_door = ['goat', 'goat', 'car']

random.shuffle(behind_door)
door_num_1_behind, door_num_2_behind, door_num_3_behind = behind_door
# Now you have the results behind all three doors

if door_num == 1 :
    if door_num_2_behind == 'goat':
        print_animated_str("Before you finalize your choice. I will tell you a hint...\nBehind door 2 is actually a goat!",0.05)
    elif door_num_3_behind == 'goat':
        print_animated_str("Before you finalize your choice. I will tell you a hint...\nBehind door 3 is actually a goat!",0.05)
elif door_num == 2 :
    if door_num_1_behind == 'goat':
        print_animated_str("Before you finalize your choice. I will tell you a hint...\nBehind door 1 is actually a goat!",0.05)
    elif door_num_3_behind == 'goat':
        print_animated_str("Before you finalize your choice. I will tell you a hint...\nBehind door 3 is actually a goat!",0.05)
elif door_num == 3 :
    if door_num_2_behind == 'goat':
        print_animated_str("Before you finalize your choice. I will tell you a hint...\nBehind door 2 is actually a goat!",0.05)
    elif door_num_1_behind == 'goat':
        print_animated_str("Before you finalize your choice. I will tell you a hint...\nBehind door 1 is actually a goat!",0.05)
else:
    print("INVALID INPUT PLEASE TRY AGAIN")
    sys.exit()

change_or_not = input("\nWould you like to change your answer? (y/n): ")
if change_or_not.lower() == 'y':
    os.system('cls')
    if door_num == 1 and door_num_2_behind == 'goat':
        print(f"Actually, behind door 3 is a {door_num_3_behind}!")
    if door_num == 1 and door_num_3_behind == 'goat':
        print(f"Actually, behind door 2 is a {door_num_3_behind}!")
    if door_num == 2 and door_num_3_behind == 'goat':
        print(f"Actually, behind door 1 is a {door_num_3_behind}!")
    if door_num == 2 and door_num_1_behind == 'goat':
        print(f"Actually, behind door 3 is a {door_num_3_behind}!")
    if door_num == 3 and door_num_1_behind == 'goat':
        print(f"Actually, behind door 2 is a {door_num_3_behind}!")
    if door_num == 3 and door_num_2_behind == 'goat':
        print(f"Actually, behind door 1 is a {door_num_3_behind}!")
elif change_or_not.lower() == 'n':
    if door_num == 1 and door_num_1_behind == 'goat':
        print("Congratulation! You got the car")
    elif door_num == 2 and door_num_2_behind == 'goat':
        print("Congratulation! You got the car")
    elif door_num == 3 and door_num_3_behind == 'goat':
        print("Congratulation! You got the car")
    else:
        print("Ah...you got the goat")