#Set is one of 4 built-in data types in Python used to store collections of data
#The other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
def everyOtherLetter(sentence):
    msg =""
    for i in range(0,len(sentence)):
        if i % 2 == 0:
            msg += sentence[i]
        else:
            pass
    return msg

sentence = "I love learning Python!"

result = everyOtherLetter(sentence)
print( "result:"+ result )
