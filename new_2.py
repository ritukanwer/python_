#
#
#
# student_data = {'id1':
#    {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id2':
#   {'name': ['David'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id3':
#     {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
# 'id4':
#    {'name': ['Surya'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
# }
# # def add_key_value(student_data):
# #
# #     for i in student_data:
# #         student_data[i]['ritu']=18
# #
# #     return student_data
# # print(add_key_value(student_data))
#
#
#
#
#
#
# student_data = {'id1':
#    {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id2':
#   {'name': ['David'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id3':
#     {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
# 'id4':
#    {'name': ['Surya'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
# }
# #
# # key = 'ritu'
# # value = '18'
# # def add(student_data):
# #     new_list = [id1, id2, id3, id4]
# #     for i in new_list:
# #         if i in student_data:
# #             student_data[i][key] = value
# #         else:
# #             student_data[i] = {key: value}
# #
# #     return new_list
# #
# # print(add(student_data))
#
#
#
#
#
# # Write a Python program to get the maximum and minimum values of a dictionary.
# my_dict = {'x':500, 'y':5874, 'z':560}
def find_min_and_max_value(my_dict):
    min_value  = None
    max_value  = None
    for i in my_dict.values():
        if min_value is None or i < min_value:
            min_value = i

        elif max_value is None or i > max_value:
            max_value = i
    return min_value, max_value
print(find_min_and_max_value(my_dict))

#
#
# # find second smallest number in list
#
# lst = [1,2,3,4,5,6,7]
# lst.sort()
# print(lst[1])
# lst = [1,2,3,4,5,6,7]
# def find_second_smallest_number(lst):
#
#     for i in lst:
#         sorted_lst = sorted(lst)
#         second_smallest = sorted_lst[1]
#
#
#
#
student_data = {'id1':
   {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id2':
  {'name': ['David'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id3':
    {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
'id4':
   {'name': ['Surya'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   }
}

#
# def find_duplicate(student_data):
#     duplicate_values = {}
#     count = 0
#     for key1, value1 in student_data.items():
#         for key2, value2 in student_data.items():
#             if key1 != key2 and value1 == value2:
#                 duplicate_values[key1] = value1
#                 count = count + 1
#
#     return duplicate_values,count
#
# print(find_duplicate(student_data))
















#
# def find(student_data):
#     result = {}
#     duplicate = {}
#     count = 0
#     for key, value in student_data.items():
#         if value not in result.values():
#             result[key] = value
#         else:
#             duplicate[key] = value
#     # print(result)
#     # print(duplicate)
#             count += 1
#     return result,duplicate,count
#


# print(find(student_data))


#
#
# dict = {'ritu':18,
#         'kannu':10,
#         'hitu':7,
#         'babbu':8}
#
#
# def count_numbers(dict):
#     count = 0
#     for key,value in dict.items():
#         count = count + 1
#
#     return count
# print(count_numbers(dict))




student_data = {'id1':
   {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id2':
  {'name': ['David'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id3':
    {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
'id4':
   {'name': ['Surya'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
}




#
# def count_numbers(student_data):
#     count = 0
#     for key,value in student_data.items():
#         count = count + 1
#
#     return count
# print(count_numbers(student_data)),
# remove duplicate
# find duplicate , count




# remove duplicates

student_data = {'id1':
   {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id2':
  {'name': ['David'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id3':
    {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id4':
   {'name': ['Surya'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
'id5': {'name': ['Surya'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
'id6': {'name': ['Surya'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
'id7': {'name': ['Surya'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   }
}

def remove_duplicates(student_data):
    new_dict = {}
    for key,value in student_data.items():
        if value not in new_dict.values():
            new_dict[key] = value
    return  new_dict
print(remove_duplicates(student_data))



# count all elements

student_data = {'id1':
   {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id2':
  {'name': ['David'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id3':
    {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
'id4':
   {'name': ['Surya'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
'id5': {'name': ['Surya'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   }
}

def count_elements(student_data):
    count = 0
    for key,value in student_data.items():
        count = count + 1
    return count
print(count_elements(student_data))



# find_duplicate

student_data = {'id1':
   {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id2':
  {'name': ['David'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id3':
    {'name': ['suriya'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
'id4':
   {'name': ['sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },

    }

def find_duplicates(student_data):
    duplicate_count = 0
    check_dictionary = []
    duplicate = []
    for key,value in student_data.items():
        value_list = list(value.items())
        if value_list in check_dictionary:
            duplicate_count += 1

        else:
            check_dictionary.append(value_list)
    return duplicate_count
print(find_duplicates(student_data))

#
#
# def print_arguments(*args):
#     even = []
#     for i in args:
#         if i % 2==0:
#             even.append(i)
#     return even
#
# x = print_arguments(1,2,3,5,68,7,80,45,2,45,767,6,87,8,87,8,8,22)
# print(x)
#
#
# def find_keys(*args):
#     for key,value in args:
#         print(key)
#     return key
# # print(find_key(("19.07'53.2", "72.54'51.0"):"Mumbai", \
# #           ("28.33'34.1", "77.06'16.6"):"Delhi")
# # )
#
# print(find_keys({"a": 10, "risa": 20}))
#
#
# def sum_of_values(*args):
#     sum = 0
#     for key, value in args:
#         sum = sum + value
#     return sum
#


"""
Question1: Write a program which will find all such numbers which are divisible by 7
but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained
should be printed in a comma-separated sequence on a single line.

Hints: Consider use range(#begin,#end)method"""

def find_divisible_by_7():
    lst = []
    for i in range(2000,3201):
        if (i%7==0) and (i%5!=0):
            lst.append(i)
    return lst

x = find_divisible_by_7()
print(x)



"""
Question: With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
such that is an integral number between 1 and n (both included). and then the program should print the
dictionary. Suppose the following input is supplied to the program: 8 Then, the output should
be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
Consider use dict()"""

def find_squerevalues(x):
    new_dictionary = {}
    for i in range(1,x+1):
        new_dictionary[i] = i*i
    return new_dictionary
print(find_squerevalues(8))




"""
Question: Write a program which can compute the factorial of a given numbers. 
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

Hints: In case of input data being supplied to the question, it should be assumed to be a console input."""


# def find_factorial(x):
#
#     if x == 0:
#         return 1
#     else:
#         return x * find_factorial(x - 1)
# a = int(input("enter a number:"))
# output = find_factorial(a)
# print(output)

"""
Question: Write a program which accepts a sequence of comma-separated 
numbers from console and generate a list and a tuple which contains every
number. Suppose the following input is supplied to the program: 34,67,55,33,12,98
Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')

Hints: In case of input data being supplied to the question, it should be assumed
to be a console input. tuple() method can convert list to tuple
"""


x = input("enter number")
a = x.split(',')
change_tuple = tuple(a)

print(a)
print(change_tuple)

