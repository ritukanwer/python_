# # 2
# # marge two python dictionary into one
dict_1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict_2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}


dict_3 = dict_1.copy()
dict_3.update(dict_2)

print(dict_3)

# Write a Python script to add a key to a dictionary.
dict = {'name':'ritu','age':18}
dict.update({"address":"chandma"})
print(dict)


# .Write a Python program to sum all the items in a dictionary.

dictionary = {10:20,30:40,50:60,70:80}
def sum_all_items(dictionary):
    keys_sum = 0
    values_sum = 0
    new_dict = {}
    for key,value in dictionary.items():
        keys_sum = keys_sum + key
        values_sum = values_sum + value
        new_dict = {keys_sum:values_sum}
    return new_dict
print(sum_all_items(dictionary))


# Write a Python program to multiply all the items in a dictionary.
dictionary = {1:2,3:4,5:2,7:2}
def multiply_all_items(dictionary):
    keys_multi = 1
    values_multi = 1
    new_dict = {}
    for key,value in dictionary.items():
        keys_multi = keys_multi* key
        values_multi = values_multi * value
        new_dict = {keys_multi:values_multi}
    return new_dict
print(multiply_all_items(dictionary))


# Write a Python program to sort a given dictionary by key.
dict = {'ritu':18,"kannu":10,"hiyu": 7,'yash':8,'divyanshee':15}
def sorted_by_keys(dict):
    new_sorted_dict = {}
    for key in sorted(dict.keys()):
        new_sorted_dict[key] = dict[key]
    return new_sorted_dict
print(sorted_by_keys(dict))



# Write a Python program to sort a given dictionary by values.
dict = {'ritu':18,"kannu":10,"hiyu": 7,'yash':8,'divyanshee':15}
def sorted_by_values(dict):
    new_sorted_dict = {}
    for key,value in sorted(dict.items()):
        new_sorted_dict[value] = key
    return new_sorted_dict
print(sorted_by_values(sorted_by_values(dict)))


# find  smallest number in list
list = [19,20,30,191,20,1,90,80]
def min_number(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min

print(min_number(list))


# find second smallest number in list

lst = [1,2,3,4,5,6,7]
lst.sort()
print(lst[1])
lst = [1,2,3,4,5,6,7]
def find_second_smallest_number(lst):

    for i in lst:
        sorted_lst = sorted(lst)
        second_smallest = sorted_lst[1]



    return second_smallest
print(find_second_smallest_number(lst))


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
# remove duplictes
def remove_douplicate(student_data):
    new_dict ={}
    for key,value in student_data.items():
        if value not in new_dict.values():
            new_dict[key] = value
    return new_dict
print(remove_douplicate(student_data))


 # Write a Python script to concatenate the following dictionaries to create a new one
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

new_dict = dic1.copy()
new_dict.update(dic2)
new_dict.update(dic3)
print(new_dict)


# Write a Python program to select an item randomly from a list.
# import random
# lst = [1,2,3,4,5,6,7]
#
# random_number = random.choice(lst)
# print(random_number)



# Write a Python program to get the maximum and minimum values of a dictionary.
my_dict = {'x':500, 'y':5874, 'z':560}
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

# Write a Python program to remove a key from a dictionary.
my_dict = {'x':500, 'y':5874, 'z':560}
del my_dict['x']
print(my_dict)


# import random
# list=[1,5,4,2,36,5,8,7]
# def a(list):
#     ran=random.choice(list)
#     return ran
# print(a(list))



#







# remove duplictes
# def find_douplicate(input_list):
#     douplicate = {}
#     seen = set()
#     for i in input_list():
#
#         if i in seen:
#             douplicate.apped(i)
#         else:
#             seen.add(i)
#     return douplicate
# input_list = [6,7,6,8,9,5,4,3,7]
#
# print(find_douplicate(input_list))




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
   },
}


# for i in student_data:
#     student_data[i]['ram']=2
# print(student_data)




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

result = {}
duplicate = {}

for key, value in student_data.items():
    if value not in result.values():
        result[key]=value
    else:
        duplicate[key]=value
# print(result)
print(duplicate)

