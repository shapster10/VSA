# coding=utf-8
# Name:
# Date:

"""
proj04

practice with lists

"""

# #Part I
# #Take a list, say for example this one:
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# #and write a program that prints out all the elements of the list that are less than 5.
# op_list = [1, 1, 2 , 3, 5]
# for x in a:
#     if x < 5:
#         print x




#Part II
# Take two lists, say for example these two:
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that creates and prints a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
for item in b:
    for Item in c:
        if item == Item:
            print [Item]
#Part III
# Take a list, say for example this one:

# d = ["b", "a", "f", "y", "a", "t", "_", "p", "a", "R"]
# # and write a program that replaces all “a” with “*”.
# x = 0
# for a in d:
#     if d[x] == 'a':
#         d[x] = '*'
#     x = x + 1
# print d









#Part IV
#Ask the user for a string, and print out whether this string is a palindrome or not.

j = 1
while j == 1:
    y = raw_input("give me a string and I will tell you if it is a palindrone or not: ")
    y = y.lower()
    z = []
    x = 0
    q = 1
    for lol in range(0,len(y)):
        if y[x] != " ":
            z.append(y[x])
        x = x + 1
    for pal in range(0,len(z)/2):
        if z[0] == z[-1]:
            z = z[1:-1]
        else:
            q = 0
    if q == 0:
        print 'We dont have a palindrome'
    else:
        print 'This is a palindrome! Good job'









