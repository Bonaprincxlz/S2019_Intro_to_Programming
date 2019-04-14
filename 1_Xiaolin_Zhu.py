# Intro to Programming for Public Policy
# Spring 2019
# - all sections -
# Homework 1 - due on GitHub by Monday 4/15 at midnight CST
# QUESTION 1: Use the following dictionary:

#https://stackoverflow.com/questions/4868904/what-is-the-origin-of-foo-and-bar
my_dict = {'foo':[1,2,3,4],
		   'bar':['a', 'b', 'c'],
		   'baz':['a', tuple([0, 0, 100]), set(['a', 'a', 'b', 'b']), [], True and False, 1==4]}
# a) Find and display the number of elements in the list under the 'foo' key.
print(my_dict['foo'])
print(len(my_dict['foo']))

# b) Find how many elements are in the object under the 'baz' key, at index location 2.  In comments explain why.
print(len(my_dict['baz'][2]))
# set refers to unordered collection of unique values

# c) Extract just the last two elements from the list under the 'baz' key.  In comments, explain why the result
#    is the values you see.
print(my_dict['baz'][-2:])
# True and False returns boolean False , 1 does not equal 4 boolean False

# d) Replace the first two elements in the object under the 'bar' key with 'dog' and 'cat'.
my_dict['bar'][:2] = ['dog', 'cat']

# e) Under the 'baz' key, at index location 1, replace the first two elements in the object with 'dog' and 'cat'.
#    In comments, explain the result.
my_dict['baz'][1][:2] = ['dog', 'cat']
# tuple is immutable

# f) Assign the value 'd' to index location 3 in the object under the 'bar' key.
my_dict['bar'].insert(3, 'd')
my_dict['bar']

# g) Find the mean and sum of the values under the 'foo' key.
import numpy as np
print(np.mean(my_dict['foo']))
print(np.sum(my_dict['foo']))


# QUESTION 2: Use the following string:

my_string = 'Hello how are  you?  do you like coffee?  because if youre going to write code, you pretty much have to.'

# a) Fix the missing apostrophe in "youre"
my_string1 = my_string.replace("youre", "you're")
my_string1

# b) This string has some double spaces in it.  Write one solution that turns them into single spaces that only applies
#    to this sentence, and one solution that is generalized to remove double spaces from any string.
mystring2 = my_string.replace("  ", " ")
mystring2

# Generalized solution
def clean_dspace(strings):
    while '  ' in strings:
        strings = strings.replace('  ', ' ')
    return strings

clean_dspace(my_string1)

# c) Split this string into a list of unique sentences.
my_string3 = clean_dspace(my_string1)
import re
split_string = re.split(r'(?<=[\.\!\?])\s*', my_string3)
# reference:
# https://stackoverflow.com/questions/44244583/python-splitting-on-regex-without-removing-delimiters

# d) Two sentences are missing capitalization at the start.  Write two solutions, one that fixes only this string, and
#    one that is generalized to fix missing capitalization at the start of sentences for any string containing them.
# For the string
cap_string = ' '.join(s[:1].upper() + s[1:] for s in split_string)

# Function
def caps(strings):
    str1 = re.split(r'(?<=[\.\!\?])\s*', strings)
    result = ' '.join(s[:1].upper() + s[1:] for s in str1)
    return result

# QUESTION 3: Use the following list:

my_list = [1, 2, 3, 8, 9, 101, 102, 45, 73, 1000]

# a) Loop over the values in this list, and print a sentence saying which value is at each index location.
#    e.g. "55 is at index 4" followed by "10 is at index 5" and so on.
for i in range(len(my_list)):
    print(my_list[i], "is at index", i)

# b) Print the sum, mean, median, max and min values of the list.  The first time, loop over each value one at a time
#    and use conditional statements to figure out the answers.  The second time use the NumPy library.
# sum
addup = 0
for i in range(len(my_list)):
    addup = addup + my_list[i]
print(addup)

# mean
s = 0
j = 0
mean = ' '
for i in range(len(my_list)):
    s = s + my_list[i]
    j = j + 1
    mean = s / j
print(mean)

# median
my_list.sort()
p = len(my_list)
s = p//2
if p % 2 == 0:
    print('median is', (my_list[s-1] + my_list[s])/2)
else:
    print('median is', my_list[s])

# max
maxi = my_list[0]
i = 0
while i < len(my_list):
    if maxi < my_list[i]:
        maxi = my_list[i]
    i = i + 1
print('max is', maxi)

# min
mini = my_list[0]
i = 0
while i < len(my_list):
    if mini > my_list[i]:
        mini = my_list[i]
    i = i + 1
print('min is', mini)

# numpy
import numpy as np
print(np.max(my_list))
print(np.min(my_list))
print(np.mean(my_list))
print(np.median(my_list))
print(np.sum(my_list))

# c) In a way that generalizes to any list of numbers, print the number of entries that are greater than or equal to 100.
def count_100(lists):
    j = 0
    for i in range(len(lists)):
        if lists[i] >= 100:
            j = j+1
    return j
