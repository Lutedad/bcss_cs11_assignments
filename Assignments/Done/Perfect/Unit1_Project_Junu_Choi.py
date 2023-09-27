#Intro to Madlibs Game
print("\nWelcome to the game :)\nLet's build a story together!")


#Questions to set variables (answers).
print('---------------------------------------------------------\n')
fav_person = input("Enter your favorite person: ")
fav_food = input("Enter your favorite food: ")
current_feelings = input("Enter your current_feelings: ")
adverb = input("Enter an adverb: ")
adjective_1 = input("Enter an adjective : ")
parent = input("Enter one of your parents : ")
weather = input("Enter current weather : ")
noun = input("Enter a noun : ")
verb = input("Enter a verb : ")
facial_expression = input("Enter a facial expression : ")
adjective_2 = input("Enter an adjective : ")
print('''\n\nThat's all you have to answer!\nNow, let's take a look at your unique story.\n---------------------------------------------------------''')
#----------------------------------------------------------------------------
#The story starts. 
print(f'''It was a {weather} day in the city.
The unknown person was approaching my {fav_person}.
Suddenly I felt uncomfortable even though nothing was {current_feelings}.
The person was holding a {adjective_1} {fav_food}.
My {fav_person} without a single {noun}, told me to {verb} as fast as I could.
I instinctively reacted with a big {facial_expression}.
The person was my {parent}! {parent} surprised us with {adjective_1} {fav_food} 😊.
{fav_person} just tried to eat that whole {fav_food} without me -_-!
THE END
''')
#Program ends!