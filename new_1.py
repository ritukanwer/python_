

# Learn how to add elements in nested dictionary.
nested_dictionary = {1:{'name':'ritu','age':18,'address':'chandma_kalan'},
                     2:{'name':'risa','age':20,'address':'jaipur'},
                     3:{'name':'nidhi','age':15,'address':'jodhpur'}
                     }

nested_dictionary[4] = {}
nested_dictionary[4]['name'] = 'veeni'
nested_dictionary[4]['age'] = '25'
nested_dictionary[4]['address'] = 'ajmer'
print(nested_dictionary[4])
print(nested_dictionary)

# How to add another dictionary to nested dictionary
nested_dictionary = {1:{'name':'ritu','age':18,'address':'chandma_kalan'},
                     2:{'name':'risa','age':20,'address':'jaipur'},
                     }
nested_dictionary[3] = {'name':'nidhi','age':15,'address':'jodhpur'}

print(nested_dictionary)


# How to delete elements from nested dictionary

nested_dictionary = {1:{'name':'ritu','age':18,'address':'chandma_kalan'},
                     2:{'name':'risa','age':20,'address':'jaipur'},
                     3:{'name':'nidhi','age':15,'address':'jodhpur'}
                     }
del nested_dictionary[3]['name']
print(nested_dictionary)

# How to delete dictionary from nested dictionary
nested_dictionary = {1:{'name':'ritu','age':18,'address':'chandma_kalan'},
                     2:{'name':'risa','age':20,'address':'jaipur'},
                     3:{'name':'nidhi','age':15,'address':'jodhpur'}
                     }
del nested_dictionary[3]
print(nested_dictionary)



# Python program to find the sum of all items in a dictionary

dictionary = {1:2,2:3,4:5}
def sum_all_items(dictionary):
    keys_sum = 0
    values_sum = 0
    new_dictionary = {}
    for key,value in dictionary.items():
        keys_sum = keys_sum + key
        values_sum = values_sum + value

        new_dictionary = {keys_sum:values_sum}
    return new_dictionary
print(sum_all_items(dictionary))


# define a function returnsum that takes a dictionary as a input..

dictionary = {'ritu':18,'babbu':8,'hiyu':7,'kannu':10,'divyanshee':15}
def sum_of_values(dictionary):
    sum = 0
    for i in dictionary.values():
        sum = sum + i
        i = sum
    return sum
x = sum_of_values(dictionary)
print(x)


# convert to a dictionary values to a list using the list() function.
dictionary = {'ritu':18,'hiyu':7,'kannu':10,'BABBU':8}
a = list(dictionary.values())
print(a)


"""   OR  """

dictionary = {'ritu':18,'hiyu':7,'kannu':10,'babbu':8}
def convert_dict_values_list(dictionary):
    new_list = []
    for i in dictionary.values():
        new_list.append(i)
    return new_list
print(convert_dict_values_list(dictionary))



# Exercise 1: Convert two lists into a dictionary
#
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# dict_1 = dict()
#
# for i in range(len(keys)):
#     dict_1.update({keys[i]: values[i]})
# print(dict_1)
#


