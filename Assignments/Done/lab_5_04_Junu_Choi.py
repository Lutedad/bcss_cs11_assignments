##################################################################################################################################################################
#Intro

import os
#clear terminal
os.system("cls")

#Intro
input("---------------------------------------------\nWelcome to Lab 5.02!\nYou will add/change/remove/update/print students list.\n---------------------------------------------\n\nPress Enter to continue...")

student_dic = {1234:{"FirstName":"Junu","LastName":"Choi"},12345:{"FirstName":"Alex","LastName":"Anderson"}}

##################################################################################################################################################################3
#Main Functions

def readFile():
    #Open the file
    originalFile = open("file3.txt","r")

    for item in originalFile.readlines():
        try:
            strip_item = item.strip().split()

            number = int(strip_item[0])
            fname = strip_item[1]
            lname = strip_item[2]

            update_val = {number: {"FirstName":fname,"LastName":lname}}
            student_dic.update(update_val)
        except:
            print("Invalid Type of Source. //ERROR//\nPlease check your txt file..")

def writeFile():
    os.system("cls")
    try:
        msg = ""
        originalFileWrite = open("file3.txt","w")
        for k in student_dic.keys():
            msg += f"{k} {student_dic[k]['FirstName']} {student_dic[k]['LastName']}\n"
        originalFileWrite.write(msg)
        input("Successfully saved!\nPress Enter to continue...")
    except:
        input("Error! Please try again.\nPress Enter to continue...")

def addStudent():

    while True:
        
        #Print student dict
        printDict("-add-")

        #Getting user input.
        try:
            number = int(input("\nStudent Number: "))
        except:
            input("\nInvalid input. Please try again.\nPress Enter to continue...")
            continue
        
        #First&Last name
        fname = input("Student First Name: ")
        lname = input("Student Last Name: ")

        #Checking whether first name & last name is empty string or not.
        if fname and lname:
            pass
        else:
            input("You cannot leave the name empty! Please try again.\nPress Enter to continue...")
            continue

        #If user's input (student number) already exists in student dict, print error message and make the user try again.
        if number in student_dic.keys():
            input("\nStudent number you put already exists.\nPlease try again with different student number.\nPress Enter to continue...")
            continue
        #Else, user may add certain studentNumber:studentName in dict.
        else:
            update_val = {number: {"FirstName":fname,"LastName":lname}}
            student_dic.update(update_val)
            input("\nSuccessfully added!\nPress Enter to continue...")
            #Call return to execute whole addStudent function.
            return

def removeStudent(): 

    while True:

        #Print student dict
        printDict("remove")
        
        user_input = input("\nStudent Number (a)\nStudent Name (b)\nExit (c)\n\nChoose the number or name to use (a,b,c): ")

        #Student Number
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
                return
            #If not, print error message and make user try agian by calling continue.
            else:
                input("\nStudent number you typed does not exist.\nPlease try agian.\n\nPress Enter to continue...")
                continue
        #Student Name
        elif user_input.lower() == "b":
            #Get student's name by user input.
            name = input("Student Full Name: ").replace(" ","") #"replace" purpose/function--> to replace " " with "" in the string. (Which will eventually get rid of spaces in string.)
            
            #If name is True(When string is not empty)
            if name:
                pass
            else:
                input("Error! You should not leave it empty..\nTry again! Press Enter to continue...")
                continue

            #Use for loop to get every single keys and values
            for k,v in student_dic.items():
                # if name user typed is in dict's value, proceed.
                if (v["FirstName"] + v["LastName"]).lower() == name.lower():
                    #While loop to control Invalid user input
                    while True:

                        printDict("remove")

                        #Check for duplicated names in dict
                        user_input_dup = input(f"\nAre you trying to remove {v['FirstName']} {v['LastName']}, Student number : {k}? (y/n): ")
                        #Yes
                        if user_input_dup.lower() == "y":
                            student_dic.pop(k)
                            input(f"\nSuccessfully removed {v['FirstName']} {v['LastName']}, {k}\n\nPress Enter to continue...")
                            #If user successfully removed a student, use return to execute removeStudent() function.
                            return
                        #No
                        elif user_input_dup.lower() == "n":
                            break
                        #Invalid input
                        else:
                            input("\nInvalid input, please type in y or n.\nPress Enter to continue...")
                            continue
                else:
                    pass
            
            #If there is no more student who has (name) as their name, print error message and call continue.
            input("\nStudent does not exist. Please try again.\nPress Enter to continue...")
            continue
        #Exit
        elif user_input.lower() == "c":
            #If user want to exit, call return to execute the function.
            return
        #If user's input's invalid, print error message and make user try again by calling continue.
        else:
            input("Invalid Input! Please type in a/b/c. \nPress Enter to continue...")
            continue

def updateStudent():

    #Initializing variables to avoid possible errors.
    name = ""
    number = ""
    user_input_dup = ""

    while True:

        #Print student dict
        printDict("update")
        
        user_input = input("\nStudent Number (a)\nStudent Name (b)\nExit (c)\n\nChoose the number or name to use (a,b,c): ")

        #If user wants to use student's number
        if user_input.lower() == "a":
            #Try to get student number by user's input. If the input is invalid, it'll automatically process except, which will print Error message and call continue.
            try:
                number = int(input("Student Number: "))
            except:
                input("Invalid input. Please try again.\nPress Enter to continue...")
                continue
        #If user wants to use student's name
        elif user_input.lower() == "b":
            #Get student name by user input.
            name = input("Student Full Name: ").replace(" ","") #replace : to get rid of spaces in the string.

            #If name is True(When string is not empty)
            if name:
                pass
            else:
                input("Error! You should not leave it empty..\nTry again! Press Enter to continue...")
                continue
        #If user wants to exit
        elif user_input.lower() == "c":
            #call return to execute whole function
            return
        #If user's input is invalid.
        else:
            input("\nInvalid input. Please try again.\nPress Enter to continue...")
            continue
        
        #For key,value in student dict's item(keys,values)
        for k,v in student_dic.items():
            if number == k or name.lower() == (v['FirstName'] + v['LastName']).lower():
                #While loop to handle Invalid user input
                while True:

                    #Print student dict
                    printDict("update")

                    #If user input is already "y", don't ask user again.
                    if user_input_dup.lower() != "y":
                        #Check for duplicated names in dict
                        user_input_dup = input(f"\nAre you trying to update {v['FirstName']} {v['LastName']}, Student number : {k}? (y/n): ")
                    else:
                        pass
                    
                    #Yes
                    if user_input_dup.lower() == "y":
                        #While loop to handle Invalid user input
                        while True:
                            #Clear terminal
                            os.system("cls")
                            #Print chosen student
                            print(f"--------------------------------------------\nStudent Number : {k}, Student Name: {student_dic[k]['FirstName']} {student_dic[k]['LastName']}\n--------------------------------------------")
                            #Ask user which task to do.
                            user_update = input("Name(a)\nNumber(b)\nExit(c)\n\nChoose what to update..: ")
                            #Update name
                            if user_update.lower() == "a":
                                #Get first&last name
                                update_fname = input("First Name: ")
                                update_lname = input("Last Name: ")
                                #If first name & last name aren't empty string
                                if update_fname and update_lname:
                                    #Update first&last name
                                    student_dic[k]['FirstName'] = update_fname
                                    student_dic[k]['LastName'] = update_lname
                                    #Print message and break while loop
                                    input(f"\nSuccessfully updated {v['FirstName']} {v['LastName']}, {k}\n\nPress Enter to continue...")
                                    break
                                #If one of first/last name is empty, print error message and call continue to make user try again.
                                else:
                                    input("Error! You should not leave the first or last name empty..\nTry again! Press Enter to continue...")
                                    continue
                            #Update Number
                            elif user_update.lower() == "b":
                                #Try to get new_key value from user's input.
                                try:
                                    new_key = int(input("Number: "))
                                #If the input is string or invalid, print error message and call continue to make user try again.
                                except:
                                    input("\nInvalid input. Please try again.\nPress Enter to continue...")
                                    continue
                                
                                #If new_key value is in student dict key values, print error message and call continue to make user try again.
                                if new_key in student_dic.keys():
                                    input("\nStudent number you put already exists.\nPlease try again with different student number.\nPress Enter to continue...")
                                    continue
                                #If not, update key value to new one.
                                else:
                                    student_dic[new_key] = student_dic.pop(k)
                                    k = new_key
                                    #Print message & call continue to go back.
                                    input(f"\nSuccessfully updated {v['FirstName']} {v['LastName']}, {k}\n\nPress Enter to continue...")
                                    continue
                            #Exit
                            elif user_update.lower() == "c":
                                #Call return to execute function
                                return
                            #If user's input is invalid, print error message and call continue
                            else:
                                input("\nInvalid input. Please try again.\nPress Enter to continue...")
                                continue                 
                    #No
                    elif user_input_dup.lower() == "n":
                        break
                    #Invalid
                    else:
                        #If user's input is invalid, call continue.
                        input("\nInvalid input, please type in y or n.\nPress Enter to continue...")
                        continue
            #If student does not exist.
            else:
                pass
        #If there is no more student who has (name) as their name, print error message and call continue.
        input("\nStudent does not exist. Please try again.\nPress Enter to continue...")
        continue
        
def printDict(msg):
    #Clear terminal
    os.system("cls")
    print("---------------------------------------------")
    for k in student_dic.keys():
        print(f"Student Number : {k}, Student Name : {student_dic[k]['FirstName']} {student_dic[k]['LastName']}")
    print(f"-------------------{msg}---------------------")

##################################################################################################################################################################3
#Main while loop

#Get information/source from existing student roster/file if possible.
readFile()

while True:
    #Clear terminal
    os.system("cls")

    user_input = input("---------------------------------------------\n-Print roster(a)\n-Add student to a roster(b)\n-Remove student(c)\n-Update student(d)\n-Exit(e)\n-Save file(f)\n---------------------------------------------\n\nChoose your task to do (a,b,c,d,e,f): ")

    #Print
    if user_input.lower() == "a":
        printDict("print")
        input("\nPress Enter to continue...")
    #Add
    elif user_input.lower() == "b":
        addStudent()
    #Remove
    elif user_input.lower() == "c":
        removeStudent()
    #Update
    elif user_input.lower() == "d":
        updateStudent()
    #Exit
    elif user_input.lower() == "e":
        input("THANKS! Press Enter to exit...!")
        break
    #Write file (save file)
    elif user_input.lower() == "f":
        writeFile()
    #Invalid
    else:
        input("Invalid input. Please try again...\n\nPress Enter to continue...")
        continue

##################################################################################################################################################################