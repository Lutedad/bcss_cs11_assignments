import random
import os,sys
import time

#Clear terminal
os.system("cls")

#Name : cm_to_in_ft
#Purpose : prints animated text.
#Input : text to animate (str), time_to_sleep (int)
#Output : None
def print_animated_str(text, time_to_sleep):
    for char in str(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        
        #Sleeping
        time.sleep(time_to_sleep)



#Intro to road trip simulation
print_animated_str("----------------------------\nWelcome to a road trip simulator\nFrom Burnaby to Toronto.....is apx 4364km\nEnjoy your trip!\n----------------------------",0.04)
input("\nPress Enter to start...")

#Distance we are traveling
left_distance = 4364
#Counting days
day_x = 1
#Randomly assign food amount to start
food_amount = random.randint(4,10)
#Randomly assign health point to start
health_point = random.randint(4,10)
#List contains what incidents will happen during a day
#20% chance of getting bad incidents.
event = ["Illness","Bad_Weather","Nothing","Nothing","Nothing","Nothing","Nothing","Nothing","Nothing","Nothing"]
#Name : travel
#Purpose : To calculate left_distance and moved_distance randomly. + To count the days.
#Input : left_distance(int), day_x(int)
#Output : left_distance, day_x, moved_distance
def travel(left_distance,weather):
        if weather == False:
            #Randomly assigning numbers between 300~400
            moved_distance = random.randint(300,400)
        else:
            #Randomly assigning numbers between 300~400
            moved_distance = random.randint(100,200)
        if (left_distance - moved_distance > 0):
            #calculating left distance by subtracting the moved_distance from left distance.
            left_distance -= moved_distance
        #If the result is negative
        else:
            #re-assign the moved_distance with left_distance and make left_distance zero.
            moved_distance = left_distance
            left_distance = 0
        return left_distance, moved_distance

#Name : buy_food
#Purpose : To purchase between 1-3 kg food per action
#Input :  current food_amount
#Output : ___ kg of food
def buy_food(food_amount):
    amount = random.randint(1,3)
    food_amount += amount
    return food_amount, amount

#Name : rest
#Purpose : To restore between 1-3 health points per action
#Input : current health point
#Output : ___ amount(s) of health point
def rest(health_point):
    amount = random.randint(1,3)
    health_point += amount
    return health_point, amount

#Name : day_passed
#Purpose : To use 1 kg of food and 1 health points per each day
#Input : health_point,food_amount
#Output : ___ -1 kg of food, ____ - 1 amount(s) of health point
def day_passed(health_point,food_amount):
    health_point -= 1
    food_amount -= 1
    return health_point,food_amount

#Name : start
#Purpose : To print left distance, current food and health points
#Input : None
#Output : none
def start(day_x,moved_distance,bought_food,gained_health):
    #clear the terminal
    os.system('cls')
    print_animated_str(f"Day_{day_x}\n\nBought Food: {bought_food}kg\n\nGained health point: {gained_health}\n\nYou traveled {moved_distance}km\n",0.05)
    time.sleep(1.5)
    #clear the terminal
    os.system('cls')


#Name : showStat
#Purpose : To show stats
#Input : left_distance, health_point, food_amount
#Output : None
def showStat(left_distance, health_point, food_amount):
    os.system("cls")
    print_animated_str(f"Your current left distance : {left_distance}km\nHealth Points : {health_point}\nLeft Foods: {food_amount}",0.05)
    #wait 2sec
    time.sleep(2)
    #clear the terminal
    os.system('cls')


#clear the terminal
os.system('cls')
#While left distance is bigger than 0, recieve the output from the travel function and print it.
while left_distance > 0:

    #To prevent error occuring
    moved_distance = 0
    gained_health = 0
    bought_food = 0
    weather = False
    choose_stat = False

    #If player chose (D) Show Stats, the incident of current day should not be changed.
    if choose_stat:
        pass
    else:
        #Randomly choose what the incident is.
        incident = random.choice(event)

    
    #If the incident is bad weather or illness, player must rest or decrease the travelled distance.
    if incident == "Nothing":
        pass
    elif incident == "Bad_Weather":
        print_animated_str("OH..!\nWeather is too bad...",0.05)
        time.sleep(1)
        os.system("cls")
        weather = True

    elif incident == "Illness":
        print_animated_str("OH..!\nYou caught cold...must rest...",0.05)
        time.sleep(1)
        (health_point,gained_health) = rest(health_point)
        os.system("cls")


    #If one of health point and food amount is zero or low, game over.
    if health_point <= 0 or food_amount <= 0:
        #clear terminal
        os.system('cls')
        #print animated string that informs the user that it's a game over.
        print_animated_str(f"Day_{day_x}\n\nEH! You Died.",0.1)
        #wait 1 sec
        time.sleep(1)
        #End the program
        sys.exit()
    else:
        if incident != "Illness":
            print_animated_str(f"Day_{day_x}\n\nBuy food (A)\nRest (B)\nMove (C)\nShow Stats (D)",0.05)
            #Get user's input
            choice = input("\n\nWhat do you want to do?: ")
            if choice.lower() == "a":
                (food_amount,bought_food) = buy_food(food_amount)
            elif choice.lower() == "b":
                (health_point,gained_health) = rest(health_point)
            elif choice.lower() == "c":
                (left_distance, moved_distance) = travel(left_distance,weather)
            elif choice.lower() == "d":
                showStat(left_distance,health_point,food_amount)
                choose_stat = True
                continue
            #If the input is cheat, activate the cheat and immediately win the game
            elif choice.lower() =="cheat":
                break
            #If the input is invalid, nothing happens but the day goes.
            else:
                print_animated_str("\nYou failed to buy/rest/move, nothing happened...\n\nTry Again!",0.07)
                time.sleep(1)
                #clear terminal
                os.system('cls')
                #Player have to try agian with same incident.
                choose_stat = True
                #To go back to the start of the while loop.
                continue
        #use start() function to print details
        start(day_x,moved_distance,bought_food,gained_health)
        #Counting days.
        day_x += 1
        #use day_passed() function to subtract 1 from each health point and food amount as day goes.
        (health_point,food_amount) = day_passed(health_point,food_amount)

        

os.system('cls')
#Print animated text that informs user's arrived the destination.
print_animated_str(f"#############################\nDays it took : {day_x}\nAfter traveling 4364km\nYou've arrived to your destination.\n#############################",0.05)
