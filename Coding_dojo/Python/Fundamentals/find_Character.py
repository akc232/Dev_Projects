# Assignment: Find Characters
# Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.
#
# Here's an example:
#
# # input
word_list = ['hello','world','my','name','is','Anna']
# char = 'o'
# # output
# new_list = ['hello','world']

def find_character(list, char):
    new_list=[]
    for i in range(0, len(list)):
        print list[i]
        if list[i].find(char) != -1:
            new_list.append(list[i])
    print new_list

find_character(word_list, "a")
