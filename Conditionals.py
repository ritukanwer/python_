# question_111
# Considering the code below, write code that prints out True! if x has 50 characters or more.
x = "The days of Python 2 are almost over. Python 3 is the king now."
if len(x) >= 50:
    print('True')



# question_112
# Considering the code below, write code that prints out True! if x is a string and the first character in the string is T.
x = "The days of Python 2 are almost over. Python 3 is the king now."

if x.startswith("T"):
    print("True")

# question_113
# Considering the code below, write code that prints out True! if at least one of the following conditions occurs:

# the string contains the character z

# the string contains the character y at least twice


x = "The days of Python 2 are almost over. Python 3 is the king now."

if "z" in x or x.count("y") >= 2:
    print("True")



# question_114
# Considering the code below, write code that prints out True! if the index of the first occurrence of letter f is less
# than 10 and prints out False! if the same condition is not satisfied.


x = "The days of Python 2 are almost over. Python 3 is the king now."

if x.index("f") < 10:
    print("True")
else:
    print("False")


# question_115
# Considering the code below, write code that prints out True! if the last 3 characters of the string
# are all digits and prints out False! otherwise

x = "The days of Python 2 are almost over. Python 3 is the king now."

if x[-3:].isdigit():
    print("True")
else:
    print("False")


# question_116
# Considering the code below, write code that prints out True! if x has at least 8 elements and the element positioned at index
# 6 is a floating-point number and prints out False! otherwise.

x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]
if len(x) >= 8 and type(x[6]) is float:
    print("True")
else:
    print("False")

# question_117
# Considering the code below, write code that prints out True! if the second string of the first list in x ends
# with the letter h and the first string of the second list in x also ends with the letter h, and prints out False! otherwise.
x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]

if x[3][1].endswith("h") and x[7][0].endswith("h"):
    print("True!")
else:
    print("False!")


# question_118
# Considering the code below, write code that prints out True! if one of the following two conditions are satisfied and
# prints out False! otherwise.
#
# the third string of the first list in x ends with the letter h
#
# the second string of the second list in x also ends with the letter h
x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]

if x[3][2].endswith("h") or x[7][1].endswith("h"):
    print("True!")
else:
    print("False!")



# question_119
# Considering the code below, write code that prints out True! if the largest value among the first 3 elements of
# the list is less than or equal to the smallest value among the next 3 elements of the list. Otherwise, print out False!
x = [115, 115.9, 116.01, 109, 115, 119.5, ["length", "width", "height"]]

if max(x[:3]) <= min(x[3:6]):
    print("True")
else:
    print("False")

# question_120
# Considering the code below, write code that prints out True! if 115 appears at least once inside the list or if
# it is the first element in the list. Otherwise, print out False!
x = [115, 115.9, 116.01, 109, 115, 119.5, ["length", "width", "height"]]

if x.count(115) >= 1 or x.index(115) == 0:
    print("True")
else:
    print("False")

# question_121
# Considering the code below, write code that prints out True! if the value associated with key number 5 is Perl
# or the number of key-value pairs in the dictionary divided by 5 returns a remainder less than 2. Otherwise, print out False!

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

if x[5] == "perl" or len(x) % 5 < 2:
    print("True")
else:
    print("False")

# question_122
# Considering the code below, write code that prints out True! if 3 is a key in the dictionary and the smallest value
# (alphabetically) in the dictionary is C#. Otherwise, print out False!
x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}


if 3 in x and sorted(x.values())[0] == "C#":
    print("True")
else:
    print("False")

# question_123
# Considering the code below, write code that prints out True! if the last character of the largest (alphabetically)
# value in the dictionary is n. Otherwise, print out False!
x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

if sorted(x.values())[-1][-1] == "n":
    print("True")
else:
    print("False")

# question_124

# Considering the code below, write code that prints out True! if the largest key in the dictionary divided by the second largest key
# in the dictionary returns a remainder equal to the smallest key in the dictionary. Otherwise, print out False!

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

