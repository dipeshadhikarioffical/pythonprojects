import file1_hangmandeveloper

hangman = file1_hangmandeveloper.Hangman('C:\\Users\\DIPESH ADHIKARI\\PycharmProjects\\python\\Proj1_Hangman\\words.txt')
hangman.choose_the_word()   # calling the package from another file
hangman.fill_the_word_status()  # calling the package from another file

while True:
    hangman.get_word_status()  # calling the package from another file
    hangman.guess_the_letter()  # calling the package from another file

    if(hangman.attempts_remaining == 0):
        print("OUT OF ATTEMPTS. THE WORD WAS '{}'. GAME OVER !!!! ".format(hangman.chosen_word))
        break  # to exit from game

    elif (hangman.chosen_word == ''.join(hangman.word_status)):
        print("CONGRATULATION !!! YOU HAVE OWN THE GAME")
        break    # to exit from game
