# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.
#
# Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.
#

mix_list = ['magical unicorns',19,'hello',98.98,'world']
num_list = [2,3,1,7,4,12]
str_list = ['magical','unicorns']



def type_list(list):
    new_str =""
    total = 0

    for value in list:
        if isinstance(value, int) or isinstance(value, float):
            total += value
        elif isinstance(value, str):
            new_str += value

    if new_str and total:
        print new_str
        print total

    elif new_str:
        print new_str
    elif total:
        print total


print type_list(mix_list)
