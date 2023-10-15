

"""
question_121
Considering the code below, write code that prints out True! if the
 value associated with key number 5 is Perl or the number of key-value
  pairs in the dictionary divided by 5 returns a remainder less than 2.
   Otherwise, print out False!
"""
x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

if x[5] == 'perl' or len(x) % 5 < 2:
    print("true")

else:
    print("false")


"""
question_122
Considering the code below, write code that prints out 
True! if 3 is a key in the dictionary and the smallest value
 (alphabetically) in the dictionary is C#. Otherwise, print 
 out False!"""

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
if 3 in x and sorted(x.values())[0] == "C#":
    print("true")
else:
    print("false")


"""
question_123
Considering the code below, write code that prints out True! if the
 last character of the largest (alphabetically) value in the dictionary is n. Otherwise, print out False!"""

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
if sorted(x.values())[-1][-1] == "n":
    print('true')

else:
    print("false")

"""question_124
Considering the code below, write code that prints out True! if the largest key in the dictionary divided by the second
 largest key in the dictionary returns a remainder equal to the smallest key in the dictionary. Otherwise, print out False!"""

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
if sorted(x.keys())[-1] % sorted(x.keys())[-2] == sorted(x.keys())[0]:
    print("true")

else:
    ("false")


"""
question_125
Considering the code below, write code that prints out True! if the sum of all 
the keys in the dictionary is less than the number of characters of the string 
obtained by concatenating the values associated with the first 5 keys in the 
dictionary. Otherwise, print out False!
"""

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
if sum(x) > len(x[1] + x[2] + x[3] +x[4]+x[5]):
    print("true")

else:
    print("false")

"""question_126
Considering the code below, write code that prints out True! if the 3rd element
 of the first range is less than 2, prints out False! if the 5th element of the
  first range is 5, and prints out None! otherwise.
"""
x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]

if x[0][2] < 2:
    print("true")
elif x[0][4] == 5:
    print("false")
else:
    print("none")


"""
question_127
Considering the code below, write code that prints out True! if the 3rd element
 of the 3rd range is less than 6, prints out False! if the 1st element of the
  second range is 5, and prints out None! otherwise.


"""

x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]

if x[2][2] < 6:
    print("true")
elif x[1][0] == 5:
    print("false")
else:
    print("none")


"""
question_128
Considering the code below, write code that prints out True! if 
the last element of the first range is greater than 3, prints out 
False! if the last element of the second range is less than 9, and
 prints out None! otherwise."""

x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]
if x[1][-1] > 3:
    print("true")

elif x[2][-2]<9:
    print("false")

else:
    print("none")


"""
question_129
Considering the code below, write code that prints out True! if the 
length of the first range is greater than or equal to 5, prints out
 False! if the length of the second range is 4, and prints out None! otherwise."""
x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]
if len(x[0]) >= 5:
    print("true")
elif len(x[1]) == 4:
    print("false")

else:
    print("none")


"""
question_130
Considering the code below, write code that prints out True! if the sum of all
the elements of the first range is greater than the sum of all the elements of
the third range, prints out False! if the largest element of the second range
is greater than the largest element of the third range, and prints out None! otherwise.

"""

x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]
if sum(x[0]) > sum(x[1]):
    print("true")

elif max(x[1]) > max(x[2]):
    print("false")

else:
    print("none")



"""
question_131
Considering the code below, write code that prints out True! if the largest element of the first range minus the second 
element of the 3rd range is equal to the first element of the first range, prints out False! if the length of the first
 range minus the length of the 2nd range is equal to the first element of the 3rd range, prints out Maybe! if the sum 
 of all the elements of the 3rd range divided by 2 returns a remainder of 0, and prints out None! otherwise."""

x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]
if max(x[0]) - x[2][1] == x[1][0]:
    print("true")
elif len(x[0]) - len(x[1]) == x[2][0]:
    print("false")
elif sum(x[2]) %2 == 0:
    print("maybe")
else:
    print("nonee")


"""
question_132
Considering the code below, write code that prints out True! if the sum of the last 3 
elements of the first range plus the sum of the last 3 elements of the 3rd range is equal
 to the sum of the last 3 elements of the 2nd range, and prints out False! if the length of
  the first range times 2 is less than the sum of all the elements of the 3rd range."""


x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]
if sum(x[0][-3:]) + sum(x[2][-3:]) == sum(x[1][-3:]):
    print("true")

elif len(x[0]) * 2 < sum(x[2]):
    print("false")


"""question_133
Considering the code below, write code that prints out True! if the 2nd character
 of the value at key 1 is also present in the value at key 4, and prints out False! otherwise."""

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
if x[1][1] in x[4]:
    print("true")
else:
    print("false")

"""question_134
Considering the code below, write code that prints out True! if the second to last 
character of the value at key 3 is the first character of the value at key 5, and prints out False! otherwise."""
x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
if x[2][-2] == x[5][0]:
    print("True!")
else:
    print("False!")


"""
question_135
Considering the code below, write code that prints out True! if the number of characters 
of the smallest value in the dictionary is equal to the number of occurrences of letter a 
in the value at key 3, and prints out False! otherwise."""

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
if len(min(x.values())) == x[3].count("a"):

    print("true")
else:
    print("false!")










# loops
"""
question_136
Write a for loop that iterates over the x list and prints out all the elements of the list."""
x = [10, 12, 13, 14, 17, 19, 21, 22, 25]
for i in x:
    print(i)


"""
question_137
Write a for loop that iterates over the x list and prints out the remainders of each element of the list divided by 3.

"""
x = [10, 12, 13, 14, 17, 19, 21, 22, 25]
for i in x:
    print(i%3)

"""question_138
Write a for loop that iterates over the x list and prints out all the elements of the list in reversed order and multiplied by 10."""
x = [10, 12, 13, 14, 17, 19, 21, 22, 25]

for i in sorted(x, reverse = True):
    print(i * 10)


"""question_139
Write a for loop that iterates over the x list and prints out all the elements of the list divided by 2 and the string Great job! after the list is exhausted.
"""
x = [10, 12, 13, 14, 17, 19, 21, 22, 25]
for i in x:
    print(i / 2)
else:
    print("Great job!")

"""
question_140
Write a for loop that iterates over the x list and prints out the index of each element."""

x = [10, 12, 13, 14, 17, 19, 21, 22, 25]
for i in x:
    print(x.index(i))



"""
question_141
Write a while loop that prints out the value of x squared while x is less than or equal to 5. Be careful not to end up with an infinite loop!

"""
x = 0

while x <= 5:
    print(x ** 2)
    x = x + 1



"""
question_142
Write a while loop that prints out the value of x times 10 while x is less than or equal to 4 and then
 prints out Done! when x becomes larger than 4. Be careful not to end up with an infinite loop!"""
x = 0

while x <= 4:
    print(x * 10)
    x = x + 1
else:
    print("Done!")

"""
question_143
Write a while loop that prints out the value of x plus 10 while x is less than or 
equal to 15 and the remainder of x divided by 5 is 0. Be careful not to end up with an infinite loop!"""
x = 10

while x <= 15 and x % 5 == 0:
    print(x + 10)
    x = x + 1

"""
question_144
Write a while loop that prints out the absolute value of x while x is negative. Be careful not to end up with an infinite loop!"""
x = -7

while x < 0:
    print(abs(x))
    x = x + 1

"""question_145
Write a while loop that prints out the value of x times y while x is greater than or equal to 5 and less than 10, and prints out the result of x divided by y when x becomes 10. Be careful not to end up with an infinite loop!

"""
x = 5
y = 2

while x >= 5 and x < 10:
    print(x * y)
    x = x + 1
else:
    print(x / y)


"""question_146
Write code that will iterate over the x list and multiply by 10 only the elements that are greater than 20 and print them out to the screen."""

x = [10, 12, 13, 14, 17, 19, 21, 22, 25]
for i in x:
    if i > 20:
        print(i * 10)

"""
question_147
Write code that will iterate over the x and y lists and multiply each element of x with each element of y, also printing the results to the screen."""
x = [2, 4, 6]
y = [5, 10]
for i in x:
    for j in y:
        print(i * j)


"""question_148
Write code that will iterate over the x and y lists and multiply each element of x with each element of y that is less than 12, also printing the results to the screen.
"""

x = [2, 4, 6]
y = [5, 10]

for i in x:
    for j in y:
        print(i * j)


"""
question_149
Write code that will iterate over the x and y lists and multiply each element of x that is greater
 than 5 with each element of y that is less than 12, also printing the results to the screen."""

x = [2, 4, 6, 8]
y = [5, 10, 15, 20]

for i in x:
    for j in y:
        if i > 5 and j < 12:
            print(i * j)

"""
question_150
Write code that will iterate over the x and y lists and multiply each element of x with each element
 of y that is less than or equal to 10, also printing the results to the screen. For y's elements
  that are greater than 10, multiply each element of x with y"""

x = [2, 4, 6, 8]
y = [5, 10, 15, 20]

for i in x:
    for j in y:
        if j <= 10:
            print(i * j)
        else:
            print(i * j ** 2)

"""
question_151

Write code that will print out each character in x doubled if that character is also inside y"""

x = "cryptocurrency"
y = "blockchain"

for i in x:
    if i in y:
        print(i * 2)


"""
questiona_152
Write code that will iterate over the range generated by range(9) and for each element that is between 3
 and 7 inclusively print out the result of multiplying that element by the second element in the same range."""
my_range = range(9)

for i in my_range:
    if 3 <= i <= 7:
        print(i * my_range[1])


"""
question_153
Write code that will iterate over the range starting at 1, up to but not including 11, with a step of 2, and for each
 element that is between 3 and 8 inclusively print out the result of multiplying that element by the last element in 
 the same range. For any other element of the range (outside [3-8]) print Outside!"""

for i in range(1,11,2):
    if 3 <= i <= 8:
        print(i * range(1,11,2)[-1])
    else:
        print("Outside")

"""
question_154
Write code that will iterate over the range starting at 5, up to but not including 25, with a step of 5,
 and for each element that is between 10 and 21 inclusively print out the result of multiplying that element 
 by the second to last element of the same range. For any other element of the range (outside [10-21]) print
  Outside! Finally, after the entire range is exhausted print out The end!"""

for i in range(5,25,5):
    if 10 <= i <= 21:
        print(i * range(5,25,5)[-2])
    else:
        print("Outside")
else:
    print("The end")


"""question_155
Write a while loop that prints out the value of x times 11 while x is less than or equal to 11. 
 When x becomes equal to 10, print out x is 10! Be careful not to end up with an infinite loop!

"""

x = 5

while x <= 11:
    if x == 10:
        print("x is 10!")
        x = x + 1
    else:
        print(x * 11)
        x = x + 1


"""
question_156
Insert a break statement where necessary in order to obtain the following result:

1
1
100
20
10"""
x = [1, 2]
y = [10, 100]

for i in x:
    for j in y:
        if i % 2 == 0:
            print(i * j)
            break
        print(i)
    print(j)

"""question_157
Insert a break statement where necessary in order to obtain the following result:

1
10
20
2
10
"""

x = [1, 2]
y = [10, 100]

for i in x:
    for j in y:
        if i % 2 == 0:
            print(i * j)
        print(i)
        break
    print(j)


"""
question_158
Insert a break statement where necessary in order to obtain the following result:

1
1
100
10"""
x = [1, 2]
y = [10, 100]

for i in x:
    for j in y:
        if i % 2 == 0:
            break
            print(i * j)
        print(i)
    print(j)


"""
question_159
Insert a continue statement where necessary in order to obtain the following result:

1
1
100
20
200
100"""
x = [1, 2]
y = [10, 100]

for i in x:
    for j in y:
        if i % 2 == 0:
            print(i * j)
        print(i)
    print(j)


"""
Exercise 160 - Loops
Insert a continue statement where necessary in order to obtain the following result:

1
1
100
100"""

x = [1, 2]
y = [10, 100]

for i in x:
    for j in y:
        if i % 2 == 0:
            print(i * j)
        print(i)
    print(j)


"""
Exercise 161 - Exceptions
Fix the code below so that it doesn't generate a SyntaxError.


"""
x = [1, 2]
y = [10, 100]

for i in x:
    for j in y:
        if i % 2 == 0:
            print(i * j)


"""Exercise 162 - Exceptions
Fix the code below so that it doesn't generate a SyntaxError."""

x = [1, 2]
y = [10, 100]

for i in x:
    for j in y:
        if i % 2 == 0:
            print(i * j)

"""
Exercise 163 - Exceptions
Fix the code below so that it doesn't generate a NameError"""
x = [1, 2]
y = [10, 100]

for i in x:
    for j in y:
        if i % 2 == 0:
            print(i * j)

"""
Exercise 164 - Exceptions
Fix the code below so that it doesn't generate a TypeError."""
x = [1, 2]
y = [10, 100]

for i in x:
    for j in y:
        if i % 2 == 0:
            print(i * j)



"""
Exercise 165 - Exceptions
Fix the code below so that it doesn't generate an IndexError."""

x = [1, 2]
y = [10, 100]

for i in x:
    for j in y:
        if i % 2 == 0:
            print(x[1] * y[1])

"""question_167
Add the necessary clause(s) to the code below so that in case
 the ZeroDivisionError exception is raised then the program prints out Zero! to the screen.

"""

