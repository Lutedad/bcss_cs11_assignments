# Made by Junu Choi 2687251
# This is an Area Calculator that calculates area of a square, a rectangle, a triangle, and a cricle.
#----------------------------------------------------------------------------------------------------
#Importing math to get specific pi
import math

#Greeting
print("\nWelcome to area calculator!")
print("---------------------------------")
print("This Area Calculator is made by Junu Choi")
print("---------------------------------\n\n")

#Square
square_length = float(input("What is the side length of a square?: "))
square_area = square_length * square_length
print("Area of Square =",square_area,"squared units.\n")

#Rectangle
rec_length = float(input("What is the length of a rectangle?: "))
rec_width = float(input("What is the width of a rectangle?: "))
rec_area = rec_length * rec_width
print("Area of Rectangle =",rec_area,"squared units.\n")

#Triangle
tri_base = float(input("What is the base of a triangle?: "))
tri_height = float(input("What is the height of the triangle?: "))
tri_area = tri_base * tri_height * 0.5
print("Area of Triangle =",tri_area,"squared units.\n")

#Circle
cir_radius = float(input("What is the radius of a Circle?: "))
cir_area = cir_radius * cir_radius * math.pi
print("Area of Circle =",cir_area,"squared units.")