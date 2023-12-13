
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



