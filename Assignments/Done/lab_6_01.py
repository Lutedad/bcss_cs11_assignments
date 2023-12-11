#################################################################################
import os
#################################################################################3
class Pet():
    def __init__(self,name,type_animal,sound):
        self.name = name
        self.type_animal = type_animal
        self.sound = sound


    def add_pet(self):
        #Pet name
        self.name = input("---------------------------\nPet Name: ").lower().capitalize()

        #If pet name is not an empty string
        if self.name:

            self.type_animal = input("---------------------------\nPet Type: ").lower()

            #If pet type user typed is in pet type list.
            if self.type_animal in pet_type_list:

                #If it's a cat
                if self.type_animal == "cat":
                    self.sound = "meow"
                #If it's a dog
                elif self.type_animal == "dog":
                    self.sound = "woof"
                #If it's a turtle
                elif self.type_animal == "turtle":
                    self.sound = "I AM THE TURTLE"
                #If it's a bird
                elif self.type_animal == "bird":
                    self.sound = "whistles"
                #If it's a fish
                else:
                    self.sound = "I AM THE FISH"
                input("\nSuccessfully Added! \nPress Enter to continue...")
                return True
            
            #If pet type user typed is not in pet type list.
            print('''
            Error! We don't take this type of pet.
            Please try again with different type of pet.''')
            input("Press Enter to continue...")
            return False
        #If it's empty string, print Error message
        input('''
Error! 
You cannot leave it empty. 

Please try again
Press Enter to continue...''')
            
        return False
    
    def adopt_pet(self):
        while True:
            os.system("cls")

            #Pet name
            self.name = input('''
Type check to check pet list
---------------------------
Pet Name: ''').lower().capitalize()

            #If pet name is not an empty string
            if self.name:

                #If user want to check pet list
                if self.name == "Check":
                    print_pet()
                    continue

                self.type_animal = input("---------------------------\nPet Type: ").lower()

                #If pet type user typed is in pet type list.
                if self.type_animal in pet_type_list:

                    for i in range(1,capacity):
                        if globals()[f"pet_{i}"].name == self.name:
                            del globals()[f"pet_{i}"]
                            input("\nSuccessfully Adopted! \nPress Enter to continue...")
                            return False

                    input('''
We don't have the pet you are asking for.
Try again with different name/type!

Press Enter to continue...''')
                    return True
            #If it's empty string, print Error message
            input("\nError! You cannot leave it empty. Please try again\nPress Enter to continue...")
            return False

def print_pet():
    for i in range(1,capacity):
        try:
            print(f'''------------------------------
Name: {globals()[f"pet_{i}"].name}, Type: {globals()[f"pet_{i}"].type_animal}, Sound: {globals()[f"pet_{i}"].sound}''')
        except:
            print("\nWe don't have pets currently..")
    input("\nPress Enter to continue...")
    return

def print_detail():
    pass

capacity = 1
pet_type_list = ["cat","dog","turtle","bird","fish"]
#################################################################################
while True:
    #Clear Terminal
    os.system("cls")

    #Initializing variables to prevent Errors
    PETTYPE = ""
    PETNAME = ""
    PETSOUND = ""

    globals()[f"pet_{capacity}"] = Pet(name = PETNAME, type_animal = PETTYPE, sound = PETSOUND)

    #Intro
    print("-------------------------\n|\tWelcome!\t|\n-------------------------")

    print("|\tAdopt\t\t(a)\n|\tAdd\t\t(b)\n|\tPrint\t\t(c)\n|\tDetail\t\t(d)\n|\texit\t\t(e)\n---------------------------")
    user_input = input("What are you going to do? (a,b,c,d,e): ").strip().lower()

    #Adopt (remove animal)
    if user_input == "a":
        if globals()[f"pet_{capacity}"].adopt_pet():
            continue
    #Add
    elif user_input == "b":
        if globals()[f"pet_{capacity}"].add_pet():
            capacity += 1
        else:
            continue
    #Print
    elif user_input == "c":
        print_pet()
    #Detail
    elif user_input == "d":
        input("\nTODO\nPress Enter to continue...")
        pass #TODO
    #Exit
    elif user_input == "e":
        input("\nByeBye!\nPress Enter to continue...")
        break
    #Invalid
    else:
        input("\nInvalid input, please try again.\nPress Enter to continue...")
        continue