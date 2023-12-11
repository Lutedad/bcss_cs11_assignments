import random
import sys, os
import time

# Function that prints animated text.
def print_animated_str(text, time_to_sleep):
    for char in str(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        
        #Sleeping
        time.sleep(time_to_sleep)

# Intro to dungeon game

#To clear the terminal
os.system('cls')

#To print animated string
print_animated_str("\nWelcome to Dungeon Game!\nWatch out...don't make the monster angry!\n", 0.05)
print_animated_str("You can move left/right/up/down and choose which item to pick up...",0.05)
print_animated_str("\nGood luck!\U0001F970",0.05)

#Sleeping
time.sleep(0.5)

#To clear the terminal
os.system('cls')


#Choose your character!
character_num = int(input("\n1.\U0001F970\n2.\U0001F618\n3.\U0001F60B\nChoose your character! (1~3): "))
if character_num == 1:
    player = '\U0001F970'
elif character_num == 2:
    player = '\U0001F618'
elif character_num == 3:
    player = '\U0001F60B'
else:
    print("You failed to select a character...\nYou'll get a defult one")
print_animated_str('.....',0.1)
#To clear the terminal
os.system('cls')

# Lists
map = ['__','__','__','__',['__','__','__','__']]

item_location = ['candy','sword','monster','gold',['candy','sword','candy','gold']]

# Values
player_current_location = random.choice([0, 1, 3, 4])  # Getting a random value from the list [0, 1, 3] which means getting a random position for the player except the monster location (2)
player_current_location_2f = random.choice([0, 1, 2, 3])  # Getting a random value for player's second-floor location

#Item in inventory
item_picked_up = "Nothing"

# Cant_Go_Further_Error_Message
message_cant_go_further = ("\n#########################\nYou cannot go any further. :(\n#########################\n")

def not_second_floor():
    if player_current_location != 4:
        return True
    else:
        return False

def pick_or_no(item):
    # To decide whether the player wants to pick up an item or not. @@@@EXCEPT MONSTER

    if (item != "monster") and (item != "Nothing"):
        pick_or_no_item = input("Do you want to pick up the item? (yes/no): ")
        if pick_or_no_item.lower() == 'yes':
            return (item, False)
        elif pick_or_no_item.lower() == "no":
            #Return True if player doesn't want to pick up an item
            return (item_picked_up, True)
        else:
            print("\nYou failed to pick up an item...\n")
            time.sleep(0.5)
            return (item_picked_up, True)
    else:
        return (item_picked_up, True)

while True:

    # Handling two chances ( first floor or second floor ) by using not_second_floor function.
    #IF PLAYER'S LOCATION IS FIRST FLOOR
    if not_second_floor():
        #To clear the terminal
        os.system('cls')

        #To set a value of an item located at current player's location
        first_floor_item = item_location[player_current_location]

        # Putting player's character into map list so that it could appear in the console.
        map[player_current_location] = player

        # To make a list without a bracket
        first_floor = '    '.join(map[0:4])
        second_floor = '    '.join(map[4])

        # Print player's location & Item in the room
        print(f'\n\n|   {first_floor}   |\n\n|   {second_floor}   |\n\nItem in this room : {first_floor_item}\n\nItem in your inventory: {item_picked_up}\n')

        # Replace current player's location with '' to clear the list.
        map[player_current_location] = '__'
        
        #Use pick_or_no function to decide whether to pick the item up or not.
        (item_picked_up,pick_up) = pick_or_no(first_floor_item)

        ##To replace an item at current player's location with "Nothing" @@ ONLY IF player picked up an item from the location. @@
        if pick_up == False:
            #To replace an item at current player's location with "Nothing"
            item_location[player_current_location] = "Nothing"

    #IF PLAYER'S LOCATION IS SECOND FLOOR
    else:
        #To clear the terminal
        os.system('cls')

        #To set a value of an item located at current player's location
        second_floor_item = item_location[4][player_current_location_2f]

        # Putting player( ^~^ ) into map list so that it could appear in the console.
        map[4][player_current_location_2f] = player

        # To make a list without a bracket
        first_floor = '    '.join(map[0:4])
        second_floor = '    '.join(map[4])

        # Print player's location & Item in the room
        print(f'\n\n|   {first_floor}   |\n\n|   {second_floor}   |\n\nItem in this room : {second_floor_item}\n\nItem in your inventory: {item_picked_up}\n')

        # Replace current player's location with '' to clear the list.
        map[4][player_current_location_2f] = '__'

        #Use pick_or_no function to decide whether to pick the item up or not.
        (item_picked_up,pick_up) = pick_or_no(second_floor_item)

        ##To replace an item at current player's location with "Nothing" @@ ONLY IF player picked up an item from the location. @@
        if pick_up == False:
            #To replace an item at current player's location with "Nothing"
            item_location[4][player_current_location_2f] = "Nothing"

        

    # To get input whether the player wants to go left or right / up or down.
    left_or_right = input("Player move (left/right/up/down): ")

    # If the answer is left, subtract 1 from player_current_location so that the location could move to the left.
    if left_or_right.lower() == 'left':
        if not_second_floor():
            
            #To see if the player can go further or not. If the player's movement makes out of range, print caution message.
            if ((player_current_location - 1) <= -1):
                #To clear the terminal
                os.system('cls')


                print(message_cant_go_further)
                
                #Sleeping
                time.sleep(0.5)
            else:
                player_current_location -= 1
        else:            

            #To see if the player can go further or not. If the player's movement makes out of range, print caution message.
            if ((player_current_location_2f - 1) <= -1):
                #To clear the terminal
                os.system('cls')


                print(message_cant_go_further)
                
                #Sleeping
                time.sleep(0.5)
            else:
                player_current_location_2f -= 1
    # If the answer is right, add 1 to player_current_location so that the location could move to the right.
    elif left_or_right.lower() == "right":
        
        if not_second_floor():

            #To see if the player can go further or not. If the player's movement makes out of range, print caution message.
            if ((player_current_location + 1) >= 4):
                #To clear the terminal
                os.system('cls')


                print(message_cant_go_further)
                
                #Sleeping
                time.sleep(0.5)
            else:
                player_current_location += 1
        else:

            #To see if the player can go further or not. If the player's movement makes out of range, print caution message.
            if ((player_current_location_2f + 1) >= 4):
                #To clear the terminal
                os.system('cls')


                print(message_cant_go_further)
                
                #Sleeping
                time.sleep(0.5)
            else:
                player_current_location_2f += 1
    # If the answer is up, check if it's the second floor or not.
    elif left_or_right.lower() == "up":
        if not_second_floor():
            #To clear the terminal
            os.system('cls')

            print(message_cant_go_further)
            
            #Sleeping
            time.sleep(0.5)
        else:
            player_current_location = player_current_location_2f
    # If the answer is down, check if it's the first floor or not.
    elif left_or_right.lower() == "down":
        if not not_second_floor():
            #To clear the terminal
            os.system('cls')

            print(message_cant_go_further)
            
            #Sleeping
            time.sleep(0.5)
        else:
            player_current_location_2f = player_current_location
            player_current_location = 4
    # If the answer is neither left nor right, it appears an error message.
    else:
        os.system('cls')
        print("####Invalid input, please try again.####")
        time.sleep(0.5)
        os.system('cls')

    # To determine if the player is being encountered the monster or not.
    if player_current_location == 2:

        #To clear the terminal
        os.system('cls')

        #Put surprised face at current player's location
        player = ("\U0001FAE2 ")
        map[player_current_location] = player

        #To print a list without bracket / Have to re-assign or player will not move
        first_floor = '    '.join(map[0:4])
        second_floor = '    '.join(map[4])

        #To print a map once again
        print(f'\n\n|   {first_floor}   |\n\n|   {second_floor}   |')

        # Get an input whether the player wants to fight or not.
        fight_or_not = input("\nYOU ENCOUNTERED A MONSTER! WATCH OUT!\nDo you want to fight against the monster? (yes/no): ")

        # An if-else method that determines to fight or move away when player encounters the monster.
        if fight_or_not.lower() == "yes":
            print_animated_str("......", 0.4)

            #To clear the terminal
            os.system('cls')

            # An if-elif-else function to get different results with different items.

            #if item is a candy do the following function
            if item_picked_up == "candy":
                print("\nThe monster loved candy!\nYou won the game!")

            #if item is a sword do the following function // However, we don't know the result of the fight! It's randomized.
            elif item_picked_up == "sword":
                # Randomizing the result of battle | 25% chance of lost!
                if random.choice([True, False, True, True]):
                    print(".\n.\n.\nYou killed the monster!\nYou won the game!")
                else:
                    print("\nYOU LOST...GAME OVER")
            
            #if item is a gold do the following function
            elif item_picked_up == "gold":
                print("\n\nOh....it wasn't the best choice....\nGAME OVER!\n")
            
            #if item is nothing do the following function
            elif item_picked_up == "Nothing":
                print("WHAT?\nGAME OVER!\n")
            sys.exit()
        # If the answer is no or something except yes, the player will try to run away, but 0.25 change of getting caught!
        else:

            # Printing animated string by using function print_animated_str
            print_animated_str(".....", 0.23)

            # Randomizing the result of escape | 25% chance of getting caught!
            if random.choice([True, False, True, True]):
                print("\n\nSuccessfully ran away...")

            # If false, player gets caught & game over.
            else:
                print("\nYOU got caught...GAME OVER")
                sys.exit()
    #Just pass if player isn't located at monsters' area.
    else:
        pass
