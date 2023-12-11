#Importing time class & os class
import time
import sys

# Intro to triangle program
print("\nWelcome to the triangle program!!\nYou will be asked to provide three dimensions, and I will tell you if it is a triangle, and if so, what type of triangle it is.\n")

# Getting three inputs of triangle's dimensions.

f_side = float(input("Enter the first side: "))
s_side = float(input("Enter the second side: "))
t_side = float(input("Enter the third side: "))

#printing animation
def print_animated_str (text,time_to_sleep):
    for char in str(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        #sleeping
        time.sleep(time_to_sleep)

print_animated_str("\nCalculating...\n\n",0.065)

# Determining whether it is a triangle or not. &If it is a triangle, what kind of triangle it is.

if ((f_side < s_side + t_side) and (s_side < f_side + t_side) and (t_side < f_side + s_side)):

    if ((f_side == s_side) and (s_side == t_side)):

        print("This is a equilateral triangle.")
    elif ((f_side == s_side and s_side != t_side) or (f_side == t_side and t_side != s_side) or (t_side == s_side and s_side != f_side)):

        print("This is a Isosceles triangle.")
    elif ((f_side ** 2 == s_side **2 + t_side **2) or (s_side ** 2 == f_side **2 + t_side **2) or (t_side ** 2 == s_side **2 + f_side **2)):

        print("This is a Right triangle.")
    else:

        print("This is a Scalene triangle.")
else:

    print(f"{f_side}, {s_side}, and {t_side} do not form a triangle.")

