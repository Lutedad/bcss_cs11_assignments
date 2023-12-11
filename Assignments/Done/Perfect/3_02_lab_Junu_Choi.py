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
#print_animated_str("----------------------------\nWelcome to a road trip simulator\nFrom Burnaby to Toronto.....is apx 4364km\nEnjoy your trip!\n----------------------------",0.04)
input("Press Enter to start...")

#Distance we are traveling
left_distance = 4364
#Counting days
day_x = 0

#Name : travel
#Purpose : To calculate left_distance and moved_distance randomly. + To count the days.
#Input : left_distance(int), day_x(int)
#Output : left_distance, day_x, moved_distance
def travel(left_distance,day_x):
        #Randomly assigning numbers between 300~400
        moved_distance = random.randint(300,400)
        if (left_distance - moved_distance > 0):
            #calculating left distance by subtracting the moved_distance from left distance.
            left_distance -= moved_distance
        #If the result is negative
        else:
            #re-assign the moved_distance with left_distance and make left_distance zero.
            moved_distance = left_distance
            left_distance = 0
        day_x += 1
        return left_distance, day_x, moved_distance

#clear the terminal
os.system('cls')

#While left distance is bigger than 0, recieve the output from the travel function and print it.
while left_distance > 0:
    (left_distance, day_x, moved_distance) = travel(left_distance,day_x)
    print(f"Day_{day_x}, you traveled {moved_distance}km. {left_distance} left.\n")
    time.sleep(0.5)

#Print animated text
print_animated_str(f"#############################\nDays it took : {day_x}\nAfter traveling 4364km\nYou've arrived to your destination.\n#############################",0.05)
