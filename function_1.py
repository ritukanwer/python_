# #question_1
# # FIND MAX OF THREE NUMBERS
#
#
# # #
# def max_of_three_number(num1,num2,num3):
#     numbers = [num1,num2,num3]
#     max_num = numbers[0]         #[0] is num1
#     # for i in numbers[1:]:
#     for i in numbers:
#         if i > max_num:
#             max_num = i
#     return max_num
#
# x = max_of_three_number(10,20,30)
#
# print(x)
#
#
#
#
#
# # find min of three numbers
#
# def min_of_three_numbers(num1,num2,num3):
#     numbers = [num1,num2,num3]
#     min_num = numbers[0]
#     for i in numbers:
#         if i < min_num:
#             min_num = i
#     return min_num
#
# y = min_of_three_numbers(17,39,506)
# print(y)
#
# #
# #
# # even_numbers
# list = [3,4,5,7,8,9,1,2,4,6]
# def find_even_numbers(list):
#     even = []
#     for i in list:
#         if i % 2 == 0:
#             even.append(i)
#     return even
#
# x = find_even_numbers(list)
# print("even_number_of_list", x)
#
#
#
#
# #
# # # odd numbers
# list = [3,4,5,7,8,9,1,2,4,6]
# def find_odd_numbers(list):
#     odd = []
#     for i in list:
#         if i % 2 != 0:
#
#             odd.append(i)
#     return odd
#
# x = find_odd_numbers(list)
# print(x)
# #
#
#
#
#
# # # even/odd numbers
# number  = int(input("enter your number: "))
#
# if number % 2 == 0:
#     print("even")
#
# else:
#     print("odd")

#
#
#
#
#
# # sum_of_all_number
#
# list = [1,2,3,4,5]
#
# def sum_of_all_numbers(list):
#     total = 0
#     for i in list:
#         total += i
#     return total
#
# x = sum_of_all_numbers(list)
# print(x)
#
#
#
#
#
# #
# # # mulatiple all_numbers
# list = [2,4,2,6,100]
# def multiple_all_numbers(list):
#
#     total = 1
#     for i in list:
#         total *= i
#     return total
#
# x = multiple_all_numbers(list)
# print(x)
# #
#
#
#
#
#
# # # remove duplicate
# def remove_duplicate(list):
#     list1 = []
#     for i in list:
#         if i not in list1:
#             list1.append(i)
#     return list1
#
# print(remove_duplicate(list = [1,2,3,4,1,2,3,4,5,6,7,6,7,8,9]))
# #
#
#
#
#
#
#
# # # DICTIONARY
# # # covert two list into one dictionary
keys = ["ritu","nidhi","ridhi","kitu"]

values = [18,29,10,39]
dict_1 = dict()

for i in range(len(keys)):
    dict_1.update({keys[i]: values[i]})
print(dict_1)
#
#
#
#
#
#
#
# # # average_of_list
# list = [10,20,30,40,50]
# def average_of_list(list):
#     sum = 0
#     for i in list:
#         sum += i
#     average_value = sum / len(list)
#     return average_value
#
# x  =  average_of_list(list)
# print(x)
#
#
#
#
#
#
#
# #
# #
# # # # Python program to print all odd numbers in a range
# def all_odd_numbers(list):
#     odd = []
#     for i in range(0, 100):
#         if i % 2 != 0:
#             odd.append(i)
#     return odd
#
# print(all_odd_numbers(100))
#
#
#
#
# # # Python program to print positive numbers in a list
# def positive_number(list):
#     positive = []
#     for i in list:
#         if i >= 0:
#             # print(i)
#             positive.append(i)
#     return positive
#
#
#
# x = positive_number(list = [-3,3,9,-4,-5,3,9,-9])
# print(x)
#
#  # Python program to print nagetive numbers in a list
# def negetive_number(list):
#     negetive = []
#     for i in list:
#         if i <= 0:
#             negetive.append(i)
#     return negetive
#
# x = (negetive_number(list = [-3,3,9,-4,-5,3,9,-9]))
# print(x)
#
#
#
#
#
#
#
#
#
# #  count positive numbers
# list = [1,2,4,5,6,-4,-5,-6,7,-7]
# def count_positive_number(list):
#     positive = 0
#     for i in list:
#         if i >= 0:
#             positive += 1
#     return positive
# print(count_positive_number(list))
#
#
#
# # length_of_dictionary
#
# dict= { "math": 82, "physics": 67, "hindi":87,"english":70}
# def len_of_dic(dictionary):
#     length =  len(dict)
#     return length
#
# x = len_of_dic(dict)
# print(x)
#
#
#
#
#
#
# # average_of_dictionary
#
names = {"ritu" : 20, "ridhi" : 30, "nidhi" : 40}

def average_of_dict(names):

    total = 0
    for i in names.values():

        total = total + i
    average_value = total / len(names)
    return average_value
y = average_of_dict(names)

print("average_of_dictionary",  y)

#
#
#
#
#
# # even_number[DICTIONARY]
# #
# names = {"ritu" : 18, "ridhi" : 13, "nidhi" : 17, "sidhi" : 20}
# def even_number(names):
#     even = []
#     for i in names.values():
#         if i % 2 == 0:
#             even.append(i)
#     return even
# print(even_number(names))
# #
#
# # max_number_in_a _dictionary
#
# ages ={"dr":14, "ritu":18,"kannu":10,"babbu":8,"hiyu":7}
# def max_number_of_dict(ages):
#
#     max_age = 0
#
#     for i in ages.values():
#
#         if i > max_age:
#             max_age = i
#
#     return max_age
# print(max_number_of_dict(ages))

# min of dictionary

# dict ={"divya":14, "ritu":18,"hiyu": 7,"babbu":8,"kannu":10}
# def min_number(dict):
#     min_value = list(dict.values())[0]
#
#     for keys in dict.values():
#
#         if keys < min_value:
#             min_value = keys
#
#     return min_value
# print(min_number(dict))
# #
# #
#
#
#
#
#
#
#
# # marge two python dictionary into one
#
# dict1 = {"r": 12, 'k' : 13,"n": 10}
# dict2 = {"x": 1, "y": 2, "z": 3}
#
#
# dict3 = dict1.copy()
# dict3.update(dict2)
#
# print(dict3)
#
#
#
# # sum_of_dictionary_values
# dict = {"r":1,"k":2,"n":3}
#
# def sum_of_values(dict):
#
#     total = 0
#     for i in dict.values():
#         total += i
#     return total
#
# print(sum_of_values(dict))



# sum of key and value in pyhton dictionary
# dict = {1:2,3:4,5:5}
# def sum_of_keys_values(dict):
#     total = 0
#     sum = 0
#     for i,j in dict.items():
#         total += i
#         sum += j
#     return total, sum
#
# print(sum_of_keys_values(dict))


"""
write a python program that takesna list of name as input and return a dictionary where the keys are the name and
the values are the lengthof the corresponding names. the program should ignore any names that have a
 length less than 4 charcters.

"""
# list = ["ritu", "raj", "put", "naruka"]
#
# def get_name_length(name):
#     name_length = {}
#     for i in name:
#         if len(i) < 4:
#             name_length[i]=len(i)
#
#     return name_length
# print(get_name_length(list))
#
#






#
# # write down the max and its value in new dict
#
dict = {"ritu":4,"kitu":5,"ridhi":9,"sidhi":6}
#
def find_max_key_value_in_dictionary(dict):
    new_dict = {}
    new_list = []
    max = 0
    max_name = " "
    for i , j in dict.items():
        if j > max:
            max_name = i
            max = j


    new_dict = {max:max_name}
    new_list.append(new_dict)
    return new_list
print(find_max_key_value_in_dictionary(dict))





# list = ["ritu_naruka","kannu_naruka","divya","hiyanshi_naruka","babbu","yash"]
# def check_sername(list):
#     check = "naruka"
#     new_list = []
#     for i in list:
#         if "naruka" in i:
#             new_list.append(i)
#     return new_list
#
# print(check_sername(list))






# find min value in a list
list = [19,20,30,191,20,1,90,80]
def min_number(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min

print(min_number(list))

