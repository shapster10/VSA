import random
name = raw_input("What is your name? ")
print "For keywords, type /help. For games, type 'guess' or 'rps'."
game = 0

for x in range(1,201):
    y = raw_input('Enter something: ')
    if y == 'hi':
        print 'bye'
    elif y== 'Charlie' or y == 'charlie':
        print 'is ded meme'



    elif y == '/help':
        print 'Keywords include: hi, Charlie, Brad, why, Are you my friend, nothing, yes, stupid, i\'m sad, game, Game, no, what, hey, random, ai, is charlie a good programmer, cool, wow, operate, me, you, bye, kill, kill urself, rude, I hate you, or I\'m <insert your name>'







    elif y == 'Brad' or y == 'brad':
        print 'is better than charlie'
    elif y== 'why':
        print 'because'
    elif y== 'Are you my friend':
         print 'no'
    elif y == 'nothing':
         print 'what'
    elif y== 'yes':
        print 'no bc you bad'
    elif y== 'stupid':
        print 'dumb kid'
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
    elif y == 'rps' or y== 'RPS':
        print "Hey " + str(name) + ", let's play rock, paper, scissors!"
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
    elif y == 'I\'m ' + name or y == 'i\'m ' + name or y == 'Im ' + name or y == 'im ' + name:
        print 'I know...'
    else:
        print 'so what'
# #
# #
# y = 1000
# while y == 1000:
#     x = raw_input("Enter a word")
#     print "ai says " + str(x)
