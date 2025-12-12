# #1 . Write a Python program to calculate the length of a string.
#
# a = "ritu_naruka"
# print(len(a))
#
# # 2
# # Reverse words in a given String in Python
#
# a = "ritu_naruka"
# reverse = a[::-1]
# print(reverse)
#
# # 3
# #change all charcter in uppercase in Python
# a = "ritu_naruka"
# b = a.upper()
# print(b)
#
# # 4#change all charcter in lowercase in Python
# string = "hello_WORLd"
# print(a.lower())
#
#
#
# #5 What is the character at index 0 in the string
# string = 'coding'
# first_char = string[0]
# print(first_char)
#
# # 6What is the last index of the string Coding
# string = "coding"
# last_char = string[-1]
# print(last_char)
#
# # 7What is the second index of the string Coding
# string = 'coding'
# second_char = string[1]
# print(second_char)
#
# #
# # 8# replace character in string
# string = 'coding'
# a = string.replace('o', 'g')
# print(a)
#
#
# #9remove one charater
# string = 'coding'
# a = string.replace('o','')
# print(a)
#
# # 10 add one new character in string
# string = 'coding'
# a= string + ' with me'
# print(a)
#
#
# # 1Count Words in a Sentence: Write a function that counts the number of words in a given sentence.
# str = "cosdinwithme"
# print(len(str))
#
# # 2Capitalize Each Word: Write a function that capitalizes the first letter of each word in a sentence.
# st = "coding with me"
# new = st.title()
# print(new)
#
# # 3Use index to determine the position of the first occurrence of o in Coding with me.
# string = "conding with me"
# position_of_c = string.index("o")
# print(position_of_c)
#
# #4 Cut(slice) out the first word of Coding with me string.
# str = "coding with me"
# remove_first = str[1:]
# print(remove_first)
#
# # 5 find  last word of Coding with me string.
#
# str = "coding with me"
# last_char = str[-1:]
# print(last_char)
#
#
#


# 1change all lower case latter to upper case
str = "ritunaruka"
a=str.upper()
print(a)


# 2change all upper case latter to lower case
str = "RITUNARuka"
lower = str.lower()
print(lower)

# 3change only title in upper case
str = 'ritu naruka'
title = str.title()
print(title)

#4 change upper case to lower case and lower case to upper case
str = "riTUnaRuKa"
swap = str.swapcase()
print(swap)


# 5 only covert first latter to upper case

str = 'ritu naruka'
capt = str.capitalize()
print(capt)


#6 count how many time 'i' is come in string
str = 'this is my phone'
new = str.count('p')
print(new)


# 7 check index
str  = 'ritu naruka'
index = str.index('u')
print(index)

# 8 replace character

str = 'ritu naruka'
replace_char = str.replace('u', 'a')
print(replace_char)


# 9startswith
str = 'ritu naruka'
start_from = str.startswith('r')
print(start_from)

# 10 print len of string

str = 'ritu naruka'
print(len(str))