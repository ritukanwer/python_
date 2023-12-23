
#1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

string1 = "thirty"
string2 = "days"
string3 = "of"
string4 = "python"
space = " "

string = string1 +space+ string2+space + string3+space + string4


print(string)


# 2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'
first_string = "coding"
second_string = "for"
third_string = "all"
space = " "

new_string = first_string +space + second_string +space + third_string
print(new_string.title())

#3Declare a variable named company and assign it to an initial value "Coding For All".
company = "coding for all"
print(company)

#4 Print the variable company using print().
company = "coding"
print(company)
print("company")

# 5 Print the length of the company string using len() method and print().
a = "company"
print(len(a))

# 6 Change all the characters to uppercase letters using upper() method.
a = "company"
print(a.upper())

# 7 Change all the characters to lowercase letters using lower() method.
a = "CompaNy"
print(a.lower())


# 8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
a = "ritu_naruka"
print(a.capitalize())
print(a.title())
a = "ritu NARuKa"
print(a.swapcase())

# 9 Cut(slice) out the first word of Coding For All string.
str = "coding for all"
slice_first = str[1:]
print(slice_first)

# 10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
a = "coding for all"
check = "coding"
print(a.index(check))
challenge = 'thirty days of python'


# 11 Replace the word coding in the string 'Coding For All' to Python.
str = "coding for all"
print(str.replace("coding","python"))


# 12Change Python for Everyone to Python for All using the replace method or other methods.
string = "python for everyone"
print(string.replace("everyone","all"))

# 13 Split the string 'Coding For All' using space as the separator (split()) .
string = "coding for all"
print(string.split())

# 14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(string.split(","))

# 15 What is the character at index 0 in the string Coding For All.
string = "coding for all"
first_index = string[0]
print(first_index)

# 16 What is the last index of the string Coding For All.
string = "coding for all"
last_index = string[-1]
print(last_index)

# 17 What character is at index 10 in "Coding For All" string.
string = "coding for all"
number_index = string[11]
print(number_index)

# 18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
string = "Python For Everyone"
new_string = ""
for i in string.split():
    new_string += i[0]
print(new_string)


# 19 Create an acronym or an abbreviation for the name 'Coding For All'.
string = "Coding For All"
new_str = ""
for i in string.split():
    new_str += i[0]
print(new_str)

# 20 Use index to determine the position of the first occurrence of C in Coding For All.
string = "conding for all"
position_of_c = string.index("c")
print(position_of_c)

# 21Use index to determine the position of the first occurrence of F in Coding For All.
string = "conding for all"
position_of_f = string.index("f")
print(position_of_f)

# 22Use rfind to determine the position of the last occurrence of l in Coding For All People.
str = "coding for all people"
position_of_l = str.rfind('l')
print(position_of_l)


# 23 Use index or find to find the position of the first occurrence of the word 'because' in
# the following sentence: 'You cannot end a sentence with because because because is
# a conjunction'

sentence = 'You cannot end a sentence with because because because is a conjunction'

position = sentence.find('because')

print(position)

# 24Use rindex to find the position of the last occurrence of
# the word because in the following sentence: 'You cannot end
# a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'

last_because = sentence.rindex("because")
print(last_because)


# 25 Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
sentence = "you cannot end a sentence with because because because in a conjunction"
because = sentence[31:54]
print(because)

# 26 Find the position of the first occurrence of the word 'because' in
# the following sentence: 'You cannot end a sentence
# with because because because is a conjunction
sentence = "you cannot end a sentence with because because because in a conjunction"
position = sentence.find('because')
print(position)

# 28
# Does ''Coding For All' start with a substring Coding?

str = "coding for all"
print(str.startswith("coding"))

# 29 Does 'Coding For All' end with a substring coding?
string  = "coding for all"
print(string.endswith("coding"))

# 30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
str ="coding for all"
print(str.strip())


# 31 Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python

challenge = '30DaysOfPython'
print(challenge.isidentifier())

challenge = 'thirty_days_of_python'
print(challenge.isidentifier())


# 32 The following list contains the names of some of python
# libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join
# the list with a hash with space string.

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
hash = "#  ".join(libraries)
print(hash)


#33 Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print("I am enjoying this challenge. \nI just wonder what is next.")

#34 Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# ritu  18     india   jaipur
print('name\tage\tcity\tcountry')
print('ritu\t18\tjaipur\tindia')


# 35 Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.

formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area)

print(formated_string)
# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

# a = 8
# b = 6
#
# print('{} + {} = {}'.format(a, b, a + b))
# print('{} - {} = {}'.format(a, b, a - b))
# print('{} * {} = {}'.format(a, b, a * b))
# print('{} / {} = {:.2f}'.format(a, b, a / b))
# print('{} % {} = {}'.format(a, b, a % b))
# print('{} // {} = {}'.format(a, b, a // b))
# print('{} ** {} = {}'.format(a, b, a ** b))
