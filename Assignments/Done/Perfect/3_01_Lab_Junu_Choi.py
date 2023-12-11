import time
import random
import sys
import os


# Function that prints animated text.
def print_animated_str(text, time_to_sleep):
    for char in str(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        
        #Sleeping
        time.sleep(time_to_sleep)

#Assigning answer variables
ans_1 = "It'll be allllll goooood."
ans_2 = "You need to take some time..."
ans_3 = "Not good..."
ans_4 = "Congrats! You got this."
ans_5 = "Try harder."
ans_6 = "Work harder."
ans_7 = "Work smarter."
ans_8 = "Be yourself."

#To form a list
answers = [ans_1,ans_2,ans_3,ans_4,ans_5,ans_6,ans_7,ans_8]

#To clear the terminal
os.system("cls")

#Print animated text
print_animated_str("What is your concern my friend...?",0.05)

#We don't need to save user's input since it's unnecessary
input("\nSay it!: ")

#To choose random answer for user's question
ran_ans_num = random.randrange(0,8)
ran_ans = answers[ran_ans_num]

#To clear the terminal
os.system("cls")

#Print magical-randomized answer
print_animated_str(ran_ans,0.08)