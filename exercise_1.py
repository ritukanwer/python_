#
#
#
#

#
#
#
#
#
#  # Given the code below, insert the correct positive index on line 3 in order to return the comma character from the string.
#
#
# # question_2
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
#
# print(my_string[7])
#
#
#
#
#
#
# #QUESTION_3
# # Given the code below, insert the correct negative index on line 3 in order to return the w character from the string.
#
#
#
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
#
# print(my_string[-10])
#
#
#
#
#
#
# # question_4
# # Given the code below, insert the correct method on line 3 in order to return the index of the B character in the string.
#
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
# def check_character(my_string):
#     check = "B"
#     str = " "
#     for i in my_string:
#         if "B" in i:
#             print('yes')
#         else:
#             ("no")
#             str.join(i)
#     return str
# print(check_character(my_string))

#
#
# # question_8
#
# # # Given the code below, insert the correct method on line 3 in order to check of the string starts with the letter X
# #
# #
# # my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
# # def check_elements(my_string):
# #     check = 'X'
# #     res = " "
# #     for i in my_string:
# #
# #         if  "X" in i:
# #             print('true')
# #         else:
# #             print("False")
# #             res.join(i)
# #     return res
# # print(check_elements(my_string))
#
#
# # question_9
#
# # Given the code below, insert the correct method on line 3 in orderto convert all uppercase
# # letters to lowercase and all lowercase letters to uppercase.
#
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
# def upper_to_lower_and_lower_to_uper(my_string):
#     string = my_string.swapcase()
#     return string
#
# print(my_string.swapcase())
#
#
# # question 10
# # Given the code below, insert the correct method on line 3 in order to remove all spaces (single Space characters from the keyboard)
# # from the string.
# # # #
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
#
# def replace_character(my_string):
#    string = my_string.replace("i", "btc")
#    return string
# print(replace_character(my_string))
# #
#
#
#
#
#
#
#
#
# # question_12
# # Given the code below, insert the correct method on line 3 in order to split the entire string in two parts, using the comma as a delimiter.
#
# #
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
# def split_string(my_string):
#     string = my_string.split(",")
#     return string
# print(split_string(my_string))
#

#
#
# # question_15
# # Given the code below, insert the correct method on line 3 in order to convert the first letter of each word in the string to uppercase.
# #
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
# def first_letter_uppercase(my_string):
#     string = my_string.title()
#     return string
# print(first_letter_uppercase(my_string))
#
#
#
# # question_16
# # Given the code below, use string formatting with the % operator on line 3 to map the values of 2010, 10k and Bitcoin to the corresponding formatting operators.
#
# my_string = "In %s, someone paid %s %s for two pizzas."
# def change_string_value(my_string):
#     string =(my_string%("2010","10k","Bitcoin"))
#     return string
# print(change_string_value(my_string))
#
#
# # question_17
# # Given the code below, use string formatting with the format() method on line 3 to map the values of 2010, 10k and Bitcoin to the corresponding formatting operators.
#
# my_string = "In {}, someone paid {} {} for two pizzas."
# def change_string_value(my_string):
#     string = (my_string("2010","10k","Bitcoin"))
#     return string
# print(change_string_value(my_string))
#


#question_18
# Given the code below, use slicing and insert the correct code on line 3 in order to return the substring 2010 from the string. Use positive indexes!


my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
def slcing(my_string):
    string =  my_string[3:7]
    return string
print(slcing(my_string))

# question_19

# Given the code below, use slicing and insert the correct code on line 3 in order to return the substring Bitcoin from the string. Use negative indexes!my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

def slicing(my_string):
    string = my_string[-23:-16]
    return string
print(slicing(my_string))



# question_20
# Given the code below, use slicing and insert the correct code on line 3 in order to return the first 12 characters in the string. Use a single, positive index!
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
def slicing(my_string):
    string = my_string[:12]
    return string
print(slicing(my_string))



# question_21

# Given the code below, use slicing and insert the correct code on line 3 in order to return the last 9 characters of the string. Use a single, negative index!
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
def slicing(my_string):
    string = my_string[-9:]
    return string
print(slicing(my_string))




# question_22
# Given the code below, use slicing and insert the correct code on line 3 in order to return the entire string in reversed order.

my_string = 'In 2010, some paid 10k Bitcoin for two pizzas.'
def slicing(my_string):
    string = my_string[::-1]
    return string
print(slicing(my_string))


# question_23

# Given the code below, use slicing and insert the correct code on line 3 in order to return every 7th character of the string, starting with the first character.
my_string = 'In 2010, some paid 10k Bitcoin for two pizzas.'
def slicing(my_string):
    string = my_string[::7]
    return string
print(slicing(my_string))


# question_24
# Given the code below, use slicing and insert the correct code on line 3 in order to return the string except the first 10 characters. Use a single, positive index!
my_string = 'In 2010, some paid 10k Bitcoin for two pizzas.'
def slicing(my_string):
    string = my_string[10:]
    return string
print(slicing(my_string))


# question_25
# Given the code below, use slicing and insert the correct code on line 3 in order to return the string except the last 4 characters. Use a single, negative index!

my_string = 'In 2010, some paid 10k Bitcoin for two pizzas.'
def slicing(my_string):
    string = my_string[:-4]
    return string
print(slicing(my_string))


