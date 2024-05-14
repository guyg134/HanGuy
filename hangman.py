import os 

# Constants
MAX_TRIES = 6
HANGMAN_PHOTOS = {1 : "x-------x", 2 : """        x-------x
        |
        |
        |
        |
        |""", 3 : """        x-------x
        |       |
        |       0
        |
        |
        |""", 4 : """        x-------x
        |       |
        |       0
        |       |
        |
        |""", 5 : """        x-------x
        |       |
        |       0
        |      /|\\
        |
        |""", 6 : """        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |""", 7 : """        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |"""}

HANGMAN_ASCII_ART="""                                      
    .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------. 
    | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
    | |  ____  ____  | || |      __      | || | ____  _____  | || |    ______    | || | _____  _____ | || |  ____  ____  | |
    | | |_   ||   _| | || |     /  \     | || ||_   \|_   _| | || |  .' ___  |   | || ||_   _||_   _|| || | |_  _||_  _| | |
    | |   | |__| |   | || |    / /\ \    | || |  |   \ | |   | || | / .'   \_|   | || |  | |    | |  | || |   \ \  / /   | |
    | |   |  __  |   | || |   / ____ \   | || |  | |\ \| |   | || | | |    ____  | || |  | '    ' |  | || |    \ \/ /    | |
    | |  _| |  | |_  | || | _/ /    \ \_ | || | _| |_\   |_  | || | \ `.___]  _| | || |   \ `--' /   | || |    _|  |_    | |
    | | |____||____| | || ||____|  |____|| || ||_____|\____| | || |  `._____.'   | || |    `.__.'    | || |   |______|   | |
    | |              | || |              | || |              | || |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
    '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' """


def check_valid_input(letter_guessed, old_letters_guessed):
    """check if the input is valid.
    :param base: letter_guessed - the letter that the user guessed
    :param base: old_letters_guessed - list of the letters that the user guessed
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True if the input is valid, False otherwise
    :rtype: bool"""
    #if the input is not a letter or the letter is already guessed return False
    if len(letter_guessed) > 1 or not letter_guessed.isalpha() or letter_guessed in old_letters_guessed:
        return False
    return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """update the list of the guessed letters if the input is valid.
    :param base: letter_guessed - the letter that the user guessed
    :param base: old_letters_guessed - list of the letters that the user guessed
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True if the input is valid, False otherwise
    :rtype: bool"""
    #if the input is valid add the letter to the list and return True
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed += letter_guessed
        return True
    #if the input is not valid print X and the list of the guessed letters and return False
    print("X")
    print(print_list_format(old_letters_guessed))
    return False

def print_list_format(list):
    """print the list in the format of -> between the letters.
    :param base: list - list of the letters that the user guessed
    :type list: list
    :return: the list in the format of -> between the letters
    :rtype: str"""
    output = ' -> '.join(list[::2] + list[1::2])
    return output

def show_hidden_word(secret_word, old_letters_guessed):
    """print the secret word with the guessed letters.
    :param base: secret_word - the secret word
    :param base: old_letters_guessed - list of the letters that the user guessed
    :type secret_word: str
    :type old_letters_guessed: list
    :return: the secret word with the guessed letters
    :rtype: str"""
    hidden_word = ""
    #for each letter in the secret word
    for letter in secret_word:
        #if the letter is in the list of the guessed letters add the letter to the hidden word
        if letter in old_letters_guessed:
            hidden_word += letter
        #if the letter is not in the list of the guessed letters add _ to the hidden word
        else:
            hidden_word += '_ '
    #return the hidden word
    return hidden_word

def check_win(secret_word, old_letters_guessed):
    """check if the user guessed the secret word.
    :param base: secret_word - the secret word
    :param base: old_letters_guessed - list of the letters that the user guessed
    :type secret_word: str
    :type old_letters_guessed: list
    :return: True if the user guessed the secret word, False otherwise
    :rtype: bool"""
    #for each letter in the secret word
    for letter in secret_word:
        #if the letter is not in the list of the guessed letters return False
        if letter not in old_letters_guessed:
            return False
    #if all the letters in the secret word are in the list of the guessed letters return True
    return True

def print_hangman(num_of_tries):
    """print the hangman photo.
    :param base: num_of_tries - the number of tries that the user has left
    :type num_of_tries: int"""
    
    #print the hangman photo
    print(HANGMAN_PHOTOS[num_of_tries])

def choose_word(file_path, index):
    """choose a word from the file.
    :param base: file_path - the path of the file with the words
    :param base: index - the index of the word in the file
    :type file_path: str
    :type index: int
    :return: the word in the index
    :rtype: str"""
    #open the file 
    words_file = open(file_path, 'r')
    #read the words from the file and split them to a list of words
    words_list = words_file.read().split()
    words_count = len(words_list)
    #close the file
    words_file.close()
    #return the word in index % number of words in the list
    return words_list[(index - 1) % words_count]

def welcome(MAX_TRIES):
    """print the welcome message.
    :param base: MAX_TRIES - the number of tries that the user has
    :type MAX_TRIES: int"""
    #print the welcome message
    print(HANGMAN_ASCII_ART, '\n')
    print("Welcome to HanGuy! Guess the secret word by entering one letter at a time. You have " + str(MAX_TRIES) + " tries. Good luck!\n")

def get_secret_word():
    """get the secret word from the user.
    :return: the secret word
    :rtype: str"""
    #input of the path of the file while the path is not valid
    file_path = input("enter the path of the file with words: ")
    while not os.path.isfile(file_path):
        file_path = input("not valid path, try enter again: ")
    
    #input of the index of the word while index is not digit or less than 1
    word_index = input("enter the index of the word: ")
    while not word_index.isdigit():
        word_index = input("not valid index, try enter again: ")

    word_index = int(word_index)
    #return the secret word
    return choose_word(file_path, word_index)

def main():

    mistakes = 0
    old_letters_guessed = []

    #print welcome 
    welcome(MAX_TRIES)
    #get the secret word
    secret_word = get_secret_word()
    #print the hangman photo and the hidden word
    print_hangman(1)
    print(show_hidden_word(secret_word, old_letters_guessed))

    #while the user has tries
    while mistakes < MAX_TRIES:
        #input of letter
        letter_input = input("enter letter: ")

        #clear the screen
        os.system('cls')

        #validation of the letter input
        if not try_update_letter_guessed(letter_input, old_letters_guessed):
            continue
        
        #if the letter is not in the secret word add 1 to the mistakes and print the hangman photo 
        if  letter_input not in secret_word:
            mistakes += 1
            print_hangman(mistakes + 1)

        #print the number of tries left, the hidden word
        print("tries left: " + (str)(MAX_TRIES - mistakes))
        print(show_hidden_word(secret_word, old_letters_guessed))
        #if the user guessed the secret word print WIN and break
        if check_win(secret_word, old_letters_guessed):
            print("WIN")
            break

    #if the user didn't guess the secret word print LOSE
    if mistakes == MAX_TRIES:
        print("LOSE")
    #print the secret word
    print("the secret word is: " + secret_word + "\n")

if __name__ == "__main__":
    main()
