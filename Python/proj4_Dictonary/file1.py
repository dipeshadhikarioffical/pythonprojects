import json
from difflib import get_close_matches


data = json.load(open("dict_data.json"))  # to read the json file

## to search the data in the file
def translate(word):
    word = word.lower()
   
    if word in data:   ## if data found take the result out
        return data[word]
    
    ## if input word is a title 1st letter caiptal and other letter small
    elif word.title() in data:
        return data[word.title()]
    
    ## if the input word is in upper letter
    elif word.upper() in data:
        return data[word.upper()]
    
    ## for close matches if similar word exits then it enters in this loop
    elif len(get_close_matches(word, data.keys())) > 0:
        print("did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("press y for yes or n for no")
        if decide == "y":
            return (" pugger your paws steps in wrong keys ")
        else:
            return (" you have enter wrong input please enter y or n : ")
    ## if  did not exits in file   
    else:
        print(" Please check the spelling the word you enter is wrong !!!! ")

word = input(" Enter the word you want to search: ")
output = translate(word)  # to take the result from json file
#print(output)
if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)
