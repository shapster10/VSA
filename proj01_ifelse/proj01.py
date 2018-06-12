# Name:
# Date:

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
#Then, it prints out a sentence that says the number of years until they graduate.
#print 'hello there!'
#Name= raw_input("What's your name?")
#Grade= int(raw_input('What grade are you in?'))
#print 'your name is ' + str(Name) + ' and you are in ' + str(Grade) + ' grade so you will graduate in ' +  str(13-Grade)+' years'
#Name = Name[0].upper() + Name[1:20] .lower()
#print Name

# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday
Current_Month=6
Current_Day=12
name= raw_input('Enter your name:')
Birth= raw_input('Enter your birth month:')
Day= raw_input('Enter your birth day:')
if int(Birth) >= 6:
    print "Your birthday is in " + str(int(Birth)-int(Current_Month)) + ' months'
else:
    print 'Your birthday is in ' + str(12-(Current_Month - int(Birth))) + ' months'
if int(Day) >=12:
    print 'Your birthday is in ' + str(Day-Current_Day) + 'days'
else:
    print 'Your birthday is in ' + str(30-(Current_Day- int(Day))) + ' days'
# If you complete extensions, describe your extensions here!