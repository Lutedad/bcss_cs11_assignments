import os

#clear terminal
os.system("cls")
#Intro
input("---------------------------------------------\nWelcome to Lab 5.02!\nYou will add/change/remove/update/print students list.\n---------------------------------------------\n\nPress Enter to continue...")

student_dic = {1234:"asdf",12345:"asdf"}

##################################################################################################################################################################3
#Functions
def addStudent():
    while True:
        #Clear Terminal
        os.system("cls")   
        print("---------------------------------------------")
        #Print current student dict.
        for k,v in student_dic.items():
            print(f"Student Number : {k}, Student Name: {v}")

        print("--------------------add----------------------")
        try:
            number = int(input("Student Number: "))
        except:
            input("\nInvalid input. Please try again.\nPress Enter to continue...")
            continue
        name = input("Student Name: ")
        if name:
            pass
        else:
            input("You cannot leave the name empty! Please try again.\nPress Enter to continue...")
            continue

        if number in student_dic.keys():
            input("\nStudent number you put already exists.\nPlease try again with different student number.\nPress Enter to continue...")
            continue
        else:
            update_val = {number: name}
            student_dic.update(update_val)
            input("\nSuccessfully added!\nPress Enter to continue...")
            return

def removeStudent(): 

    while True:
        #Clear Terminal
        os.system("cls")   
        #Print current student dict.
        for k,v in student_dic.items():
            print(f"Student Number : {k}, Student Name: {v}")
        
        user_input = input("-------------------remove--------------------\nStudent Number (a)\nStudent Name (b)\nExit (c)\n\nChoose the number or name to use (a,b,c): ")

        if user_input.lower() == "a":
            #Try to get student number by user's input. If the input is invalid, it'll automatically process except, which will print Error message and call continue.
            try:
                number = int(input("Student Number: "))
            except:
                input("\nInvalid input. Please try again.\nPress Enter to continue...")
                continue
            #If Student Number is in Student dict's keys, use pop() function with student number.
            if number in student_dic.keys():
                student_dic.pop(number)
                input(f"\nSuccessfully removed.\nPress Enter to continue...")
                break
            else:
                input("\nStudent number you typed does not exist.\nPlease try agian.\n\nPress Enter to continue...")
                continue
        elif user_input.lower() == "b":
            #Get student name by user's input
            name = input("Student Name: ")
            #Use for loop to get every single keys and values
            for k,v in student_dic.items():
                # if name user typed is in dict's value, proceed.
                if v.lower() == name.lower():
                    #While loop to control Invalid user input
                    while True:
                        #Check for duplicated names in dict
                        user_input_dup = input(f"Are you trying to remove {v}, Student number : {k}? (y/n): ")
                        if user_input_dup.lower() == "y":
                            student_dic.pop(k)
                            input(f"\nSuccessfully removed {v}, {k}\n\nPress Enter to continue...")
                            #If user successfully removed a student, use remove to execute removeStudent() function.
                            return
                        elif user_input_dup.lower() == "n":
                            break
                        else:
                            #If user's input is invalid, use continue function to go back to the start of the while loop.
                            #So that user can re-enter the answer.
                            input("Invalid input, please type in y or n.\nPress Enter to continue...")
                            continue
                else:
                    pass
            input("\nStudent does not exist. Please try again.\nPress Enter to continue...")
        elif user_input.lower() == "c":
            return
        else:
            input("Invalid Input! Please type in a/b/c. \nPress Enter to continue...")
            continue
    return

def updateStudent():
    name = ""
    number = ""
    while True:

        #Clear Terminal
        os.system("cls")   
        print("--------------------------------------------")
        #Print current student dict.
        for k,v in student_dic.items():
            print(f"Student Number : {k}, Student Name: {v}")
        #Get user input
        user_input = input("-------------------update--------------------\nStudent Number (a)\nStudent Name (b)\nExit (c)\n\nChoose the number or name to use (a,b,c): ")

        if user_input.lower() == "a":
            #Try to get student number by user's input. If the input is invalid, it'll automatically process except, which will print Error message and call continue.
            try:
                number = int(input("Student Number: "))
            except:
                input("Invalid input. Please try again.\nPress Enter to continue...")
                continue
        elif user_input.lower() == "b":
            name = input("Student Name: ")
        elif user_input.lower() == "c":
            return
        else:
            input("Invalid input. Please try again.\nPress Enter to continue...")
            continue
        
        
        for k,v in student_dic.items():
            new_key = k
            #If number is in student dict's keys or name is in student dict.
            if number == k or name.lower() == v:
                #Check for duplicated names in dict
                user_input_dup = input(f"Are you trying to update {v}, Student number : {k}? (y/n): ")
                #While loop to control Invalid user input
                while True:
                    #Clear terminal & print chosen student
                    os.system("cls")
                    try:
                        print(f"--------------------------------------------\nStudent Number : {k}, Student Name: {student_dic[k]}\n--------------------------------------------")
                    except:
                        print(f"--------------------------------------------\nStudent Number : {new_key}, Student Name: {student_dic[new_key]}\n--------------------------------------------")
                    ###############################################################################
                    if user_input_dup.lower() == "y":
                        user_update = input("Name(a)\nNumber(b)\nExit(c)\n\nChoose what to update..: ")
                        if user_update.lower() == "a":
                            update_name = input("Name: ")
                            student_dic[new_key] = update_name
                            input(f"\nSuccessfully updated {v}, {k}\n\nPress Enter to continue...")
                            continue
                        elif user_update.lower() == "b":
                            try:
                                new_key = int(input("Number: "))
                            except:
                                input("Invalid input. Please try again.\nPress Enter to continue...")
                                continue

                            if new_key in student_dic.keys():
                                input("\nStudent number you put already exists.\nPlease try again with different student number.\nPress Enter to continue...")
                                continue
                            else:
                                student_dic[new_key] = student_dic.pop(k)
                                input(f"\nSuccessfully updated {v}, {k}\n\nPress Enter to continue...")
                                continue

                        elif user_update.lower() == "c":
                            return
                    elif user_input_dup.lower() == "n":
                        break
                    else:
                        #If user's input is invalid, use continue function to go back to the start of the while loop.
                        #So that user can re-enter the answer.
                        input("Invalid input, please type in y or n.\nPress Enter to continue...")
                        os.system("cls")
                        user_input_dup = input(f"Are you trying to update {v}, Student number : {k}? (y/n): ")
                        continue
            else:
                pass
        input("\nStudent does not exist. Please try again.\nPress Enter to continue...")
        continue

def printDict():
    #Clear terminal
    os.system("cls")
    print("-------------------Print---------------------")
    for k,v in student_dic.items():
        print(f"Student Name: {v}, Student Number : {k}")
    input("---------------------------------------------\nPress Enter to continue...")
##################################################################################################################################################################3
#While loop that calls function by user's input until user exits.
while True:
    os.system("cls")

    user_input = input("---------------------------------------------\nPrint roster(a)\n---------------------------------------------\nAdd student to a roster(b)\n---------------------------------------------\nRemove student(c)\n---------------------------------------------\nUpdate student(d)\n---------------------------------------------\nExit(e)\n---------------------------------------------\n\nChoose your task to do (a,b,c,d,e): ")

    if user_input.lower() == "a":
        printDict()
    elif user_input.lower() == "b":
        addStudent()
    elif user_input.lower() == "c":
        removeStudent()
    elif user_input.lower() == "d":
        updateStudent()
    elif user_input.lower() == "e":
        input("THANKS! Press Enter to exit...!")
        break
    else:
        input("Invalid input. Please try again...\n\nPress Enter to continue...")
        continue