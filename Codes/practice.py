import random

#Intro to dungeon game
print("\nWelcome to Dungeon Game!\nWatch out...don't make the monster angry!\n")

#lists
player_location = ['-','-','-','-']
item_location = ['candy','sword','monster','gold']
#Values
player = ''' ^~^ '''
player_current_location = random.randrange(0,4) # Getting value randomly in between 0 to 3
#Cant_Go_Further_Error_Message
message = "\n#########################\nYou cannot go any further. :(\n#########################\n"

while True:
    player_location[player_current_location] = player

    print(f'{player_location}\nItem in this room : {item_location[player_current_location]}')

    #To get an input whether the player wants to go left or right.
    left_or_right = input("Player move (left/right): ")

    #Replace current player's location with '' to clear the list.
    player_location[player_current_location] = '-'

    #If the answer is left, subtract 1 from player_current_location so that the location could move to left.
    if left_or_right.lower() == 'left':
        if ((player_current_location - 1) <= -1 ):
            print(message)
            pass
        else:
            player_current_location -= 1
    #If the answer is right, add 1 to player_current_location so that the location could move to right.
    elif left_or_right.lower() == "right":
        if ((player_current_location + 1) >= 4 ):
            print(message)
            pass
        else:
            player_current_location += 1
    #If the answer is neither left nor right, it appears error message.
    else:
        print("Invalid input, please try again.")