#Introduction to Programming for Public Policy: Spring 2019
#Homework 2
#Due on GitHub classroom on Monday, 4/22 at 11:59pm

# Quesiton 1: Write a function that takes a string as its input, then returns that string reversed
# and turned into all lowercase characters. Then apply it to these three strings, collecting the
# results in a list.

string_1 = "That's what I do: I drink and I know things."
string_2 = 'Hold the door!'
string_3 = 'You know nothing, Jon Snow.'

def reverse_low(strings): # Function reverse & lower
    s = strings[::-1]
    result = ''.join(i.lower() for i in s)
    return result

list1 = [string_1, string_2, string_3] # create the list of strings
result_list = []
for string in list1:
    result_list.append(reverse_low(string))
print(result_list)

# Question 2: Write a function that takes a list of numbers as its input, then returns a dictionary
# with keys "length", "num_unique", "num_duplicates", and "sum", with the values being the length of
# the list, the number of unique items in the list, the number of duplicate items in the list, and
# the sum of all the values, respectively.  Display the result on this list:

my_list_1 = [1, 1, 2, 4, 8, 16, 16, 16, 16, 16]
def dictionary(lists):
    result = {"length": [], "num_unique": [], "num_duplicates": [], "sum": []} # create an empty dictionary
    length = len(lists)
    result["length"].append(length)
    # length of the list
    num_uni = len(set(lists))
    result["num_unique"].append(num_uni)
    # the number of unique items in the list
    num_dup = length - num_uni
    result["num_duplicates"].append(num_dup)
    # the number of duplicate items in the list
    s = 0
    for x in lists:
        s = s + x
    result["sum"].append(s)
    # the sum of all the values
    return result
dictionary(my_list_1)

# Question 3: Write a list comprehension that takes a list of numbers, and creates a new list made up
# of every other value from that list, doubled.  Display the result from this list:

my_list_2 = [1, 5, 2, 7, -4, 0, 33, 20, 45, 45, 2, 1, 5]
result_list_2 = [my_list_2[i] * 2 if i % 2 == 0 else my_list_2[i] for i in range(len(my_list_2))]
print(result_list_2)

# Question 4: Create a class called MyStringFixer.  Have it require an instance variable when created,
# which you will set to a string.  Then create three methods in this class that modify the string
# it was created with, returning the new string as a variable.  The exact modifications can be anything
# you like, as long as they modify the string and are different from each other.  Then create three
# instances of this class for each of the strings from question 1, and display the results of the
# methods you created (nine outputs in total).
import re
class MyStringFixer():
    def __init__(self, strings):
        self.str = strings

    def split(self):
        self.split = re.split(r'(?<=[\.\!\,\?\:])\s*', self.str) # split strings
        return self.split

    def lower(self):
        self.lower = ''.join(i.lower() for i in self.str) # lower strings
        return self.lower

    def reverse(self):
        self.reverse = ''.join(reversed(self.str)) # reverse strings
        return self.reverse
# Apply to three strings
x = MyStringFixer(string_1)
print(x.split())
print(x.lower())
print(x.reverse())

y = MyStringFixer(string_2)
print(y.split())
print(y.lower())
print(y.reverse())

z = MyStringFixer(string_3)
print(z.split())
print(z.lower())
print(z.reverse())
