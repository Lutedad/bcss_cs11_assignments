import random, sys, time

#Intro to dungeon game
print("\nWelcome to Dungeon Game!\nWatch out...don't make the monster angry!\n")

#lists
player_location = ['-','-','-','-']
item_location = ['candy','sword','monster','gold']

#Values
player = ''' ^~^ '''
player_current_location = random.randrange(0,4) # Getting value randomly in between 0 to 3
#To prevent NameError, in line 98
item_picked_up = None

#Cant_Go_Further_Error_Message
message_cant_go_further = ("\n#########################\nYou cannot go any further. :(\n#########################\n")

#function that prints animated text.
def print_animated_str (text,time_to_sleep):
    for char in str(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        #sleeping
        time.sleep(time_to_sleep)



while True:
    #Putting player( ^~^ ) into player_location list so that it could appear in console.
    player_location[player_current_location] = player

    #Print player's location & Item in the room
    print(f'{player_location}\nItem in this room : {item_location[player_current_location]}')


    #To decide whether the player wants to pick up an item or not. @@@@EXCEPT MONSTER

    if (item_location[player_current_location] != "monster") and (item_location[player_current_location] != "Nothing"):
        
        pick_or_no = input("Do you want to pick up the item? (yes/no): ")

        if pick_or_no.lower() == 'yes':
            #To set a variable with the player's item
            item_picked_up = item_location[player_current_location]
            #To get rid of item that the player picked up
            item_location[player_current_location] = 'Nothing'
        elif pick_or_no.lower() == 'no':
            pass
        else:
            print("You failed to pick up an item...\n")
    else:
        pass

    #To get an input whether the player wants to go left or right.
    left_or_right = input("Player move (left/right): ")

    #Replace current player's location with '' to clear the list.
    player_location[player_current_location] = '-'

    #If the answer is left, subtract 1 from player_current_location so that the location could move to left.
    if left_or_right.lower() == 'left':
        if ((player_current_location - 1) <= -1 ):
            print(message_cant_go_further)
            pass
        else:
            player_current_location -= 1
    #If the answer is right, add 1 to player_current_location so that the location could move to right.
    elif left_or_right.lower() == "right":
        if ((player_current_location + 1) >= 4 ):
            print(message_cant_go_further)
            pass
        else:
            player_current_location += 1
    #If the answer is neither left nor right, it appears error message.
    else:
        print("Invalid input, please try again.")

    #To determine if the player is being encountered the monster or not.
    if player_current_location == 2:
        #Get an input whether the player wants to fight or not.
        fight_or_not = input("\nYOU ENCOUNTERED A MONSTER! WATCH OUT!\nDo you want to fight against the monster? (yes/no): ")
        #A if else method that determines to fight or move away when player encounters the monster.
        if fight_or_not.lower() == "yes":
            #a if elif else function to get different results with different items.
            if item_picked_up == "candy":
                print_animated_str("\n......",0.5)
                print("\nThe monster loved candy!\nYou won the game!")
            elif item_picked_up == "sword":
                #Randomizing the result of battle | 0.25% chance of lost!
                if random.choice([True, False, True, True]):
                    print(".\n.\n.\nYou killed the monster!\nYou won the game!")
                else:
                    print("\nYOU DIED...GAME OVER")
            elif item_picked_up == "gold":
                print_animated_str("......",0.5)
                print("\nOh....it wasn't the best choice....\nGAME OVER!\n")
            elif item_picked_up == None:
                print_animated_str("......",0.5)
                print("WHAT?\nGAME OVER!\n")
            else:
                pass

            sys.exit()
        #If the answer is no...nothing happens!
        elif fight_or_not.lower() == 'no':
            pass
        else:
            print("\nLet's just run away...\n")
    else:
        pass