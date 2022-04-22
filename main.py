from random import randint

word_list = ("eis", "baum", "erdbeere", "zebra", "hund", "wassermelone")
active_word = None
anonymised_word = None
guesses_counter = 0

def anonymise_word(active_word):
    return '*' * len(active_word)


def choose_random_word():
    return word_list[randint(0, len(word_list) - 1)]


def print_hangman():
    if guesses_counter == 1:
        print("Oops - wrong guess:")
        print()
        print("__|__")
    elif guesses_counter == 2:
        print("Oops - wrong guess:")
        print("  |  ")
        print("  |  ")
        print("  |  ")
        print("  |  ")
        print("  |  ")
        print("  |  ")
        print("__|__")
    elif guesses_counter == 3:
        print("Oops - wrong guess:")
        print("  _____________  ")
        print("  |  ")
        print("  |  ")
        print("  |  ")
        print("  |  ")
        print("  |  ")
        print("  |  ")
        print("__|__")
    elif guesses_counter == 4:
        print("Oops - wrong guess:")
        print("  _____________  ")
        print("  |           |")
        print("  |         |   |")
        print("  |          ---")
        print("  |  ")
        print("  |  ")
        print("  |  ")
        print("__|__")
    elif guesses_counter == 5:
        print("Oops - wrong guess:")
        print("  _____________  ")
        print("  |           |")
        print("  |         |   |")
        print("  |          ---")
        print("  |           |")
        print("  |           |")
        print("  |  ")
        print("__|__")
    elif guesses_counter == 6:
        print("6 guesses are over. Sorry - You loosed!")
        print("  _____________  ")
        print("  |           |")
        print("  |         |   |")
        print("  |          ---")
        print("  |           |")
        print("  |          / \\")
        print("  |             ")
        print("__|__")


def check_choosenChar(choosen_char):
    global anonymised_word
    global guesses_counter
    new_anonymised_word = ""
    for i in range(len(active_word)):
        if active_word[i] == choosen_char:
            new_anonymised_word += choosen_char
        elif anonymised_word[i] != '*':
            new_anonymised_word += anonymised_word[i]
        else:
            new_anonymised_word += '*'

    if new_anonymised_word == active_word:
        anonymised_word = new_anonymised_word
        print(f'Congrats! - you guessed the right word: {active_word}')
    elif anonymised_word == new_anonymised_word:
        guesses_counter = guesses_counter + 1
        print_hangman()
    else:
        anonymised_word = new_anonymised_word


def start_game():
    global active_word
    global anonymised_word
    global guesses_counter
    active_word = choose_random_word()
    anonymised_word = anonymise_word(active_word)
    while guesses_counter < 6 and "*" in anonymised_word:
        print(anonymised_word)
        choosen_char = str(input("Please choose a character:"))
        check_choosenChar(choosen_char)


start_game()
