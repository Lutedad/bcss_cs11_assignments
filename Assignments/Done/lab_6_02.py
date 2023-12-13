'''This program allows user to search cars by it's manufacture,
Price, Colour, Type and so on'''
###################################################
#                    Intro
import os

color_list = ['red','silver','white','black','blue','pink','purple']
manufacture_list = ['Toyota','Hyundai','Bmw','Honda']
###################################################
#              Car Class/functions
class Car():
    '''Set the specific details for car instance'''
    def __init__(self,car_information):
        self.name = car_information[0]
        self.type_car = car_information[1]
        self.color = car_information[2]
        self.manufacture = car_information[3]
        self.price = car_information[4]

def find_by_price():
    '''Find cars by price range'''
    try:
        minimum = int(input("minimum: "))
        maximum = int(input("Maximum: "))
    except TypeError:
        print("Invalid Input")
        return True

    for car_val in cars:
        if car_val.price >= minimum and car_val.price <= maximum:
            print(f'''----------------------------------------
    {car_val.name}, {car_val.type_car}, {car_val.color}, {car_val.manufacture}, {car_val.price}''')
    return False

def find_by_name():
    '''find a car by its name'''
    car_name = input("Car Name: ").lower()
    #If car_name is not empty string
    if car_name:
        for car_val in cars:
            if car_val.name.lower() == car_name:
                print(f'''----------------------------------------
{car_val.name}, {car_val.type_car}, {car_val.color}, {car_val.manufacture}, {car_val.price}''')
    else:
        print('''----------------------------------------
Invalid Input''')
        return True
    return False

def find_by_color():
    '''find a car by its name'''
    car_color = input("Car Color: ").lower()
    #If car_color is in color list
    if car_color in color_list:
        for car_val in cars:
            if car_val.color == car_color:
                print(f'''----------------------------------------
{car_val.name}, {car_val.type_car}, {car_val.color}, {car_val.manufacture}, {car_val.price}''')
    else:
        print('''----------------------------------------
Invalid Input''')
        return True
    return False

def find_by_manufact():
    '''find a car by its manufacture'''
    car_manufacture = input("Car Manufacture: ").lower().capitalize()
    #If car_manufacture is in manufacture list
    if car_manufacture in manufacture_list:
        for car_val in cars:
            if car_val.manufacture == car_manufacture:
                print(f'''----------------------------------------
{car_val.name}, {car_val.type_car}, {car_val.color}, {car_val.manufacture}, {car_val.price}''')
    else:
        print('''----------------------------------------
Invalid Input''')
        return True
    return False
###################################################
#            Initialize Car List
car1 = Car(car_information = ["Ironman","suv","red","Toyota", 100000])
car2 = Car(car_information = ["Superman","sedan","white","Hyundai", 200000])
car3 = Car(car_information = ["Batman","truck","black","BMW", 300000])
car4 = Car(car_information = ["Spiderman","sedan","silver","Toyota", 150000])
car5 = Car(car_information = ["Justman","sedan","red","Honda", 200000])
car6 = Car(car_information = ["Coolname","suv","purple","Hyundai", 250000])
car7 = Car(car_information = ["Justname","sedan","black","Toyota", 350000])
car8 = Car(car_information = ["Carname","truck","pink","BMW", 400000])
car9 = Car(car_information = ["Something","sedan","blue","Toyota", 50000])
car10 = Car(car_information = ["Fancycar","sedan","red","Honda", 90000])

cars = [car1,car2,car3,car4,car5,car6,car7,car8,car9,car10]
###################################################
#               Main While loop
while True:
    os.system("cls")
    user_input = input('''| Which car are you looking for |
|-------------------------------|
|\tPrice\t\t(a)\t|
|\tName\t\t(b)\t|
|\tManufacture\t(c)\t|
|\tColor\t\t(d)\t|
|\tExit\t\t(e)\t|
|-------------------------------|

Find by: ''').lower()
    if user_input:
        match user_input:
            #price
            case "a":
                if find_by_price():
                    continue
            #name
            case "b":
                if find_by_name():
                    continue
            #manufacture
            case "c":
                if find_by_manufact():
                    continue
            #color
            case "d":
                if find_by_color():
                    continue
            #exit
            case "e":
                print("Bye Bye!")
                break
            case others:
                print("\nInvalid input")
    input('''----------------------------------------
    Press Enter to continue...
----------------------------------------''')
