# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

def get_partial_word(w, l):
    result = []
    for i in range(len(w)):
        if w[i] == l:
            result.append(l)
        else:
            result.append("-")
    return result

def update_alphabet(alphabet, letter):
    res = ""
    if letter in alphabet:
        res = alphabet.replace(letter, "")
    return res

def normalize_string(words):
    for i in range(len(words)-1):
        if words[i] == "-":
            del words[i] 
          
    return "".join(words)

aval_letters = "abcdefghijklmnopqrstuvwxyz"
num_guesses = 8
word = choose_word(wordlist)
print("Welcome to the game, Hangman!")
print("I am thinking of a word that is " + str(len(word)) + " letters long.")
print("-----------------------------------------------")
guess = ""
while(num_guesses > 0):
    print("You have " + str(num_guesses) + " guesses left.")
    print("Available letters: ", aval_letters)
    print("-----------------------------------------------")
    letter = raw_input("Please guess a letter:")
    num_guesses -= 1
    print word
    words = get_partial_word(word, letter)    
    guess = normalize_string(words)
    if guess == word:
        break
    aval_letters = update_alphabet(aval_letters, letter)
