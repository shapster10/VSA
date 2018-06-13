# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
game = 1

play = raw_input("Lets play a guessing game, press enter to play or type 'EXIT' to end game.")
if play != "EXIT":
    limit = int(raw_input('Choose a guess limit:'))
    if limit == 1:
        limit = limit + 1
        print "Set to minimum of 2"
    elif limit < 1:
        print "Set to minimum of 2"
        limit = 2
    elif limit > 30:
        print "Set limit to maximum of 30"
    x = int(raw_input("Choose a bottom number:"))
    y = int(raw_input("Choose a top number:"))
    if x > y:
        print "Set numbers to default of 1 and 100"
        x = 1
        y = 100
    elif x == y:
        print "Set numbers to default of 1 and 100"
        x = 1
        y = 100
    print "I am thinking of a number between " + str(x) + " and " + str(y) + "."
    import random
    rnum = random.randint(x, y)

    while game == 1 and limit > 0:
        limit = int(limit) - 1
        guess = raw_input("Guess a number or enter 'EXIT' to exit the game:")
        if guess == "Exit" or guess == "exit" or guess == "EXIT" or guess == "EXit" or guess == "EXIt" or guess == "eXit" or guess == "eXIt" or guess == "eXIT":
            game = 0
        else:
            if limit == 0:
                print 'You ran out of guesses. Game over. The number was. ' + str(rnum)
            else:
                if int(guess) > y:
                    print "That is not an option."
                elif int(guess) < x:
                    print "That is not an option."
                elif int(guess) > rnum:
                    print 'Your answer is too high!'
                elif int(guess) < rnum:
                    print 'Your answer is too low!'
                else:
                        print "Congragulations you got the number."
                        game = 0
else:
    print "Goodbye."

