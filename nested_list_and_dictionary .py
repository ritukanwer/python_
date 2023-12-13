


# 1 = how to create a nested dictionary.
nested_dictionary = {1:{'name': 'ritu','age':18},
                     2:{'name':'ridhi', 'age':20}
                     }
print(nested_dictionary)






# 3 = add element to a nested dictionary.

nested_dictionary = {1:{'name': 'ritu','age':18},
                     2:{'name':'ridhi', 'age':20}
                     }
nested_dictionary[3] = {}
nested_dictionary[4] = {}

nested_dictionary[3]['name'] = 'sidhi'
nested_dictionary[3]['age'] = '13'
nested_dictionary[4]['name'] = 'veeni'
nested_dictionary[4]['age'] = '25'
#
print(nested_dictionary[3])
print(nested_dictionary[4])
print(nested_dictionary)




# 4 = add anouther dictionary to a nested dictionary.

nested_dictionary = {1:{'name': 'ritu','age':18},
                     2:{'name':'ridhi', 'age':20}
                     }

nested_dictionary[3] = {'name':'risa','age':21}
print(nested_dictionary)



# 5 = delete elements from a nested dictionary?
nested_dictionary = {1:{'name': 'ritu','age':18},
                     2:{'name':'ridhi', 'age':20}
                     }

del nested_dictionary[1]['name']
print(nested_dictionary[1])




# 6 = how to delete dictionary from a nested dictionary?
nested_dictionary = {1:{'name': 'ritu','age':18},
                     2:{'name':'ridhi', 'age':20},
                     3:{'name':'sidhi','age':10},
                     4:{'name':'veeni','age':23}
                     }
del nested_dictionary[1]
print(nested_dictionary)
#
#
#  #7 = How many students are in the "students" dict? Use the appropriate function.
#
students = {
    "ritu": {"age": 10, "address": "jaipur"},
    "ridhi": {"age": 11, "address": "jodhpur"},
    "sidhi": {"age": 9, "address": "ajmer"},
}
def student_length(students):
   length  = len(students)
   return length

a = student_length(students)
print("students_length:-",a)
#



people = {1: {'name': 'John', 'age': '27', 'sex': 'Male',4:[2,3,5]},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}
          }
if 1 in people:
    for i,j in people[1].items():
        print(i,j)





people = {1: {'name': 'John', 'age': '27', 'sex': 'Male',4:[2,3,5]},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}
          }

if 4 in people[1]:
    sum = 0
    for i in people[1][4]:
        sum = sum + i

print(sum)


people = {1: {'name': 'John', 'age': '27', 'sex': 'Male',4:[2,3,5],'john_friend':{'name': 'Marie', 'age': '22', 'sex': 'Female', 9:[1,2,4,5,6]}},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}
          }

if 9 in people[1]['john_friend']:
    sum = 0
    for i in people[1]['john_friend'][9]:

        sum += i

print(sum)

# average of nested dictionary numbers
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male',4:[2,3,5],
              'john_friend':{'name': 'Marie', 'age': '22', 'sex': 'Female', 'ritu':[10,20,30]}},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}
          }

if 'ritu' in people[1]['john_friend']:
    sum =0
    for i in people[1]['john_friend']['ritu']:             # 60/3 = 20
        sum = sum + i
average = sum/len(people[1]['john_friend']['ritu'])

print(average)
print(sum)


# average of nested dictionary numbers
people = {1:{'name':'ritu','age':18,'address':{'village':'chandma','number':[10,20]}},
          2:{'name':'kannu','age':20}
}

def find_average_value_of_number(people):
    if 'number' in people[1]['address']:
        sum = 0
        for i in people[1]['address']['number']:
            sum = sum + i

            average_value = sum/len(people[1]['address']['number'])
        return average_value
print(find_average_value_of_number(people))
















 # average age of student.
# students = {
#     "ritu": {"age": 10, "address": "chandma"},
#     "sidhi": {"age": 20, "address": "jaipur"},
#     "ridhi": {"age": 30, "address": "ajmer"},
# }
#
#
# def average_of_student(students):
#     total = 0
#     for i in students.keys():
#         total += students[i]['age']
#     average = total/len(students)
#     return average
# average = average_of_student(students)

# print(average)






# # max_value
#

student = {
    "ritu": {"age": 10, "address": "chandma"},
    "sidhi": {"age": 20, "address": "jaipur"},
    "ridhi": {"age": 13, "address": "ajmer"},
    "hiyu":{"age":7, "address":"bikaner"}
}
def find_max_number(student):
    max_number = None
    for i in student.keys():
        if max_number is None or student[i]['age'] > max_number:
            max_number = student[i]['age']

    return max_number
print(find_max_number(student))

#
# # # Python | Sort Python Dictionaries by Key or Value
# my_dict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# # {'rajnish': 9, 'ravi': 10, 'sanjeev': 15, 'suraj': 32, 'yash': 2}
#
# def sort_dictionary(my_dict):
#     new_sorted_dict = {}
#     for i in sorted(my_dict.keys()):
#
#
#         new_sorted_dict[i] = my_dict[i]
#
#     return new_sorted_dict
# print(sort_dictionary(my_dict))
#
#
# # python | Sort Python Dictionaries by Key or Value
#
# my_dict={'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# def sorted_dict(my_dict):
#     new_sorted_dict={}
#     for keys,value in sorted(my_dict.items()):
#         new_sorted_dict[value]=keys
#     return new_sorted_dict
# print(sorted_dict(sorted_dict(my_dict)))
# #
#
#
#
#
#
# # odd number of a nested dictionary
# student = {
#     "ritu": {"age": 10, "address": "chandma"},
#     "sidhi": {"age": 20, "address": "jaipur"},
#     "ridhi": {"age": 13, "address": "ajmer"},
# }
# def find_odd_number(student):
#     odd_numbers = {}
#     for i in student.keys():
#         if student[i]['age'] % 2 != 0:
#             odd_numbers[i] = student[i]
#
#     return odd_numbers
# print(find_odd_number(student))
#
#
#
#
# # even number of a nested dictionary
# student = {
#     "ritu": {"age": 10, "address": "chandma"},
#     "sidhi": {"age": 20, "address": "jaipur"},
#     "ridhi": {"age": 13, "address": "ajmer"},
# }
# def find_even_number(student):
#     even_number = {}
#     for i in student.keys():
#         if student[i]['age'] % 2 == 0:
#             even_number[i] = student[i]
#
#     return even_number
# print(find_even_number(student))
#
#
#
#
# # write a pyton program to get keys from the nested dictionary
# data = {
#     "student_1": {'name':'ritu', 'id':1,'age':18},
#     "student_2": {'name':'risa', 'id':7,'age':16},
#     "student_3": {'name':'disha', 'id':6,'age':20}
# }
#
# for i in data:
#     print(data[i].keys())
#
#
