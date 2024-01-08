#
#
# def sum_of_numbers():
#     a = int(input("enter_first_number:"))
#     b = int(input("enter_second_number:"))
#     total = a + b
#
#     return total
# print(sum_of_numbers())
#

vowel = ['a', 'e', 'i', 'o', 'u']
word = "programming"
def find_vowels(word):
    count = 0
    for character in word:
        if character in vowel:
            count += 1
    return count
print(find_vowels(word))


# con
vowel = ['a', 'e', 'i', 'o', 'u']
word = "programming"
def find_vowels(word):
    count = 0
    for character in word:
        if character not in vowel:
            count += 1
    return count
print(find_vowels(word))
#
str1 = "Analytics Vidhya"
print(str1.split(" "))



# Python – Convert Key-Value list Dictionary to List of Lists
data_dict = {'a': 1, 'b': 2, 'c': 3}
def conv_list_of_list(data_dict):
    list_of_lists = []

    for key, value in data_dict.items():
        list_of_lists.append([key, value])
    return list_of_lists

print(conv_list_of_list(data_dict))


#  Python – Convert List to List of dictionaries(dict ki value key ki len ho)

name_list = ["ritu", "raj", "rajesh"]
def con_list_of_dict(name_list):
    empty_list = []
    for i in name_list:
        dict={i:len(i)}

        empty_list.append(dict)
    return empty_list
print(con_list_of_dict(name_list))


# check "s" is list
list = ["ritu","risa","ravina","seeta"]

def check_s_in_list(list):
    new_list =[]
    for i in list:
        if "s" in i:
            new_list.append(i)
    return new_list

print(check_s_in_list(list))


#  Calculate and print the average of the dictionary.
dict = {"a":20,"b":50,"c":100,"d":30}
def average_of_dict(dict):
    sum = 0
    for i in dict.values():
        sum+=i
        avg = sum/len(dict.values())
    return avg
print(average_of_dict(dict))

 # Write a Python program to get the maximum and minimum values of a dictionary.

dict = {"a":30,"m":80,"k":90,"c":2,"d":50}
def find_min_and_max_value(dict):
    min_value  = None
    max_value  = None
    for i in dict.values():
        if min_value is None or i < min_value:
            min_value = i

        elif max_value is None or i > max_value:
            max_value = i
    return min_value, max_value
print(find_min_and_max_value(dict))



# Write a Python program to remove duplicates from the dictionary.

dict = {"a":30,"m":80,"k":90,"c":2,"d":30}
def remove_duplicate(dict):
    new_dict={}
    for key,value in dict.items():
        if value not in new_dict.values():
            new_dict[key] = value
    return new_dict
print(remove_duplicate(dict))



#  odd
list = [1,90,3,30,20,5,9,90,7,58]
def odd_numbers(list):
    odd = []
    for i in list:
        if i % 2 != 0:
            odd.append(i)
    return odd
print(odd_numbers(list))


#  even
list = [1,90,3,30,20,5,9,90,7,58]
def even_numbers(list):
    even = []
    for i in list:
        if i % 2 == 0:
            even.append(i)
    return even
print(even_numbers(list))

# sum
list = [10,20,5,9,90,7,58,1]
def sum(list):
    sum = 0
    for i in list:
        sum+=i

    return sum
print(sum(list))

# convert two list into one dict
# list1 = ["a","b","c","d"]
# list2 = [1,2,3,4]
# dict1 = dict()
# for i in range(len(list1)):
#     dict1.update({list1[i]:list2[i]})
# print(dict1)
#


# rename key of dict
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sample_dict['location' ] = sample_dict.pop('city')
print(sample_dict)


# Change value of a key in a nested dictionary
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict['emp2']['salary']  = 300
print(sample_dict)


#  Return multiple values from a function

def calculation(a,b,c):
    add = a+b+c
    subtaraction = a-b-c
    mul = a*b*c
    return add,subtaraction,mul
print(calculation(10,20,30))


# Write a Python program to iterate over the following
# dictionary and print each key-value pair on a new line:
student = {
    "Alice": 92,
    "Bob": 78,
    "Charlie": 85,
    "David": 95,
    "Eva": 88
}

for key, value in student.items():
    print(f"{key}: {value}")

"""

Create a function that takes two
lists as input and returns a new list containing
common elements between the two lists"""

list1 = [12,30,90,60,40,13]
list2 = [10,30,90,65,50,12]
def common_of_list(list1,list2):
    common_element = []
    for i in list1:
        if i in list2:
            common_element.append(i)

    return common_element
print(common_of_list(list1,list2))


# Write a Python program to find the difference between two lists.
def find_list_difference(list1, list2):
    difference = []
    for i in list1:
        if i not in list2:
            difference.append(i)
    return difference

list_a = [1, 2, 3, 4, 5, 6, 40]
list_b = [3, 4, 5, 6]
result = find_list_difference(list_a, list_b)
print(result)


# Create a function that takes a list of words and returns a new list
# containing the lengths of each word.
word_list = ["ritu","kuldeep","rohit"]
def word_lengths(word_list):
    length = []
    for i in word_list:
        length.append(len(i))
    return length
print(word_lengths(word_list))



# Print the first 10 natural numbers using for loop.
for i in range(0,11):
    print(i)


# Python program to print all the even numbers within the given range.
def evens_in_range():
    for i in range(10):
        if i %2 == 0:
            print(i)

evens_in_range()


# Example 3: Python program to calculate the sum of all numbers from 1 to a given number.

def sum_of_all_in_range():
    sum = 0
    for i in range(10):
        sum = sum+i
    return sum
print(sum_of_all_in_range())


# Example 4: Python program to calculate the sum of all the odd numbers within the given range.
def sum_of_odd():
    sum = 0
    for i in range(10):
        if i % 2 != 0:
            sum = sum + i
    return sum
print(sum_of_odd())


# Example 5: Python program to print a multiplication table of a given number
def multiplication_of_5():
    given_number = 5

    for i in range(11):
        print(given_number, "x", i, "=", 5 * i)
multiplication_of_5()



# Example 6: Python program to display numbers from a list using a for loop.
list = [2,3,4,1,4,56,7,5,7]
def display_numbers(list):
    for i in list:
        print(i)

display_numbers(list)



# Example 7: Python program to count the total number of digits in a number.
num = 123456
num = str(num)
def count_digits(num):
    count = 0
    for i in num:
        count += 1
    return count
print(count_digits(num))


# Example 8: Python program to check if the given string is a palindrome.

string = "mumum"
def palindrome_or_not(string):
    reverse = ""
    for i in string:
        reverse = i + reverse
    if (string == reverse):
        print("The string", string, "is a Palindrome.")
    else:
        print("The string", string, "is NOT a Palindrome.")
palindrome_or_not(string)



# Example 9: Python program that accepts a word from the user and reverses it.
given_string = "ritu"
def reverse_word(given_string):
    reverse_string = ""
    for i in given_string:
        reverse_string = i + reverse_string
    return reverse_string
print(reverse_word(given_string))


# # Example 10: Python program to check if a given number is an Armstrong number
given_number = 153
def armstrong_number(given_number):
    given_number = str(given_number)
    string_length = len(given_number)
    sum = 0
    for i in given_number:
        sum += int(i) ** string_length
    if sum == int(given_number):
        print("Amstrong number")
    else:
        print("Not an Amstrong number")
armstrong_number(given_number)

# #11 Example  Python program to find what is even and odd numbers from a series of numbers.
num_list = [1, 3, 5, 6, 99, 134, 55]
def the_number_is_even_or_odd(num_list):

    for i in num_list:
        if i % 2 == 0:
            print(i, "even number.")
        else:
            print(i, "odd number.")
the_number_is_even_or_odd(num_list)

# # Example 12: Python program to count the number of even and odd numbers from a series of numbers.
num_list = [1, 3, 5, 6, 99, 134, 55]
def count_even_numbers(num_list):
    count_even = 0
    for i in num_list:
        if i % 2 == 0:
            count_even += 1

    return count_even
print(count_even_numbers(num_list))


def count_odd_numbers(num_list):
    count_odd = 0
    for i in num_list:
        if i % 2 != 0:
            count_odd += 1

    return count_odd
print(count_odd_numbers(num_list))



# Example 14: Python program to find the factorial of a given number.
given_number = 5
factorial = 1
for i in range(1, given_number + 1):
    factorial = factorial * i

print(factorial)



# DICTIONARY
# Question 1: Write a Python function that takes a list of words as input and returns a dictionary where
# the keys are unique words, and the values are the frequency of each word in the list.
word_list = ["apple", "banana", "apple", "orange", "banana", "apple",32,23,32,32,32,23]
def word_frequency(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count
print(word_frequency(word_list))

"""question_2
Write a function that takes two dictionaries as input and returns a new
dictionary containing only the common key-value pairs.
"""
def common_elements(dict1, dict2):
    common_dict = {}
    for key in dict1:
        if key in dict2 and dict1[key] == dict2[key]:
            common_dict[key] = dict1[key]
    return common_dict

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 20, 'c': 30, 'd': 40}
result = common_elements(dict1, dict2)
print(result)


"""Question 3: Write a function that takes a dictionary as
input and returns a new dictionary with the same keys but
 with values sorted in descending order."""
def sort_dict_values(dictionary):
    sorted_items = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    sorted_dict = {}
    for key, value in sorted_items:
        sorted_dict[key] = value
    return sorted_dict
original_dict = {'a': 30, 'b': 10, 'c': 20}
result = sort_dict_values(original_dict)
print(result)

# sorted
dictionary = {
    5: 'e',
    4: 'd',
    3: 'c',
    2: 'b',
    1: 'a',
}
sorted_dictionary = {}
for key,value in sorted(dictionary.items()):
    sorted_dictionary[key]=value
print(sorted_dictionary)





# two sum

nums = [2,15,7,11]
target = 9
def sum_two_elements(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]+nums[j] == target:


                return[i,j]


print(sum_two_elements(nums))


# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
num_1 = [1,3]
num_2 = [2]
num = num_1+num_2
num.sort()
print(num)
def calculate_medean(num):
    sum = 0
    for i in num:
        sum += i

    midean_val = sum / len(num)
    return midean_val

c = calculate_medean(num)
print(c)


#  Convert two lists into a dictionary.
# Two lists
keys = ['name', 'age', 'city']
values = ['ritu', 18, 'jaipur']

def two_lists_into_a_dict():
    my_dict = {}
    if len(keys) == len(values):
        for i in range(len(keys)):
            key = keys[i]
            value = values[i]
            my_dict[key] = value
        return my_dict

result_dict = two_lists_into_a_dict()
print(result_dict)

#  Merge two Python dictionaries into one.
def merge_two_dict():

    dict1 = {'name': 'ritu', 'age': 18}
    dict2 = {'city': 'jaipur', 'gender': 'female'}
    dict1.update(dict2)
    print(dict1)
merge_two_dict()


# Write a Python program to create a dictionary of keys x, y, and z
# where each key has as value a list from 11-20, 21-30, and 31-40
# respectively. Access the fifth value of each key from the dictionary.

dict = {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}

def find_5th_value_all_of_keys(dict):
    for key, value in dict.items():
        if len(value) >= 5:
            print(f"{key}': {value[4]}")
    return result_dict

find_5th_value_all_of_keys(dict)

#  Write a Python program to drop empty items from a given dictionary.
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

original_dictionary = {'c1': 'Red', 'c2': 'Green', 'c3': None}
def drop_empty_items(original_dictionary):
    new_dict ={}
    for key, value in original_dictionary.items():
        if value is not None:
            new_dict[key] = value
    return new_dict
print(drop_empty_items(original_dictionary))



# Write a Python program to filter a dictionary based on values.
# Original Dictionary:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}

dict = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}

def grater_then_170(dict):
    new_dict = {}
    for key, value in dict.items():
        if value > 170:
            new_dict[key] = value
        else:
            print(None)

    return new_dict
print(grater_then_170(dict))

#  Write a Python program to convert more than one list to a nested dictionary.
# Original strings:
# ['S001', 'S002', 'S003', 'S004']
# ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# [85, 98, 89, 92]
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]

student_ids = ['S001', 'S002', 'S003', 'S004']
student_names = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
student_scores = [85, 98, 89, 92]
def convert_list_to_nested_dict(student_ids,student_names,student_scores):
    nested_dict_list = []
    for i in range(len(student_ids)):
        nested_dict_list.append({student_ids[i]: {student_names[i]: student_scores[i]}})
    return nested_dict_list
print(convert_list_to_nested_dict(student_ids,student_names,student_scores))

#  Write a Python program to verify that all values in a dictionary are the same.
# Original Dictionary:
# {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# Check all are 12 in the dictionary.
# True
# Check all are 10 in the dictionary.
# False
my_dict = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}

def all_values_are_same(my_dict):
    for value in my_dict.values():
        if value == 12:
            return "same"
        else:
            return "not_same_same"

result = all_values_are_same(my_dict)
print(result)




# Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists.
# Original list:
# [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
original_list = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
def group_to_dict(input_dict):
    group_dict = {}
    for key, value in input_dict:
        if key not in group_dict:
            group_dict[key] = []
        group_dict[key].append(value)
    return group_dict
result_dict = group_to_dict(original_list)
print(result_dict)



# Write a Python program to find the length of a dictionary of values.
my_dict = {"ritu": 3, "naruka": 10, "raj": 2, "siya": 7}
def find_values_length(my_dict):
    for i in my_dict.values():
        length_of_dict = len(my_dict)
    return length_of_dict
print(find_values_length(my_dict))


#   Write a Python program to convert a dictionary into a list of lists.
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Convert the said dictionary into a list of lists:
# [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
# Original Dictionary

dict = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
def dict_to_list_of_list(dict):
    empty_list = []
    for key,value in dict.items():
        list_of_list = [key,value]
        empty_list.append(list_of_list)
    return empty_list
print(dict_to_list_of_list(dict))

"""
 Write a Python program to filter even numbers from a dictionary of values.
Original Dictionary:
{'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
Filter even numbers from said dictionary values:
{'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}"""

dict = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
def even_number_of_dict_values(dict):
    new_dict = {}
    for key,value in dict.items():
        even_values_list = []
        for i in value:
            if i % 2 == 0:
                even_values_list.append(i)
        new_dict[key] = even_values_list
    return new_dict
print(even_number_of_dict_values(dict))


#  Write a Python program to create a flat list of all the keys in a flat dictionary.
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# Create a flat list of all the keys of the said flat dictionary:
# ['Theodore', 'Roxanne', 'Mathew', 'Betty']
dict = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
def dict_to_lst(dict):
    list = []
    for key,vlaue in dict.items():
        list.append(key)
    return list
print(dict_to_lst(dict))

# Write a Python program to create a flat list of all the values in a flat dictionary.
# Sample Output:
# Original dictionary elements:
dict = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# Create a flat list of all the values of the said flat dictionary:
# [19, 20, 21, 20]


def dict_to_list(dict):
    list = []
    for key,value in dict.items():
        list.append(value)

    return list
print(dict_to_list(dict))

#  Write a Python program to find the key of the maximum value in a dictionary.
# Sample Output:
# Original dictionary elements:
dict = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
# Finds the key of the maximum and minimum value of the said dictionary:
# ('Roxanne', 'Theodore')
def key_of_max_and_min_value(dict):
    min_val = None
    max_val = None
    for key,value in dict.items():
        if min_val is None or value < min_val:
            min_val = value
            min_key = key

        elif max_val is None or value > max_val:
            max_val = value
            max_key = key
    return min_key, max_key
print(key_of_max_and_min_value(dict))

