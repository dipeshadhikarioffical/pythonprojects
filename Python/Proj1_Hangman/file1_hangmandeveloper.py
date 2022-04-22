
# if rectangular cursor key comes then press 'insert' key
# create project on python package or in directory .. this is created on directories
# if import not supported then right click on folder and go to 'mark as' then click on source root

import random  # to generate random words
import re   # regular expression module


class Hangman:
    # to take word from file
    def __init__(self, wordlist):   # wordlist is the place through which system take different word
        self.wordlist = wordlist
        self.attempts_remaining = 6  # how much time user can try to play in one game
        self.current_letter = ''     # to know which is the current letter in the game
        self.chosen_word = ''        # which word is given as a input by player
        self.guessed_letters = []

    #  to choose the word by system
    def choose_the_word(self):
        file = open(self.wordlist)  # to open words.txt file by system
        words = file.read().split('\n')    # to read each line of word file
        word_count = len(words)     # to count the length of selected word

        self.chosen_word = words[random.randrange(0, word_count)]

        print(self.chosen_word)  # to know which word is selected by system

        # self is used so that system can choose own self
        # random.randrange is used to select any random word and to give to system
        # self.word_status = '-'*len(self.chosen_word)  # to given - acc to all word length
        self.word_status = ['-' for i in range(len(self.chosen_word))]  # making to come in list

    # to fill the blank space by player
    def fill_the_word_status(self):
        nos = random.randrange(1, 3)  # 1 up to 3 is the letter which is filled by system
        for i in range(nos):
            position = random.randrange(0, len(self.chosen_word))
            self.word_status[position] = self.chosen_word[position]

    #  input given by the player
    def guess_the_letter(self):
        letter = input("GUESS THE LETTER: ")
        if (letter in self.guessed_letters) :
            print("YOU HAVE ALREADY GUESSED THAT LETTER.YOUR GUESS LETTERS: {}".format(','.join(self.guessed_letters)))
            return

        self.guessed_letters.append(letter)
        # to know input given by player exist in the word or not is multiple word present fill in all position
        occurrences = []
        occurrence = re.finditer(letter, self.chosen_word)  # finditer: to know where the word matching at which place
        for m in occurrence:
            occurrences.append(m.start())  # to put in the find position

        if(len(occurrences) == 0):
            self.attempts_remaining -= 1   # if no input given then attempt turn will decrease
            print("OOPS YOUR GUESS WAS WRONG. YOUR ATTEMPTS REMAINING IS {}".format(self.attempts_remaining))
        else:
            for position in occurrences:
                self.word_status[position] = self.chosen_word[position]
            print(" YOU HAVE GUESSED THE CORRECT WORD ")

    #  to show filled part and unfilled part or to show the game
    def get_word_status(self):
        print("CURRENT STATUS: {}\n".format(''.join(self.word_status)))  # join: to remove the list format
