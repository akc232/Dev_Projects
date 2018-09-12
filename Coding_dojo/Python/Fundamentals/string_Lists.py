# Find and Replace
# In this string: words = "It's thanksgiving day. It's my birthday,too!" print the position of the first instance of the word "day". Then create a new string where the word "day" is replaced with the word "month".
#
words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")
new_words = words.replace("day", "month")
print new_words

# Min and Max
# Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.
#
x = [2,54,-2,7,12,98]
print min(x)
print max(x)


# First and Last
# Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list. Your code should work for any list.
#
x = ["hello",2,54,-2,7,12,98,"world"]

print x[0], x[len(x)-1]
