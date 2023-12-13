'''This program allows user to search cars by it's manufacture,
Price, Colour, Type and so on'''
###################################################
#                    Import
import os
###################################################
#                  Car Class
class Car():
    '''Set the specific details for car instance'''
    def __init__(self,name,type_car,color,manufacture,price):
        self.name = name
        self.type_car = type_car
        self.color = color
        self.manufacture = manufacture
        self.price = price
    
def find(user_input):
    '''Looks for car based on user_input'''
    match user_input:
        #price
        case "a":
            try:
                min = int(input("Minimum: "))
                max = int(input("Maximum: "))
            except TypeError:
                return False
            for car_inst in cars:
                if car_inst.price >= min and car_inst.price <= max:
                    print(f'''----------------------------------------
{car_inst.name},{car_inst.type_car},{car_inst.color},{car_inst.manufacture},{car_inst.price}''')
            input("\nPress Enter to continue...")
        #name
        case "b":
            pass
        #manufacture
        case "c":
            pass
        #color
        case "d":
            pass
        #exit
        case "e":
            return False
        case _:
            return False

###################################################
#          Initialize Car List
car1 = Car("JustName","suv","red","Toyota", 100000)
car2 = Car("JustName","sedan","white","Hyundai", 200000)
car3 = Car("JustName","truck","black","BMW", 300000)
car4 = Car("JustName","sedan","silver","Toyota", 150000)
car5 = Car("JustName","sedan","red","Honda", 200000)
car6 = Car("JustName","suv","purple","Hyundai", 250000)
car7 = Car("JustName","sedan","black","Toyota", 350000)
car8 = Car("JustName","truck","pink","BMW", 400000)
car9 = Car("JustName","sedan","blue","Toyota", 50000)
car10 = Car("JustName","sedan","red","Honda", 90000)

cars = [car1,car2,car3,car4,car5,car6,car7,car8,car9,car10]
###################################################
#               Main While loop
while True:
    os.system("cls")
    user_input = input('''Which car are you looking for?
Price (a)
Name (b)
Manufacture (c)
Color (d) 
Exit (e)

Find by: ''').lower()
    if user_input:
        if find(user_input):
            continue
        if user_input == "e":
            print("Bye Bye!")
            break