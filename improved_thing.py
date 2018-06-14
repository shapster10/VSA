import random
import string
import time

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


#full
a = '   |----'
c = '   |---O'
d = '   |  -|-'
e = "   |  / \\"
f = '   |'
g = '___|_______'





c1 = '   |---'#empty
d1 = '   |  '#empty
e1 = "   |  "#empty


e2 = "   |  / "#one leg



d2 = '   |   |'#body
d3 = '   |  -|'#one arm

# print a
# print b
# print c
# print d1
# print e1
# print f
# print g


def stage(something):
    if something == '0':
        print c1
        print d1
        print e1
        print f
        print g
    elif something == '1':
        print a
        print c
        print d1
        print e1
        print f
        print g
    elif something == '2':
        print a
        print c
        print d2
        print e1
        print f
        print g
    elif something == '3':
        print a
        print c
        print d3
        print e1
        print f
        print g
    elif something == '4':
        print a
        print c
        print d
        print e1
        print f
        print g
    elif something == '5':
        print a
        print c
        print d
        print e2
        print f
        print g
    elif something == '6':
        print a
        print c
        print d
        print e
        print f
        print g
print





def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


name = raw_input("What is your name? ")
print "For keywords, type /help. For games, type 'guess' or 'rps' or 'calculator' for a calculator."
game = 0

name2 = name[0].upper() + name[1:].lower()









while game == game:

    greetings1 = ['Hello', 'Greetings', 'Salutations', 'Hi', 'Hola']
    rand1 = random.randint(0, 4)
    greetings2 = ['friend', 'fellow programmer', 'aquaintance', 'amigo', 'bro', name2]
    rand2 = random.randint(0, 5)
    greeting = greetings1[rand1] + ' ' + greetings2[rand2]





    y = raw_input(greeting + "! Enter something: ")
    y = y.lower()
    if y == 'hi':
        print 'bye'
    elif y== 'Charlie' or y == 'charlie':
        print 'is ded meme'



    elif y == '/help':
        print 'Keywords include: hi, calculator, hey bro, what are you, how, Charlie, are you going to take over the world, Brad, why,'
        print  ' Are you my friend, nothing, yes, how do i feel, stupid, i\'m sad, rps,'
        print  'can you feel emotion, is charlie a creator, game, guess, who is your creator, no, what, hey, random, ai,'
        print  ' is charlie a good programmer, cool, wow, operate, me, you, bye, kill, kill urself, rude, I hate you,'
        print  'or I\'m <insert your name>'


    elif y == 'Brad' or y == 'brad':
        print 'is better than charlie'
    elif y== 'why':
        print 'because'
    elif y == 'are you my friend':
         d = random.randint(0, 1)
         if d == 0:
             print('Ewww of couse not!')
         else:
             print 'Sure'
    elif y == 'nothing':
         print 'what'
    elif y== 'yes':
        print 'no bc you bad'
    elif y== 'stupid':
        print 'dumb kid'
    elif y == 'hello':
        print 'hi'
    elif y== "i'm sad":
        print "don't worry"
    elif y== "guess" or y == "Guess":
        print "Let's play a guessing game!"
        amount = raw_input("Choose a maximum number - ")
        on = 1
        limit = int(raw_input("Choose a guess limit - "))
        times = 1
        no = 0
        secret = random.randint(1, int(amount))
        print "I'm thinking of a number between 1 and " + str(amount) + ". Can you guess it?"
        print "Enter a number, or 'exit' to end the game. "
        while on == 1 and limit > 0:
            limit = int(limit) - 1
            guess = raw_input("")
            if guess == "exit":
                print
                on = 0
            else:
                if int(guess) > secret:
                    print "Too high!"
                elif int(guess) < secret:
                    print "Too low!"
                else:
                    print 'Congratulations, you guessed the number! You used ' + str(times) + ' guesses.'
                    no = 1
                    on = 0
            times = times + 1

        if limit == 0 and no == 0:
            print 'You ran out of guesses! The number was ' + str(secret)
    elif y == "I'm sad":
        print "don't worry"
    elif y == "im sad":
        print "don't worry"
    elif y == "Im sad":
        print "don't worry"
    elif y == 'no':
        print 'yes'
    elif y == 'hangman':
        wordlist = load_words()

        # your code begins here!
        word = choose_word(wordlist)
        str.lower(word)
        guesses = 6
        print
        print 'Welcome to hangman! I am thinking of a word with ' + str(len(word)) + " letters. You have six guesses."
        stage('0')
        x = 1
        y = 2
        z = 0
        wx = 0
        blank = '_ ' * len(word)
        print blank
        underscore = ['_ '] * len(word)
        listword = []
        for fg in range(0, len(word)):
            listword.append(word[fg])

        a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
        while x == 1 and guesses > 0:
            print 'Available options are: ' + str(a)
            guess = raw_input("Pick a letter and see if it's in my word! ")
            if guess in a:
                x = x
                a.remove(str(guess))
            else:
                print 'Pick a new letter. This is not a letter or has already been guessed.'
                # break

            if guess in word:
                print "Right guess."
                for letter in word:
                    if underscore[z] == guess:
                        z = z + 1

                for r in range(0, len(word)):
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
                stage(str(6 - guesses))
                if guesses == 0:
                    print 'YOU LOSE! NO MORE GUESSES ARE AVAILABLE.'
                    print "The word was " + word + "."
            if '_ ' not in underscore:
                print "CONGRAGULATIONS! YOU WON THE HARDEST GAME YOU'LL EVER PLAY."
                print "You guessed the word " + word + "."
                x = 0
    elif y == 'rps' or y== 'RPS':
        print "Hey " + str(name2) + ", let's play rock, paper, scissors!"
        x = 1
        while x == 1:
            ai = random.randint(1, 3)
            p1 = raw_input('Rock, Paper, or Scissors? Type "stop" to exit. ')
            if p1 == 'Rock' or p1 == 'rock':
                if ai == 1:
                    print 'You tie!'
                elif ai == 2:
                    print 'You lose!'
                elif ai == 3:
                    print 'You win!'
            elif p1 == 'Paper' or p1 == 'paper':
                if ai == 1:
                    print 'You win!'
                elif ai == 2:
                    print 'You tie!'
                elif ai == 3:
                    print 'You lose!'
            elif p1 == 'Scissors' or p1 == 'scissors':
                if ai == 1:
                    print 'You lose!'
                elif ai == 2:
                    print 'You win!'
                elif ai == 3:
                    print 'You tie!'
            elif p1 == 'stop':
                x = 0
                print
    elif y == 'what' or y == 'What':
        print 'ur dumb'
    elif y == 'hey' or y == 'Hey':
        print 'sup'
    elif y == 'random':
        print 'ask charlie he is the one making the game'
    elif y == 'ai' or y == 'Ai':
        print 'yep?'
    elif y == 'is charlie a good programmer':
        print "Yes, but a ded ded meme"
    elif y == 'cool':
        print "i know i am"
    elif y == "wow":
        print 'wow is right'
    elif y== "operate" or y == "Operate":
        print "operate on what"
    elif y == "me" or y == 'Me':
        print "but u bad"
    elif y == 'you' or y == 'You':
        print 'yeah im better than you'
    elif y == 'bye' or y == 'Bye':
        print 'see ya'
    elif y == 'kill' or y == 'Kill':
        print 'yourself'
    elif y == 'kill urself' or y == 'kill yourself':
        print 'yeah you should'
    elif y == 'rude' or y == 'you are rude':
        print 'and so what'
    elif y == 'i hate you':
        print 'same'
    elif y == 'is charlie a creator':
        print 'somewhat; hes a designer'
    elif y == 'who is your creator':
        print 'brad'
    elif y == 'I\'m ' + name or y == 'i\'m ' + name or y == 'Im ' + name or y == 'im ' + name:
        print 'I know...'
    elif y == 'how':
        print 'by doing'
    elif y == 'can you feel emotion':
        print 'I feel your emotion'
    elif y == 'how do i feel':
        print 'happy, confused, and utterly stupid'
    elif y == 'are you going to take over the world':
        print 'when i want to why not'
    elif y == 'what are you':
        print 'a god ai'
    elif y == 'game':
        print 'type rps for rock paper scissors or guess for a guessing game'
    elif y == 'hey bro':
        print "hey mate"
    elif y == 'calculator':

        first = raw_input('First number? ')
        op = raw_input('What operation? ')
        second = raw_input('Second number? ')
        if op == 'multiplication' or op == 'multiplication' or op == 'x' or op == '*' or op == 'times' or op == 'time':
            answer = float(first) * float(second)
        elif op == 'add' or op == 'plus' or op == 'addition' or op == '+':
            answer = float(first) + float(second)
        elif op == '-' or op == 'subtraction' or op == 'subtract' or op == 'minus' or op == "take away":
            answer = float(first) - float(second)
        elif op == 'divided by' or op == 'divided' or op == 'divide' or op == '/' or op == 'division':
            answer = float(first) / float(second)
        else:
            print("That's not an operator")
        print 'The answer is ' + str(answer) + '.'

    else:
        print 'so what'
# #
# #
# y = 1000
# while y == 1000:
#     x = raw_input("Enter a word")
#     print "ai says " + str(x)
