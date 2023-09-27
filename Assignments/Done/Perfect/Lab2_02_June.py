#Can I be president?

#Getting inputs
age = int(input("How old are you?: "))
resident_of_US = int(input("How long have you stayed in America?: "))
natural_born = input("Are you a natural born citizen? yes/no: ")

#Prints whether the person is qualified to be a president or not in True|False.
print(age >= 35 and resident_of_US>=14 and natural_born == "yes")

#------------------------------------------------------------------------------------------

#Can I ride the roller coaster?

#Getting inputs
age_2 = int(input("How old are you?: "))
height = input("Are you taller than 50 inches? yes/no: ")
cost = int(input("How much quaters do you have?: "))
rider_pass = input("Do you have a frequent rider pass? yes/no: ")

#Prints whether the person is qualified to ride a roller coaster or not in True|False
print(  (age_2 >= 18 or height == "yes") and ((cost >= 2 and rider_pass =="yes") or cost >= 4))

#------------------------------------------------------------------------------
