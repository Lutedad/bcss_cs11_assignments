import random
import os
import time
######################################INITIALIZING VARIABLES/VALUES BRIEF INTRO TO GAME########################################################
# Clear terminal
os.system("cls")

# Intro to road trip simulation
print("----------------------------\nWelcome to a cross-country Canada game\nYou will travel from Burnaby to Toronto, which is approximately 4364km")
print("You will have to consider your health & food gauge!\nEnjoy your trip!\n----------------------------")
# Press Enter to process
input("\nPress Enter to start...")

# Distance we are traveling
left_distance = 4364
# Counting days
day_x = 1
# Randomly assign food amount to start
food_amount = random.randint(4, 10)
# Randomly assign health point to start
health_point = random.randint(4, 10)
# List contains what incidents will happen during a day
# 20% chance of getting bad incidents.
event = ["Illness", "Bad_Weather", "Nothing", "Nothing", "Nothing", "Nothing", "Nothing", "Nothing", "Nothing", "Nothing"]
# Guages that visualizing the status.
car = "_" * 0 +"\U0001F3CE" + "_" * 50 + "\U0001F6A9"
car_underscore = 50
# Conversion factor for car's progress
conver_fact = 50/4364
# Initialize variables to prevent errors
moved = 0
died = False
choose_stat = False
total_moved_distance = 0
location = ""
################################################################################################################################################


#######################################################CLASS FUNCTIONS###########################################################################
class functions():

    #Initializing variables using self method.
    def __init__(self, weather, choose_stat, sick, left_distance, food_amount, health_point, day_x, moved_distance, gained_health, bought_food, location):
        self.weather = weather
        self.choose_stat = choose_stat
        self.sick = sick
        self.left_distance = left_distance
        self.food_amount = food_amount
        self.health_point = health_point
        self.day_x = day_x
        self.moved_distance = moved_distance
        self.gained_health = gained_health
        self.bought_food = bought_food
        self.location = location
        
    # Name: car_move
    # Purpose: It moves the car emoji depends on how far it moved.
    # Input: self,car_underscore,moved
    # Output: car, moved
    def car_move(self,car_underscore,moved):
        moved += int(self.moved_distance * conver_fact)
        car_underscore -= moved
        car = "_" * moved +"\U0001F3CE" + "_" * car_underscore + "\U0001F6A9"
        return car, moved

    # Name: help
    # Purpose: To show extra information
    # Input: Null
    # Output: NUll
    def help():
        os.system("cls")
        print("Buy food (A) : From 3kg to 5kg, randomly buy foods.\nRest (B) : From 3 to 5, randomly get health points.\nMove (C) : From 300km to 400km randomly move. If it's raining, the range decrease to 100km~200km\nShow Stats (D) : It shows your current status.\nQuit Game (E) : It will immediately shut your game down.\nHelp (F) : Get extra instructions.\nActivate Cheat (G) : Activate the cheat immediately. You can add food/health point or just win the game\n")
        # Press Enter to process
        input("\n\nPress Enter to Continue: ")

    # Name: travel
    # Purpose: To calculate left_distance and moved_distance randomly. Also, counts the days.
    # Input: self
    # Output: left_distance, day_x, moved_distance
    def travel(self):
        # If weather is not in bad contidion, player could move 300~400km per day.
        if not(weather):
            # Randomly assign numbers between 300~400
            self.moved_distance = random.randint(300, 400)
        # Else, player could only move 100~200km per day due to heavy rain.
        else:
            # Randomly assign numbers between 100~200
            self.moved_distance = random.randint(100, 200)
        if self.left_distance - self.moved_distance > 0:
            # Calculate left distance by subtracting the moved_distance from left distance.
            self.left_distance -= self.moved_distance
        else:
            # Re-assign the moved_distance with left_distance and make left_distance zero.
            self.moved_distance = self.left_distance
            self.left_distance = 0
            
        left_distance = self.left_distance
        moved_distance = self.moved_distance

        return left_distance, moved_distance

    # Name: buy_food
    # Purpose: To purchase between 3-5 kg food per action
    # Input: self
    # Output: bought_food, food_amount
    def buy_food(self):
        self.bought_food = random.randint(3, 5)
        self.food_amount += self.bought_food

        bought_food = self.bought_food
        food_amount = self.food_amount

        return bought_food, food_amount

    # Name: rest
    # Purpose: To restore between 3-5 health points per action
    # Input: self
    # Output: health_point, gained_health
    def rest(self):
        self.gained_health = random.randint(3, 5)
        self.health_point += self.gained_health

        health_point = self.health_point
        gained_health = self.gained_health

        return health_point, gained_health

    # Name: day_passed
    # Purpose: To use 1 kg of food and 1 health point per each day
    # Input: self
    # Output: health_point, food_amount
    def day_passed(self):
        self.health_point -= 1
        self.food_amount -= 1

        health_point = self.health_point
        food_amount = self.food_amount

        return health_point, food_amount

    # Name: start
    # Purpose: To print left distance, current food and health points
    # Input: self
    # Output: None
    def start(self):
        # Clear the terminal
        os.system('cls')
        print(f"Day_{self.day_x}\n\nBought Food: {self.bought_food}kg\nGained health point: {self.gained_health}\nYou traveled {self.moved_distance}km")
        # Press Enter to process
        input("\n\nPress Enter to continue...")

    # Name: showStat
    # Purpose: To show stats
    # Input: self
    # Output: None
    def showStat(self):
        os.system("cls")
        print(f"Day_{self.day_x}\n\nLeft distance: {self.left_distance}km\nHealth Points: {self.health_point}\nRemaining Foods: {self.food_amount}\nIncident: {self.incident}")
        # Press Enter to process
        input("\n\nPress Enter to continue...")

    # Name: event
    # Purpose: Choose what incident/event to happen
    # Input: self
    # Output: weather, sick
    def event(self):
        # Randomly choose what the incident is.
        self.incident = random.choice(event)
        # If the incident is bad weather or illness, the player must rest or decrease the traveled distance.
        if self.incident == "Nothing":
            pass
        elif self.incident == "Bad_Weather":
            print("##############\nHeavy rain pouring down\n##############")
            time.sleep(1.3)
            self.weather = True
        elif self.incident == "Illness":
            print("##############\nYou caught a cold..must rest...\n##############")
            time.sleep(1.3)
            self.sick = True
        
        weather = self.weather
        sick = self.sick
        return weather, sick
   
    # Name: location_stat
    # Purpose: Determine which city the player passed
    # Input: self
    # Output: location
    def location_stat(self):
        if total_moved_distance < 220:
            self.location = "Burnaby"
        elif total_moved_distance >= 220 and total_moved_distance < 660:
            self.location = "Seattle"
        elif total_moved_distance >= 661 and total_moved_distance < 1320:
            self.location = "Spokane"
        elif total_moved_distance >= 1320 and total_moved_distance < 2939:
            self.location = "Bozeman"
        elif total_moved_distance >= 2939 and total_moved_distance < 3550:
            self.location = "Minneapolis"
        elif total_moved_distance >= 3550:
            self.location = "Chicago"
        
        location = self.location
        return location
################################################################################################################################################

################################################ While there's distance left to travel...#######################################################
while left_distance > 0:

    # Clear the terminal
    os.system('cls')

    # Initialize variables to prevent errors & reset values.
    moved_distance = 0
    gained_health = 0
    bought_food = 0
    weather = False
    sick = False 
    # Guages that visualizing the status.
    food_guage = "\U0001F355" * food_amount
    health_guage = "\U0001F90E" * health_point
    

    # If either health point or food amount is zero or lower, it's game over.
    if health_point <= 0 or food_amount <= 0:
        # Print a message to inform the user that it's game over.
        print(f"Day_{day_x}\n\nEH! You Died. GAMEOVER")
        input("Press Enter to continue: ")
        died = True
        # break the loop
        break
    else:
        
        # If the player chose (D) Show Stats or anything else that needs no-change, skip the creating an instance of the functions class
        # & initializing weather, Illness, location to remain the same status.
        if choose_stat:
            # Change choose_stat to "False"
            choose_stat = False
        else:
            # Create an instance of the functions class for the current day
            globals()[f"day_{day_x}"] = functions(weather, choose_stat, sick, left_distance, food_amount, health_point, day_x, moved_distance, gained_health, bought_food, location)
            # Initializing weather & sick from event() function as the day starts.
            (weather, sick) = globals()[f"day_{day_x}"].event()
            # Initializing location from location_stat() function as the day starts.
            location = globals()[f"day_{day_x}"].location_stat()



        # If the player is sick, they must rest.
        if sick:
            (health_point, gained_health) = globals()[f"day_{day_x}"].rest()
        else:
            print(f'''Day_{day_x}\n\nBuy food (A)\t{food_guage}\nRest (B)\t{health_guage}\nMove (C)\t{car}\nShow Stats (D)\nQuit Game (E)\nHelp (F)\nActivate Cheat (G)\n###############\nYou've passed {location}''')
            # Get user's input
            choice = input("###############\nWhat do you want to do?: ")
            os.system("cls")
            # Works same as if elif else.
            match choice.lower():
                case "a":
                    (bought_food, food_amount) = globals()[f"day_{day_x}"].buy_food()
                case "b":
                    (health_point, gained_health) = globals()[f"day_{day_x}"].rest()
                case "c":
                    (left_distance, moved_distance) = globals()[f"day_{day_x}"].travel()
                    # Update the guages.
                    (car, moved) = globals()[f"day_{day_x}"].car_move(car_underscore,moved)
                    # Update the total moved distance for guage.
                    total_moved_distance += moved_distance
                case "d":
                    globals()[f"day_{day_x}"].showStat()
                    # Make choose_stat "True"
                    choose_stat = True
                    # Continue to the start of the while loop.
                    continue
                case "e":
                    # Make died "True"
                    died = True
                    # Break the while loop
                    break
                case "f":
                    functions.help()
                    # Continue to the start of the while loop.
                    continue
                # If the input is "g", activate the cheat
                case "g":
                    # Clear the terminal
                    os.system("cls")
                    print("###############\nAdd Food (A):\nAdd Health (B):\nEnd game (C):\n###############")
                    choice = input("\nWhat do you want to do?: ")
                    # Works same as if elif else
                    match choice.lower():
                        case "a":
                            globals()[f"day_{day_x}"].bought_food = int(input("How many? (type in numbers): "))
                            globals()[f"day_{day_x}"].food_amount += globals()[f"day_{day_x}"].bought_food
                        case "b":
                            globals()[f"day_{day_x}"].gained_health = int(input("How much? (type in numbers): "))
                            globals()[f"day_{day_x}"].health_point += globals()[f"day_{day_x}"].gained_health
                        case "c":
                            # Make died "True"
                            died = False
                            # Break the while loop
                            break
                        case other:
                            print("\n##############\nYou failed to activate the cheat, nothing happened...\nTry Again!\n##############")
                            input("Press Enter to continue: ")
                            # Clear the terminal
                            os.system('cls')
                            choose_stat = True
                            # Continue to the start of the while loop.
                            continue

                # If the input is invalid, nothing happens, try again.
                case other:
                    print("\n##############\nYou failed to buy/rest/move, nothing happened...\nTry Again!\n##############")
                    input("Press Enter to continue: ")
                    # Clear the terminal
                    os.system('cls')
                    # Make choose_stat "True"
                    choose_stat = True
                    # Continue to the start of the while loop.
                    continue

        # Use the start() function to print details
        globals()[f"day_{day_x}"].start()

        # Use day_passed() function to subtract 1 from both health point and food amount as the day progresses.
        (health_point, food_amount) = globals()[f"day_{day_x}"].day_passed()
        # Count the days.
        day_x += 1
################################################################################################################################################

##############################################################END OF THE GAME###################################################################
if not(died):
    #To prevent Error at line 269(day += 1). If the player fail to win the game, the "break" will be used which means (day += 1) will not be used.
    #However, if player win the game, the loop will be continued until it starts again which means (day +=1) will be used.
    #Thus, we have to subtract 1 from day_x if the player won the game.
    day_x -= 1
    # Print an animated message informing the user that they've arrived at their destination.
    print(f"#############################\nDays it took: {day_x}\nAfter traveling 4364km\nYou've arrived to your destination.\n#############################")
    input("\nPress Enter to continue: ")
while True:
    # Clear the terminal
    os.system("cls")
    user_input = input("Do you want to check your histories? (y/n): ")
    #If user input is yes, process.
    if user_input.lower() == "y":
        date_to_check = int(input(f"#############################\nWhich date do you want to check? from 1 ~ {day_x}? (ex 1,2,3,4,5): "))
        #if date we're checking isn't bigger than the day player took, continue the if statement. 
        #If the input is not integer_type (something like : idk, two, three, four)
        if date_to_check <= day_x and type(date_to_check) == int:
            
            # Initializing variables from each day to print summary
            moved_distance = globals()[f"day_{date_to_check}"].moved_distance
            left_distance = globals()[f"day_{date_to_check}"].left_distance
            food_amount = globals()[f"day_{date_to_check}"].food_amount
            bought_food = globals()[f"day_{date_to_check}"].bought_food
            health_point = globals()[f"day_{date_to_check}"].health_point
            gained_health = globals()[f"day_{date_to_check}"].gained_health
            incident = globals()[f"day_{date_to_check}"].incident
            location = globals()[f"day_{date_to_check}"].location
            
            print(f"###############\nDay_{date_to_check}\nMoved distance: {moved_distance}km\nLeft distance: {left_distance}km\nFood amount: {food_amount}\nBought food: {bought_food}\nHealth point: {health_point}\nGained health: {gained_health}\nIncident: {incident}\nPassed city: {location}")
            input("###############\nPress Enter to continue: ")
        else:
            print("###############\nSomething went wrong! try again!")
            # Continue to the start of the while loop.
            continue
    #If user input is no, end the game
    elif user_input.lower() == "n":
        # Break the while loop
        break
    #If user input is invalid, try again
    else:
        print("Something went wrong, please check your answer input.\nTry again!")
        # Wait for 1.5 sec
        time.sleep(1.5)
        # Continue to the start of the while loop.
        continue
# Clear the terminal
os.system("cls")
# END of the game!
print("Thanks for playing this game! byebye!")
################################################################################################################################################