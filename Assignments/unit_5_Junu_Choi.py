##################################################################################################################################################################
#Intro

import os
#clear terminal
os.system("cls")

#Intro
input("---------------------------------------------\nWelcome to Unit5 Project!\nYou will add/change/remove/update/print students list.\n---------------------------------------------\n\nPress Enter to continue...")

#Available subjects: Math, Science, English, Socials, Business, PE, French, Computer, Band, Drama, History
availSubList = ["Math", "Science", "English", "Socials", "Business", "PE", "French", "Computer", "Band", "Drama", "History"]
#Student #, as integer, 3-digits long
#Example ==> {student#:{FirstName:Bob, LastName:Bains, Block1:Math, Block2:Science, Block3:English, Block4:Socials}
student_dic = {1234:{"FirstName":"Junu","LastName":"Choi","Block1":"Math","Block2":"Science","Block3":"English","Block4":"Socials"}}

###################################################
#ADMIN PASSWORD
adminPassword = "admin1234"
###################################################

##################################################################################################################################################################3
#Main Functions

#Choose what to check _ Done
def whatToCheck():
    #Clear terminal
    os.system("cls")
    #Ask user what to check
    user_input = input("-----------------------------------------------------\nCheck student(a)\nCheck class(b)\n\nChoose what to check (a,b): ").lower()
    #If user_input is not a empty string
    if user_input:
        #Check student
        if user_input == "a":
            studentSchedule()
            return True
        #Check class
        elif user_input == "b":
            classList()
            return True
        #Invalid input
        else:
            return False
    #invalid input
    else:
        return False
#Return True if it has duplicates _ Done
def has_duplicates(seq):
    #if len of list is not same as len of set(list) [set() deletes duplicated values in list], it means there's a duplicated value in list.
    return len(seq) != len(set(seq))
#Read information from file _ Done
def readFile():
    #Open the file
    originalFile = open("file2.txt","r")

    for item in originalFile.readlines():
        try:
            strip_item = item.strip().split()

            number = int(strip_item[0])
            fname = strip_item[1]
            lname = strip_item[2]
            block1 = strip_item[3]
            block2 = strip_item[4]
            block3 = strip_item[5]
            block4 = strip_item[6]


            update_val = {number: {"FirstName":fname,"LastName":lname,"Block1":block1,"Block2":block2,"Block3":block3,"Block4":block4}}
            student_dic.update(update_val)
        except:
            #Clear Terminal
            os.system("cls")
            input("Invalid Type of Source. //ERROR//\nPlease check your txt file..\n\nPress Enter to continue...")
            return
#Write information on file _ Done
def writeFile():

    #Check if the password matches
    if passwordCheck():
        pass
    #If it mismatch, call return
    else:
        return
    
    #Clear terminal
    os.system("cls")
    try:
        msg = ""
        #Open file as "w"
        originalFileWrite = open("file2.txt","w")
        #For every keys in student roster
        for k in student_dic.keys():
            #Add student's information/string to msg
            msg += f"{k} {student_dic[k]['FirstName']} {student_dic[k]['LastName']} {student_dic[k]['Block1']} {student_dic[k]['Block2']} {student_dic[k]['Block3']} {student_dic[k]['Block4']}\n"
        #After process, write the "msg" 
        originalFileWrite.write(msg)
        input("Successfully saved!\nPress Enter to continue...")
    except:
        input("Error! Please try again.\nPress Enter to continue...")
#Add Student _ Done
def addStudent():

    #Check if the password matches
    if passwordCheck():
        pass
    #If it mismatch, call return
    else:
        return

    #While loop to handle invalid inputs
    while True:

        #Clear terminal
        os.system("cls")

        user_input = input("--------------------------------------\n|Type 'check' to check student roster.\n|\n|Type Student Number You Want to Add: ")
        #If user input is check
        if user_input.lower() == "check":
            #If nothing happened during the process, pass.
            if whatToCheck():
                continue
            #If somehow whatToCheck process got executed due to error/invalid input call continue.
            else:
                input("\nInvalid input. Please try again.\nPress Enter to continue...")
                continue
        #if user input is something else (e.g. Integer, Empty)
        else:
            #Trying to get student number by user input.
            try:
                number = int(user_input)
            #If it's invalid (Somehow error or string input/empty)
            except:
                input("\nInvalid input. Please try again.\nPress Enter to continue...")
                continue

        #If user's input (student number) already exists in student dict, print error message and make the user try again.
        if number in student_dic.keys():
            input("\nStudent number you put already exists.\nPlease try again with different student number.\n\nPress Enter to continue...")
            continue
        #Else, user may add certain studentNumber:studentName in dict.
        else:
            #First&Last name
            fname = input("|Student First Name: ").replace(" ","").lower() #"replace" purpose/function--> to replace " " with "" in the string. (Which will eventually get rid of spaces in string.)
            lname = input("|Student Last Name: ").replace(" ","").lower()
    
            #Checking whether first name & last name is empty string or not.
            if fname and lname:
                print("|------------------------------------\n|Available subjects: Math, Science, English, Socials, Business, PE, French, Computer, Band, Drama, History")
                block1 = input("|First Block: ").replace(" ","").lower()
                print("|------------------------------------")
                block2 = input("|Second Block: ").replace(" ","").lower()
                print("|------------------------------------")
                block3 = input("|Third Block: ").replace(" ","").lower()
                print("|------------------------------------")
                block4 = input("|Fourth Block: ").replace(" ","").lower()
                print("|------------------------------------")
    
                #Checking whether courses are empty string or not.
                if (block1 and block2 and block3 and block4):
                    #Make a list of blocks/periods/classes
                    items = [block1, block2, block3, block4]
                    #If block1,2,3,4 is in availSublist, process. Further information -->https://stackoverflow.com/questions/21344842/if-a-or-b-in-l-where-l-is-a-list
                    if all( (i.capitalize() in availSubList) or (i == "pe") for i in items ):
                        #Checking whether courses are duplicated or not.
                        #If it has duplicates
                        if has_duplicates(items):
                            input("You cannot have same classes. Please try again.\nPress Enter to continue...")
                            continue
                        #If it does not have duplicates
                        else:
                            for i in range(len(items)):
                                if items[i] == "pe":
                                    items[i] = "PE"
                                else:
                                    items[i] = items[i].capitalize()
                            update_val = {number: {"FirstName":fname.capitalize(),"LastName":lname.capitalize(),"Block1":items[0],"Block2":items[1],"Block3":items[2],"Block4":items[3]}}
                            student_dic.update(update_val)
                            input("\nSuccessfully added!\nPress Enter to continue...")
                            #Call return to execute whole addStudent function.
                            return
                    #If block1 or 2 or 3 or 4 is not in availSublist
                    else:
                        input("\nClass does not exist! Please try again.\nPress Enter to continue...")
                        continue
                #If there's a empty string
                else:
                    input("\nYou cannot leave it empty! Please try again.\nPress Enter to continue...")
                    continue
            #If firstname/lastname is empty string.
            else:
                input("\nYou cannot leave the name empty! Please try again.\nPress Enter to continue...")
                continue
#Remove Student _ Done
def removeStudent(): 

    #Check if the password matches
    if passwordCheck():
        pass
    else:
        return

    while True:
        
        #Clear Terminal
        os.system("cls")

        user_input = input("-----------------------------------------------------\nStudent Number (a)\nStudent Name (b)\nExit (c)\nCheck student list(d)\n\nChoose the number or name to indicate the student (a,b,c,d): ")

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
            name = input("Student Full Name: ").replace(" ","").lower() #"replace" purpose/function--> to replace " " with "" in the string. (Which will eventually get rid of spaces in string.)
            
            #If name is True(When string is not empty)
            if name:
                pass
            else:
                input("Error! You should not leave it empty..\nTry again! Press Enter to continue...")
                continue

            #Use for loop to get every single keys and values
            for k,v in student_dic.items():
                # if name user typed is in dict's value, proceed.
                if (v["FirstName"] + v["LastName"]).lower() == name:
                    #While loop to handle Invalid user input
                    while True:

                        #Ask user to indicate correct student in case there's same named student in roster.
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
        #Check student list
        elif user_input.lower() == "d":
            #If nothing happened during the process, pass.
            if whatToCheck():
                pass
            #If somehow whatToCheck process got executed due to error/invalid input call continue.
            else:
                input("\nInvalid input. Please try again.\nPress Enter to continue...")
                continue
        #Invalid input
        else:
            input("\nInvalid Input! Please type in a/b/c/d. \nPress Enter to continue...")
            continue
#Update Student _ Done
def updateStudent():

    #Check if the password matches
    if passwordCheck():
        pass
    else:
        return

    #Initializing variables to avoid possible errors.
    name = ""
    number = ""
    user_input_dup = ""

    #While loop to handle invalid inputs _ Done
    while True:
        #Clear terminal
        os.system("cls")

        user_input = input("-----------------------------------------------------\nStudent Number (a)\nStudent Name (b)\nExit (c)\nCheck student list(d)\n\nChoose the number or name to indicate the student (a,b,c,d): ")

        #If user wants to use student's number _ Done
        if user_input.lower() == "a":
            #Try to get student number by user's input. If the input is invalid, it'll automatically process except, which will print Error message and call continue.
            try:
                number = int(input("Student Number: "))
            except:
                input("\nInvalid input. Please try again.\nPress Enter to continue...")
                continue
        #If user wants to use student's name _ Done
        elif user_input.lower() == "b":
            #Get student name by user input.
            name = input("Student Full Name: ").replace(" ","").lower() #"replace" purpose/function--> to replace " " with "" in the string. (Which will eventually get rid of spaces in string.)

            #If name is True(When string is not empty)
            if name:
                pass
            else:
                input("\nError! You should not leave it empty..\nTry again! Press Enter to continue...")
                continue
        #If user wants to exit _ Done
        elif user_input.lower() == "c":
            #call return to execute whole function
            return
        #If user wants to check student list _ Done
        elif user_input.lower() == "d":
            #If nothing happened during the process, pass.
            if whatToCheck():
                continue
            #If somehow whatToCheck process got executed due to error/invalid input call continue.
            else:
                input("\nInvalid input. Please try again.\nPress Enter to continue...")
                continue
        #If user's input is invalid.
        else:
            input("\nInvalid input. Please try again.\nPress Enter to continue...")
            continue
        
        #For key,value in student dict's item(keys,values)
        for k,v in student_dic.items():
            #Check if number matches key or name matches name value _ Done
            if number == k or name == (v['FirstName'] + v['LastName']).lower():
                #While loop to handle Invalid user input
                while True:

                    #Clear terminal
                    os.system("cls")

                    #If user input is already "y", don't ask user again.
                    if user_input_dup != "y":
                        #Check for duplicated names in dict
                        user_input_dup = input(f"\nAre you trying to update {v['FirstName']} {v['LastName']}, Student number : {k}? (y/n): ").replace(" ","").lower() #"replace" purpose/function--> to replace " " with "" in the string. (Which will eventually get rid of spaces in string.)
                    else:
                        pass
                    
                    #Yes _ Done
                    if user_input_dup == "y":
                        #While loop to handle Invalid user input
                        while True:

                            #Clear terminal
                            os.system("cls")
                            #Print chosen student
                            printStudent(k)
                            
                            #Ask user which task to do.
                            user_update = input("Name(a)\nNumber(b)\nClasses[Blocks](c)\nExit(e)\n\nChoose what to update..: ").replace(" ","").lower()

                            #Update name _ Done
                            if user_update == "a":
                                #Get first&last name
                                update_fname = input("\nFirst Name: ").replace(" ","").lower().capitalize()
                                update_lname = input("Last Name: ").replace(" ","").lower().capitalize()
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
                            #Update Number _ Done
                            elif user_update == "b":
                                #Try to get new_key value from user's input.
                                try:
                                    new_key = int(input("\nNumber: "))
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
                            #Update Classes _ Done
                            elif user_update == "c":
                                while True:
                                    #Initializing variables to avoid errors.
                                    finish = False
                                    finishchange = False

                                    #Clear terminal
                                    os.system("cls")
                                    #Print chosen student
                                    printStudent(k)
                                    
                                    #Print available subjects.
                                    print("Available subjects: Math, Science, English, Socials, Business, PE, French, Computer, Band, Drama, History\n---------------------------------------")
                                    #Get user input
                                    classinput = input("Type exit to exit!\n\nWhich class/subject do you want to update?: ").replace(" ","").lower().capitalize()

                                    #Check if classinput is valid,
                                    if classinput and classinput in availSubList:

                                        for i in range(1, 5):
                                            #For 1,2,3,4 -> Block1,Block2,Block3,Block4
                                            ori_block = f"Block{i}"

                                            #for certain block, check if Student's class equals to classinput (user typed).
                                            if student_dic[k][ori_block] == classinput:
                                                #Clear terminal
                                                os.system("cls")
                                                
                                                #Print chosen student
                                                printStudent(k)
                                                #Print available subjects.
                                                print("Available subjects: Math, Science, English, Socials, Business, PE, French, Computer, Band, Drama, History\n---------------------------------------")
                                                
                                                #Ask user what to put instead of current schedule
                                                changeClass = input(f"Type exit to exit!\n\nWhich course do you want to put instead of {classinput.capitalize()}?: ").lower().capitalize()

                                                #Check if answer/input is valid (check if it's in availSubList.),
                                                if changeClass in availSubList:

                                                    #For loop to check every blocks
                                                    for j in range(1,5):
                                                        block = f"Block{j}"

                                                        #Check if the course user put is already in current schedule or not.
                                                        if changeClass != v[block]:
                                                            pass
                                                        else:
                                                            input("\nIt already exists..Please try agian\nPress Enter to continue...")
                                                            finish = True
                                                            #Call break
                                                            break
                                                    
                                                    #If the process successfully went through, process
                                                    student_dic[k][ori_block] = changeClass
                                                    
                                                    #Print message
                                                    input(f"\nSuccessfully updated {v['FirstName']} {v['LastName']}, {k}\n\nPress Enter to continue...")
                                                    finish = True
                                                    #break for loop
                                                    break
                                                #If user want to exit
                                                elif changeClass.lower() == "exit":
                                                    finishchange = True
                                                    #Break the for loop
                                                    break
                                                #Invalid input
                                                else:
                                                    input("Invalid Input! Please try again.\nPress Enter to continue...")
                                                    finish = True
                                                    break
                                            #If it does not equal to user's input(classinput), pass.
                                            else:
                                                pass
                                        
                                        #If user successfully updated the class, do not print error message/ just pass.    
                                        if finish:
                                            pass
                                        else:
                                            input(f"\nError! The class is not in {student_dic[k]['FirstName']} {student_dic[k]['LastName']}'s curriculum.\nPress Enter to continue...")        
                                            continue

                                        #If user want to finish/execute the process(Changing classes)
                                        if finishchange:
                                            break
                                        else:
                                            pass
                                    #Check if user want to exit.
                                    elif classinput.lower() == "exit":
                                        break
                                    #If it's invalid.
                                    else:
                                        input("\nInvalid input. Please try again.\nPress Enter to continue...")
                                        continue
                                
                                #call continue to go to the start of outer while loop when inner while loop's process is done
                                continue
                            #Exit _ Done
                            elif user_update == "e":
                                #Call return to execute function
                                return
                            #If user's input is invalid, print error message and call continue _ Done
                            else:
                                input("\nInvalid input. Please try again.\nPress Enter to continue...")
                                continue                 
                    #No _ Done
                    elif user_input_dup == "n":
                        break
                    #Invalid _ Done
                    else:
                        #If user's input is invalid, call continue.
                        input("\nInvalid input, please type in y or n.\nPress Enter to continue...")
                        continue
            #If student does not exist. _ Done
            else:
                pass
        
        #Print Error message & call continue if there's no more students with same name.
        input("\nStudent does not exist. Please try again.\nPress Enter to continue...")
        continue
#Print Student Dict _ Done
def printDict(msg):
    countDict = 0
    #Clear terminal
    os.system("cls")
    print("------------------------------------------------------------------------------------------")
    for k in student_dic.keys():
        countDict += 1
        print(f"{student_dic[k]['FirstName']} {student_dic[k]['LastName']}[{k}], Block1 : {student_dic[k]['Block1']}, Block2 : {student_dic[k]['Block2']}, Block3 : {student_dic[k]['Block3']}, Block4 : {student_dic[k]['Block4']}")
        print("------------------------------------------------------------------------------------------")
    print(f"-------------------{msg}---------------------")
    print(f"Total {countDict} students.")
#Print certain student's schedule _ Done
def studentSchedule():
    
    while True:

        #Clear terminal
        os.system("cls")

        user_input = input("-----------------------------------------------------\nStudent Number (a)\nStudent Name (b)\nExit (c)\nCheck student list(d)\n\nChoose the number or name to indicate the student (a,b,c,d): ").replace(" ","").lower()

        #Student Number _ Done
        if user_input == "a":

            #Try to get student number by user's input. If the input is invalid, it'll automatically process except, which will print Error message and call continue.
            try:
                number = int(input("Student Number: "))
            except:
                input("\nInvalid input. Please try again.\nPress Enter to continue...")
                continue

            #For every key values in student roster,
            for k in student_dic.keys():
                
                #Check if the key matches number user inputted.
                if k == number:

                    #Clear terminal
                    os.system("cls")

                    #Print chosen student
                    printStudent(k)

                    input("\nPress Enter to continue...")
                    return
                #If it does not match, pass
                else:
                    pass
            #If no single student matches, print error message and call continue.
            input("\nStudent does not exist, please try again with different number.\nPress Enter to continue...")
            continue
        #Student Name
        elif user_input == "b":

            #Get student's name by user input.
            name = input("Student Full Name: ").replace(" ","").lower() #"replace" purpose/function--> to replace " " with "" in the string. (Which will eventually get rid of spaces in string.)
            
            #If name is True(When string is not empty)
            if name:
                pass
            else:
                input("Error! You should not leave it empty..\nTry again! Press Enter to continue...")
                continue

            #Use for loop to get every single keys and values
            for k,v in student_dic.items():
                # if name user typed is in dict's value, proceed.
                if (v["FirstName"] + v["LastName"]).lower() == name:
                    #While loop to handle Invalid user input
                    while True:

                        #Clear Terminal
                        os.system("cls")

                        #Ask user to indicate correct student in case there's same named student in roster.
                        user_input_dup = input(f"\nAre you trying to indicate {v['FirstName']} {v['LastName']}, Student number : {k}? (y/n): ")

                        #Yes
                        if user_input_dup.lower() == "y":
                            printStudent(k)
                            break
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
        #Exit _ Done
        elif user_input == "c":
            #If user want to exit, call return to execute the function.
            return
        #Check student dict _ Done
        elif user_input == "d":
            #If nothing happened during the process, pass.
            if whatToCheck():
                continue
            #If somehow whatToCheck process got executed due to error/invalid input call continue.
            else:
                input("\nInvalid input. Please try again.\nPress Enter to continue...")
                continue
        #If user's input's invalid, print error message and make user try again by calling continue. _ Done
        else:
            input("\nInvalid Input! Please type in a/b/c/d. \nPress Enter to continue...")
            continue
#Print certain class's (subject's) student list _ Done
def classList():

    while True:
        count = 0
        #Clear Terminal
        os.system("cls")
        #Intro
        print("------------------------------------------------------------------------------\nAvailable subjects: Math, Science, English, Socials, Business, PE, French, Computer, Band, Drama, History\n------------------------------------------------------------------------------")
        #Get input from user
        classinput = input("\nType exit to exit...\n\nWhich class/subject do you want to check?: ").replace(" ","").lower().capitalize()
        #If classinput is valid input & in availSublist OR it's exit/pe
        if ((classinput and classinput in availSubList) or classinput == "Exit") or classinput == "Pe":
            #If user want to exit
            if classinput == "Exit":
                return
            #If user want to continue
            else:
                try:
                    period = int(input("What period? (1,2,3,4): "))

                    #If type is integer and it's between 0~5
                    if type(period) == int and 0 < period < 5:
                        block = f"Block{period}"
                    else:
                        input("\nInvalid input. Please try again.\nPress Enter to continue...")
                        continue
                    
                    #Clear Terminal
                    os.system("cls")

                    #for every students, check if Student's Nth period equals to classinput user typed & print student information.
                    for k in student_dic.keys():
                        #If student's Nth period in student dict matches user input
                        if student_dic[k][block].lower().capitalize() == classinput:
                            printStudent(k)
                            count += 1
                        #If it does not match, pass.
                        else:
                            pass
                    
                    input(f"Total: {count} students\n\nPress Enter to continue...")
                    continue
                #If input is invalid
                except:
                    input("\nInvalid input. Please try again.\nPress Enter to continue...")
                    continue
        #If invalid, print error message and call continue.
        else:
            input("\nInvalid input. Please try again.\nPress Enter to continue...")
            continue
#Print Certain Student._ Done
def printStudent(k):
    #Print chosen student
    print("------------------------------------------------------------------------------------------")
    print(f"{student_dic[k]['FirstName']} {student_dic[k]['LastName']}[{k}], Block1 : {student_dic[k]['Block1']}, Block2 : {student_dic[k]['Block2']}, Block3 : {student_dic[k]['Block3']}, Block4 : {student_dic[k]['Block4']}")
    print("------------------------------------------------------------------------------------------")
#Check password _ Done
def passwordCheck():
    #If it's already in admin mode, return true
    if adminActivate:
        return True
    else:
        password = input("Password: ")
        #Check if password matches adminPassword.
        if password == adminPassword:
            return True
        else:
            input("\nWrong password, bye!\nPress Enter to continue...")
            return False

##################################################################################################################################################################3
#Main while loop

#Get information/source from existing student roster/file if possible.
readFile()
#Clear terminal
os.system("cls")
print("------------------------------------------------------------------")
adminMode = input("Login as admin(a)\nLogin as user(b)\n------------------------------------------------------------------\n\nHow would you like to login? (a,b): ").lower()
#Login as admin
if adminMode == "a":
    password = input("What is the password?: ")
    #If password matches
    if password == adminPassword:
        adminActivate = True
    #If not
    else:
        input("\nWrong Password! you'll proceed as user\nPress Enter to continue...")
        adminActivate = False
#Login as user
elif adminMode.lower() == "b":
    adminActivate = False
#Invalid input
else:
    input("\nInvalid input! you'll proceed as user\nPress Enter to continue...")
    adminActivate = False


while True:
    #Clear terminal
    os.system("cls")

    print("------------------------------------------------------------------")
    user_input = input("|-Save file(a)\t\t\t|-Add student to a roster(b)\t|\n|-Remove student(c)\t\t|-Update student(d)\t\t|\n|-Exit(e)\t\t\t|-Print whole roster(f)\t\t|\n|-Print Student Schedule(g)\t|-Check Class List(h)\t\t|\n------------------------------------------------------------------\n\nChoose your task to do (a,b,c,d,e,f,g,h): ")


    #Write file (save file)
    if user_input.lower() == "a":
        writeFile()    
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
    #Print
    elif user_input.lower() == "f":
        printDict("print")
        input("\nPress Enter to continue...")
    #studentSchedule
    elif user_input.lower() == "g":
        studentSchedule()
    #Class List
    elif user_input.lower() == "h":
        classList()
    #Invalid
    else:
        input("Invalid input. Please try again...\n\nPress Enter to continue...")
        continue
##################################################################################################################################################################