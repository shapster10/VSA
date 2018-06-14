# Name:
# Date:


# proj05: Hangman

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
import time
# your code begins here!
word = choose_word(wordlist)
str.lower(word)
guesses = 6
print 'Welcome to hangman! I am thinking of a word with ' + str(len(word)) + " letters. You have six guesses."
x = 1
y = 2
z = 0
wx = 0
blank = '_ ' * len(word)
print blank
underscore = ['_ '] * len(word)
listword = []
for fg in range(0,len(word)):
    listword.append(word[fg])

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while x == 1 and guesses > 0:
    print 'Available options are: ' + str(a)
    guess = raw_input("Pick a letter and see if it's in my word! ")
    if guess in a:
        x = x
        a.remove(str(guess))
    else:
        print 'Pick a new letter. This is not a letter or has already been guessed.'
        #break


    if guess in word:
        print "Right guess."
        for letter in word:
            if underscore[z] == guess:
                z = z + 1

        for r in range(0,len(word)):
            if guess == word[r]:
                del underscore[r]
                underscore.insert(r, str(guess) + ' ')
        blank = ''
        for df in range(0, len(word)):
            blank = blank + underscore[df]
        print blank
        z = 0
    else:
        print 'Wrong guess.'
        guesses = int(guesses) - 1
        print str(int(guesses)) + ' guesses left.'
        if guesses == 0:
            print 'YOU LOSE! NO MORE GUESSES ARE AVAILABLE.'
            print "The word was " + word + "."
    if '_ ' not in underscore:
        print 'CONGRAGULATIONS! YOU WON THE HARDEST GAME YOULL EVER PLAY.'
        print "You guessed the word " + word + "."
        x = 0