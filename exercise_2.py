#
list = ["ritu_naruka","risa","bitu","risa_naruka","lucky"]
def check_srname_naruka(list):

    check = 'naruka'

    res = []
    for i in list:
        if  "naruka" in i:
            print('yes')
            res.append(i)
    return res
print(check_srname_naruka(list))





# QUESTION_1
# Given the code below, insert the correct negative index on line 3 in order to get the last character in the string.



my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
last_charcter = my_string[-1]
print(last_charcter)
#
# # qestion_2
# # Given the code below, insert the correct positive index on line 3 in order to return the comma character from the string.
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
#
# print(my_string[7])


#question_3
# # Given the code below, insert the correct negative index on line 3 in order to return the w character from the string.
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[-10])

# question_4
# Given the code below, insert the correct method on line 3 in order to return the index of the B character in the string.
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."


print(my_string.index('B'))



#
#
#
#
# # question_5
# # # Given the code below, insert the correct method on line 3 in order to return the number of occurrences of the letter o in the string.
#
#
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

def count_character(my_string):
    count = 0


    for i in my_string:
        if i == 'o':

            count = count + 1
    return count
print(count_character(my_string))



#question_6

# Given the code below, insert the correct method on line 3 in order to convert all letters in the string to uppercase.
#
#
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string.upper())


# question_7
# Given the code below, insert the correct method on line 3 in order to get the index at which the substring Bitcoin starts.
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string.index("Bitcoin"))






# #question_8
# # Given the code below, insert the correct method on line 3 in order to check of the string starts with the letter X
#
#
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
def check_elements(my_string):
    check = 'X'
    res = " "
    for i in my_string:
        if  "X" in i:
            print('true')
        else:
            print("False")
            res.join(i)
    return res
print(check_elements(my_string))

#
#
#


# question_9

# Given the code below, insert the correct method on line 3 in orderto convert all uppercase
# letters to lowercase and all lowercase letters to uppercase.
#
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
def upper_to_lower_and_lower_to_uper(my_string):
    string = my_string.swapcase()
    return string

print(my_string.swapcase())


# question_10
# Given the code below, insert the correct method on line 3 in order to remove all spaces (single Space characters from the keyboard) from the string.
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
def remove_spaces(my_string):
    string = my_string.replace(" ","")
    return string
print(remove_spaces(my_string))

#
# # question_11
# Given the code below, insert the correct method on line 3 in order to replace all the occurrences of letter i with the substring btc.
# #
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

def replace_character(my_string):
   string = my_string.replace("i", "btc")
   return string
print(replace_character(my_string))
#


#
#
#
# # question_12
# # Given the code below, insert the correct method on line 3 in order to split the entire string in two parts, using the comma as a delimiter.
#
#
#
#
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
def split_string(my_string):
    string = my_string.split(",")
    return string
print(split_string(my_string))


# question_14
# Given the code below, insert the correct code on line 4 in order to concatenate my_string with the following string:
# my_other_string = "Poor guy!"
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
my_other_string = "Poor guy!"
string = my_string + my_other_string
print(string)




#
#
#
#
#
# # question_15
# # Given the code below, insert the correct method on line 3 in order to convert the first letter of each word in the string to uppercase.

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
def first_letter_uppercase(my_string):
    string = my_string.title()
    return string
print(first_letter_uppercase(my_string))
#
#
# #
# # # question_16
# # # Given the code below, use string formatting with the % operator on line 3 to map the values of 2010, 10k and Bitcoin to the corresponding formatting operators.
#
my_string = "In %s, someone paid %s %s for two pizzas."
def change_string_value(my_string):
    string =(my_string%("2010","10k","Bitcoin"))
    return string
print(change_string_value(my_string))
# #
#


# #question_18
# # Given the code below, use slicing and insert the correct code on line 3 in order to return the substring 2010 from the string. Use positive indexes!
#

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
def slcing(my_string):
    string =  my_string[3:7]
    return string
print(slcing(my_string))
#
# # question_19
#
# # Given the code below, use slicing and insert the correct code on line 3 in order to return the substring Bitcoin from the string. Use negative indexes!my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

def slicing(my_string):
    string = my_string[-23:-16]
    return string
print(slicing(my_string))
#
#
#
# # question_20
# # Given the code below, use slicing and insert the correct code on line 3 in order to return the first 12 characters in the string. Use a single, positive index!
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
def slicing(my_string):
    string = my_string[:12]
    return string
print(slicing(my_string))
#
#
#
# # question_21
#
# # Given the code below, use slicing and insert the correct code on line 3 in order to return the last 9 characters of the string. Use a single, negative index!
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
def slicing(my_string):
    string = my_string[-9:]
    return string
print(slicing(my_string))

#
#
#
# # question_22
# # Given the code below, use slicing and insert the correct code on line 3 in order to return the entire string in reversed order.
#
my_string = 'In 2010, some paid 10k Bitcoin for two pizzas.'
def slicing(my_string):
    string = my_string[::-1]
    return string
print(slicing(my_string))

#
#
#
# # question_23
my_string = 'In 2010, some paid 10k Bitcoin for two pizzas.'
def slicing(my_string):
    string = my_string[::7]
    return string
print(slicing(my_string))
#
#
# # question_24
# # Given the code below, use slicing and insert the correct code on line 3 in order to return the string except the first 10 characters. Use a single, positive index!
my_string = 'In 2010, some paid 10k Bitcoin for two pizzas.'
def slicing(my_string):
    string = my_string[10:]
    return string
print(slicing(my_string))

#
# # question_25
# # Given the code below, use slicing and insert the correct code on line 3 in order to return the string except the last 4 characters. Use a single, negative index!
#
my_string = 'In 2010, some paid 10k Bitcoin for two pizzas.'
def slicing(my_string):
    string = my_string[:-4]
    return string
print(slicing(my_string))