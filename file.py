
"""
question_191 - function
Add the necessary code in between print
's parentheses in order to read the content of test.txt as a string and have the result printed out to the screen.

"""


f  = open("test.txt","r")


print(f.read())



"""question_192 - function
Add the necessary code in between print
's parentheses in order to read the content of test.txt as a list where each element of the list is a row in the file,
 and have the result printed out to the screen.
"""
f = open("test.txt", "r")

print(f.readlines())




"""you are given a list of integers. Write a function
that takes this list as input and returns the sum of all even numbers in the list multiplied by
 the largest odd number in the list. If there are no even numbers in the list, the function should return 0.
For example, given the list [1, 2, 3, 4, 5], the function should return (2 + 4) * 5 = 30.
 Given the list [1, 3, 5, 7], the function should return 0.
Write a function called sum_even_times_max_odd that takes a list of integers as input and returns
 the result according to the rules above."""

#
# def sum_even_times_max_odd(input_list):
#     even_numbers = []
#     odd_number = []
#     total = 0
#     max_oddnum = 0
#     answer = 0
#     for i in input_list:
#         if i % 2 == 0:
#             even_numbers.append(i)
#             total = total + i
#
#         if i % 2 != 0:
#             odd_number.append(i)
#             if i > max_oddnum:
#                 max_oddnum = i
#
#     answer = total * max_oddnum
#
#     return even_numbers, total, odd_number, max_oddnum, answer
#
#
# x, y, z, a, b = sum_even_times_max_odd(input_list=[3, 5, 7])
# print(f"Even number in list {x}")
# print(f"Sum of all even numbers= {y}")
# print(f"odd numbers in list {z}")
# print(f"max odd number in list {a}")
# print(f"answer of the program is {b}")
#
#
# def max_of_two(x, y):
#     if x > y:
#         return x
#     return y
#
#
# print(max_of_two(10, 12))
#
#
# def max_of_three(x, y, z):
#     return max_of_two(x, max_of_two(y, z))
#
#
# print(max_of_three(3, 6, -5))
#
#
# def sum_elements(numbers):
#     total = 0
#     for x in numbers:
#         total += x
#     return total
#
#
# print(sum_elements([8, 2, 3, 0, 7]))
#
# def different_list(l):
#   x = []
#   for a in l:
#     if a not in x:
#       x.append(a)
#   return x
#
# print(different_list([1,2,3,3,3,3,4,5]))





 # # Write a program that takes a list of numbers and prints the sum of the positive numbers.
# # [-2, 5, -10, 8, 3]
# def add_positive_numbers(input: list) -> int:
#     sum = 0
#     for i in input:
#         if i > 0:
#             sum += i
#     return sum
# print(add_positive_numbers(input = 1))

 # Write a Python function that takes a list of strings as input, and then returns the 2 longest string in the list.
# input_dict = {'apple':5, 'banana':6, 'kiwi':4, 'orange':6, 'pear':4}
#
# def largest_string(input_dict , n):
#     new_dict = {}
#     for name, length in input_dict.items():
#         if length == n:
#             new_dict[name] = length
#     return new_dict
#
#
# name_of_largest_string = largest_string(input_dict=input_dict, n=6)
# print(name_of_largest_string)


#  # Write a Python function that takes a list of strings as input, and then returns the longest string in the list.
# input_list = ['apple', 'banana', 'kiwi', 'orange', 'pear', 'pineapple']
# def longest_string(input_list):
#     max_string = ""
#
#     for i in input_list:
#         if len(i) >= len(max_string):
#
#             max_string = i
#
#     return max_string
# x = longest_string(input_list)
# print(x)





#
# Dictionary = {'kevin': {'Test1': 97, 'Test2': 84, 'Test3': 89},
#                   'Bob':{'Test1': 67, 'Test2': 74, 'Test3': 59},
#                   'carol':{'Test1': 47, 'Test2': 94, 'Test3': 79},
#                   'ted':{'Test1': 67, 'Test2': 64, 'Test3': 99}
#               }
#
#
# def average_dictionary(Dictionary):
#     # dict = {}
#     sum = 0
#     for i in Dictionary.values():
#         sum += i
#         avg_value = sum/len(Dictionary)
#         return avg_value
# print(average_dictionary(Dictionary))




# You are given a list of dictionaries, where each dictionary represents a book and contains information about its title, author,
# and a list of reviews, where
# each review is a dictionary containing information about the reviewer's name, rating, and comments. Write a function that '
# takes in this list and returns the average rating for each book, along with'
#                                                                                                                                                                                                                                   ' the total number of reviews for each book. If a book has no reviews, its average rating should be 0.


input_list = [    {        "title": "The Great Gatsby",        "author": "F. Scott Fitzgerald",        "reviews": [
    {"name": "John Doe", "rating": 4, "comments": "Great book!"},            {"name": "Jane Smith", "rating": 3, "comments": "Good read."},            {"name": "Bob Johnson", "rating": 5, "comments": "Amazing!"},        ]
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "reviews": [
            {"name": "Alice Chen", "rating": 4, "comments": "Very well-written."},
            {"name": "Tom Smith", "rating": 4, "comments": "Enjoyed reading it."},
        ]
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "reviews": []
    }
]





def ave_ratings(input_list):
    result = []
    for i in input_list:
        print(i)
        total_ratings = 0
        num_reviews = len(i['reviews'])
        if num_reviews > 0:
            for review in i['reviews']:
                total_ratings += review['rating']
            average_rating = total_ratings / num_reviews
        else:
            average_rating = 0
        result.append({'title': i['title'], 'average_rating': average_rating, 'num_reviews': num_reviews})
    return result
print(ave_ratings(input_list))