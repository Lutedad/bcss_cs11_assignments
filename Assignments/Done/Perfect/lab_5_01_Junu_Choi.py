import os

AbbreviationDic = {"lol":"laughing out loud","ttyl":"Talk to you later","idk":"I don't know","wdym":"What do you mean","nvm":"Nevermind","lmk":"let me know","ty":"thank you"}

os.system("cls")
print("Welcome to Abbreviation dictionary!\nEnter in any abbreviation (small case or caps)\nType 'end' to exit the program")

end = True

while end:
    user_input = input("\n\nAbbreviation: ").lower()
    if user_input == "end":
        end = False
    else:
        print(user_input,":",AbbreviationDic.get(user_input,"not found, try again."))