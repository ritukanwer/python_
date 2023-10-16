# # QUESTION 1
# # How many students are in the dictionary? Search for the "len" function.
#
# ages = {
#     "Peter": 10,
#     "Isabel": 11,
#     "Anna": 9,
#     "Thomas": 10,
#     "Bob": 10,
#     "Joseph": 11,
#     "Maria": 12,
#     "Gabriel": 10,
# }
#
#
#
#
# def length_of_dictionary(ages):
#    length  = len(ages)
#    return length
#
# x= length_of_dictionary(ages)
# print("the length of dictionary:-",x)
#
# # #
# # #
# # QUESTION 2
# # Implement a function that receives the "ages" dictionary as parameter and returns the average age of the students.
# # Traverse all items on the dictionary using the "items" method as above.
#
#
# ages = {
#     "Peter": 10,
#     "Isabel": 11,
#     "Anna": 9,
#     "Thomas": 10,
#     "Bob": 10,
#     "Joseph": 11,
#     "Maria": 12,
#     "Gabriel": 10,
# }
#
# #
# def average_num(ages):
#     total = 0
#     for i in ages.values():
#         total += i
#
#     avg_val = total / len(ages)
#     return avg_val
#
# c = average_num(ages)
# print(c)
#
#
#
#
# # QUESTION 3
# Implement a function that receives the "ages" dictionary as parameter and returns the name of the oldest student.

ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}

# #
def oldest_person(ages):
    max_age = 0
    max_age_name= ' '
    for name, age in ages.items():
        # print(name, age)
        if age > max_age:
            max_age = age
            max_age_name= name
    return  max_age_name,max_age

x = oldest_person(ages)
print(x)
#
#
#
# #quesition 4
# # Implement a function that receives the "ages" dictionary and a number "n" and returns
# # a new dict where each student is (n) years older. For instance, new_ages(ages, 10) returns a copy of "ages" where each student is
# # 10 years older.
#
#
# def function(ages,n):
#     new_ages = {}
#     for name, age in ages.items():
#
#         if age == n:
#
#             new_ages[name] = age
#     return new_ages
#
# ages = {
#     "Peter": 10,
#     "Isabel": 11,
#     "Anna": 9,
#     "Thomas": 10,
#     "Bob": 10,
#     "Joseph": 11,
#     "Maria": 12,
#     "Gabriel": 10,
# }
# n=10
#
# x= function(ages,n)
# print(x)
#
#
# #QUESTION 5
# #How many students are in the "students" dict? Use the appropriate function.

# students = {
#     "Peter": {"age": 10, "address": "Lisbon"},
#     "Isabel": {"age": 11, "address": "Sesimbra"},
#     "Anna": {"age": 9, "address": "Lisbon"},
# }
# #
#
#
# def student_length(students):
#    length  = len(students)
#    return length
#
# a = student_length(students)
# print("students_length:-",a)

#
#
# #QUESTION 7
# #Implement a function that receives the students dict and an address,
# # and returns a list with names of all students whose address matches the address in the argument.
# # For instance, invoking "find_students(students, ’Lisbon’)" should return Peter and Anna
# students = {
#     "Peter": {"age": 10, "address": "Lisbon"},
#     "Isabel": {"age": 11, "address": "Sesimbra"},
#     "Anna": {"age": 9, "address": "Lisbon"},
# }
#
#
# def function(student, x):
#     new_dictionary = {}
#     for p, q in students.items():
#         # print(x,y)
#         for a, b in q.items():
#             if x == b:
#                 new_dictionary[p] = b
#     return new_dictionary
#
#
#
# y = function(students, x='Lisbon')
# print(y)
#
#
#
#
#
#
#
# # 6
# # Implement a function that receives the students dict and returns the average age.
# students = {
#     "Peter": {"age": 10, "address": "Lisbon"},
#     "Isabel": {"age": 11, "address": "Sesimbra"},
#     "Anna": {"age": 9, "address": "Lisbon"},
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
#
# print(average)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# num = 11
# if num > 1:
#     for i in range(2, int(num/2)+1):
#         if (num % i) == 0:
#             print(num, "false")
#             break
#     else:
#         print(num, "true")
# else:
#     print(num, "false")
#
#
#
#
#
#
#
#
#
# a = 3
# if a > 0:
#     print('A is a positive number')
#
#
#
# a = 3
# if a < 0:
#     print('A is a negative number')
# else:
#     print('A is a positive number')
#
#
#
# a = 0
# if a > 0:
#     if a % 2 == 0:
#         print('A is a positive and even integer')
#     else:
#         print('A is a positive number')
# elif a == 0:
#     print('A is zero')
# else:
#     print('A is a negative number')
#
#
#
#
# a = 0
# if a > 0 and a % 2 == 0:
#         print('A is an even and positive integer')
# elif a > 0 and a % 2 !=  0:
#      print('A is a positive integer')
# elif a == 0:
#     print('A is zero')
# else:
#     print('A is negative')
#
#
#
#
#
#
# # question :-
#
# #1
# # Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback:
# # You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# # Enter your age: 30
# # You are old enough to learn to drive.
# # Output:
# # Enter your age: 15
# # You need 3 more years to learn to
# #
#
#
# age = int(input("enter your age: "))
# if (age >= 18):
#     print("You are old enough to learn to drive.")
# elif (age == 15):
#     print("You need 3 more years to learn to drive.")
# #
# else:
#     print("not eligible to drive")
#
# #2
# # Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”)
# # to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger
# # differences, and a custom text if my_age = your_age. Output:
# # Enter your age: 30
# # You are 5 years older than me.
# age = int(input("enter your age: "))
# my_age = 25
#
# if age == my_age:
#     print("we are the same age")
# elif age > my_age:
#     print("you are", age - my_age, "years older then me" )
# else:
#     print("i am", my_age - age,"years older then you")
#
#
#
# #3
# # Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
# # Enter number one: 4
# # Enter number two: 3
# # 4 is greater than 3
#
#
#
# a = input("enter your first number: ")
# b = input("enter your second number: ")
#
# if a > b:
#     print("4 is greater than 3")
#
# else:
#     print(" 4 is less then 3")
# # 1
# # Write a code which gives grade to students according to theirs scores:
# #
# # 80-100, A
# # 70-89, B
# # 60-69, C
# # 50-59, D
# # 0-49, F
#
# mar = int(input("enter the marks"))
# if mar>=80 and mar< 100:
#     print("your gread is =", "A")
# elif  mar >=70 and mar<=79:
#     print("your gread is =","B")
# elif  mar >=60 and mar<=69:
#     print("your gread is =","C")
# elif  mar >=50 and mar<=59:
#     print("your gread is =","D")
# elif  mar >=0 and mar<=49:
#     print("your gread is =","F")
# #2
# # Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November,
# # the season is Autumn. December, January or February, the season is Winter.
# # March, April or May, the season is Spring June, July or August, the season is Summer
# month  = input("Enter season name")
# if month in ("september","october","november"):
#     print("season is :","Autumn")
# elif month in ("december", "january", "february"):
#     print("season is :", "winter")
# elif month in ("march", "april", "may"):
#     print("season is :", "spring")
# elif month in ("june", "july","august"):
#     print("season is :", "summer")
#
#
#
# #3
# fruits = ['banana', 'orange', 'mango', 'lemon']
#
# if('banana' in fruits):
#     print("That fruit already exist in the fruits list")
#
# else:
#     print("that fruit in not already exit")
#
#
# # 4
# person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
#     }
# if person['skills']:
#     print(person['skills'][len(person['skills'])//2])
#     print("python" in person['skills'])
# if ['Javascript','React'] == person['skills']:
#     print('front end developer')
# elif ['Node','MongoDB','React'] == person['skills']:
#     print('full stack developer')
# else:
#     print('unknown title')
# if person['is_marred']:
#     print(person['first_name'],person['last_name'], "lives in", person['country'],'he is married')
# else:
#     print(person['first_name'],person['last_name'], "lives in", person['country'],'he is not married')
#
#
# #     leetcode
#
# #dictionary
# # # question 1
# # # two sum
# #
# #
# # nums = [2,15,7,11]
# # target = 9
# # def sum_two_elements(nums):
# #     for i in range(len(nums)):
# #         for j in range(len(nums)):
# #             if nums[i]+nums[j] == target:
# #
# #
# #                 return[i,j]
# #
# #
# # print(sum_two_elements(nums))
# #
# #
# # nums = [2,5,6,4,5]
# # target = 6
# # def sum_two_elements(nums):
# #     for i in range(len(nums)):
# #         for j in range(len(nums)):
# #             if nums[i]+nums[j] == target:
# #
# #
# #                 return[i,j]
# #
# #
# # print(sum_two_elements(nums))
# #
# # nums = [3,3,2]
# # target = 6
# # def sum_two(nums):
# #     for i in range(len(nums)):
# #         for j in range(i+1,(len(nums))):
# #             if nums[i]+nums[j] == target:
# #
# #
# #                 return[i,j]
# #
# #
# # print(sum_two(nums))
# #
# #
# #
# #
# #add two list
# # l1 =[2,4,3]
# # l2 =[5,6,4]
# # list  = []
# # def add_two_numbers(l1,l2):
# #
# #     for i in range(len(l1)):
# #         list.append(l1[i]+l2[i])
# #
# #     return list
# # print(add_two_numbers(l1,l2))
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # # question = 4
# # # Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# # num_1 = [1,3]
# # num_2 = [2]
# # num = num_1+num_2
# # num.sort()
# # print(num)
# # def calculate_medean(num):
# #     sum = 0
# #     for i in num:
# #         sum += i
# #
# #     midean_val = sum / len(num)
# #     return midean_val
# #
# # c = calculate_medean(num)
# # print(c)
# #
# #
# #
# # num_1 = [1,2]
# # num_2 = [3,4]
# # num_3 = num_1+num_2
# # num_3.sort()
# # print(num_3)
# # def calculate_medean(num_3):
# #     sum = 0
# #     for  i in num_3:
# #         sum += i
# #     medean_value = sum/len(num_3)
# #     return medean_value
# # print(calculate_medean(num_3))
# #
# #
# #
# # #
# # #
# # # # question 7 reverse integer
# # def reverse(x):
# #
# #     if x >= 0:
# #
# #         r = int(str(x)[::-1])
# #         return r
# #
# # x = -123
# #
# # print(reverse(x))
# # def reverse(x):
# #
# #     if x >= 0:
# #
# #         r = int(str(x)[::-1])
# #         return r
# #
# # x = 120
# #
# # print(reverse(x))
# # def reverse(x):
# #
# #     if x >= 0:
# #
# #         r = int(str(x)[::-1])
# #         return r
# #
# # x = 123
# #
# # print(reverse(x))
# # #
# # #
# # #
# #
# #
# #
# #
# #
# # #
#
# def reve(x):
#     x=str(x)
#     if x[0]=='-':
#         a=x[::-1]
#         return f"{x[0]}{a[:-1]}"
#     else:
#         return x[::-1]
# x = 120
#
# print(reve(x))
# # num  = '10'
# # def string_to_interger(num):
# #     print(type(num))
# #     con_num = int(num)
# #     print(type(con_num))
# #     print(con_num)
# # print(string_to_interger(num))
# #
# #
# #
# #
# #
# #
# # #question 9 Palindrome Number
# # x = '121'
# # def palindrome(x):
# #     revers = reversed(x)
# #     if list(x) == list(revers):
# #         print('True','palindrome')
# #
# #     else:
# #         print('False','not  palindrome')
# #
# # print(palindrome(x))
# #
# #
# #
# #
# # x = '-121'
# # def palindrome(x):
# #     revers = reversed(x)
# #     if list(x) == list(revers):
# #         print('True','palindrome')
# #
# #     else:
# #         print('False','not  palindrome')
# #
# # print(palindrome(x))
# #
# # x = '10'
# # def palindrome(x):
# #     revers = reversed(x)
# #     if list(x) == list(revers):
# #         print('True','palindrome')
# #
# #     else:
# #         print('False','not  palindrome')
# #
# # print(palindrome(x))
# #13
# #
#
# # #
# # def interger_to_roman(s):
# #     roman = {'I':1,
# #              'V':5,
# #              'X':10,
# #              'L':50,
# #              'C':100,
# #              'D':500,
# #              'M':1000
# #              }
# #     n = len(s)
# #     i = n - 1
# #     sum =  0
# #     while i >= 0:
# #         if i < n-1 and roman[s[i]]<roman[s[i+1]]:
# #             sum -= roman[s[i]]
# #         sum += roman[s[i]]
# #         i -= 1
# #     return sum
# # print(interger_to_roman("III"))
# #
# #
# #
# # def interger_to_roman(s):
# #     roman = {'I':1,
# #              'V':5,
# #              'X':10,
# #              'L':50,
# #              'C':100,
# #              'D':500,
# #              'M':1000
# #              }
# #     n = len(s)
# #     i = n - 1
# #     sum =  0
# #     while i >= 0:
# #         if i < n-1 and roman[s[i]]<roman[s[i+1]]:
# #             sum -= roman[s[i]]
# #         sum += roman[s[i]]
# #         i -= 1
# #     return sum
# # print(interger_to_roman("LVIII"))
# #
# #
# # def interger_to_roman(s):
# #     roman = {'I':1,
# #              'V':5,
# #              'X':10,
# #              'L':50,
# #              'C':100,
# #              'D':500,
# #              'M':1000
# #              }
# #     n = len(s)
# #     i = n - 1
# #     sum =  0
# #     while i >= 0:
# #         if i < n-1 and roman[s[i]]<roman[s[i+1]]:
# #             sum -= roman[s[i]]
# #         sum += roman[s[i]]
# #         i -= 1
# #     return sum
# # print(interger_to_roman("MCMXCIV"))
# #
# # def roman_to_interger(num):
# #     res = ' '
# #     roman = [(1, 'I'),
# #              (5, 'V'),
# #              (10 , 'X'),
# #              (50 , 'L'),
# #              (100, 'C'),
# #              (500, 'D'),
# #              (100, 'M')
# #              ]
# #
# #
# #
# #
# # print(roman_to_interger(1520))
#
#
#
#
#
# # 12
# # def solve(num):
# #    res = ""
# #    table = [
# #       (1000, "M"),
# #       (500, "D"),
# #       (100, "C"),
# #       (50, "L"),
# #       (10, "X"),
# #       (5, "V"),
# #       (1, "I"),
# #    ]
# #    for key, value in table:
# #       d, m = divmod(num, key)
# #       res += value * d
# #       num = m
# #
# #    return res
# #
# # num = 3
# # print(solve(num))
# #
# #
# def solve(num):
#    res = ""
#    table = [
#       (1000, "M"),
#       (500, "D"),
#       (100, "C"),
#       (50, "L"),
#       (10, "X"),
#       (5, "V"),
#       (1, "I"),
#    ]
#    for key, value in table:
#       d, m = divmod(num, key)
#       res += value * d
#       num = m
#
#    return res
#
# num = 58
# print(solve(num))
#
#
# def solve(num):
#    res = ""
#    table = [
#       (1000, "M"),
#       (500, "D"),
#       (100, "C"),
#       (50, "L"),
#       (10, "X"),
#       (5, "V"),
#       (1, "I"),
#    ]
#    for key, value in table:
#       d, m = divmod(num, key)
#       res += value * d
#       num = m
#
#    return res
#
# num = 1994
# print(solve(num))
#
#
# # practice
# #  # Write a Python program to iterate over dictionaries using for loops.
# #
# def iterate(d):
#     for key, values in d.items():
#         print(key, values)
#
#
# print(iterate(d = {'Red': 1, 'Green': 2, 'Blue': 3}))
#
#
#
# D = {1 : 4, 2 : 3,  5 : 6 }
#
# sum = 0
# total = 0
# for key, valus in D.items():
#     total += valus
#     sum += key
# print(sum,total)
#
# def remove_keys(dict):
#    if 'a' in dict:
#        del dict['a']
#    return dict
# print(remove_keys(dict ={1:4,'a':3,5:6}))
#
#
# def marge_two(dict_1,dict_2):
#     x = dict_1.copy()
#     x.update(dict_2)
#     return x
# print(marge_two(dict_1={'a':8,'b':5} ,dict_2 = {'c':3,'d':8}))
#
#
#
# def already_exists(dict,x):
#     if x in dict:
#         print("already_exists")
#     else:
#         print("not_exists")
# print(already_exists(x = 32, dict = {3:10,4:7,5:9}))

#
#
# # Create a function in Python
# def name(r):
#     print(r)
# name("ritu")
#
#
# def func1(*args):
#     for i in args:
#         print(i)
#
# func1(20, 40, 60)
#
#
#
# # Check if a list contains an element. ...
# list = [1,2,3,4,5,6,7]
# print(list)
#
#
#
# def iterate(d,a):
#     for key, values in d.items():
#         for name,age in a.items():
#
#             print(key, values)
#             print(name,age)
#
#
# print(iterate(d = {'Red': 1, 'Green': 2, 'Blue': 3},a = {"q":4}))
#
# list_1 = [2,3,5,8,90]
# list_2 = [5,6,7,8,80]
# list = list_1 + list_2
# print(list)
#
#
# # Reverse a list in Python
# list = ['ritu','naruka','rajput']
# list.reverse()
# print(list)
#
# # Concatenate two lists index-wise
# li = ['ri','nar','raj']
# st = ['tu','uka','put']
# list=[]
# for i in range(len(li)):
#     list.append(li[i]+st[i])
# print(list)
#
# list = [2,3,4,5]
#
# for i in list:
#         print(i*i)
#
# list = ['ritu']
# list_2 = ['naruka']
# for i in list:
#     for j in list_2:
#         print(i + j)
#
#
#
# list = [1,2,3,4,5]
# list_2 = [3,4,5,6,7,7]
# for i in list:
#     for j in list_2:
#         print(i)
#         print(j)
#
#
# # Write a Python program to add a key to a dictionary
#
#
# def add_key(name,name_2):
#     x = name.copy()
#     x.update(name_2)
#     return x
# print(add_key(name= {"rohit": 18, "ritu": 17, "bitu": 21} ,name_2 = {"kuldeep":19}))
#
#
#
# name= {"rohit": 18, "ritu": 17, "bitu": 21}
# print(name)
# name["kuldeep"]=19
# print(name)
#
#
#
#
#
#
# # LIST EXERCISE
#
# # 1Python program to interchange first and last elements in a list
# list = [2,7,9,6]
#
# list[3] = 2
# list[0] = 6
# print(list)
#
#
# # 2 Python program to swap two elements in a list
# list = ['ritu','nidhi','ridhi','sidhi','pooja']
# list[4] = 'ridhi'
# list[2] = 'pooja'
# print(list)
#
#
# # 3Python – Swap elements in String list
# list = ['ritu','kuldeep','rohit','bitu']
# print(str(list))
#
#
# # # 4 Ways to find length of list
# list = [1,2,3,4,5,'y']
# print(len(list))
#
# # 5Maximum numbers in Python
# list = [10,20,30,40]
# def get_maximum(list):
#     max_number = 0
#     for i in list:
#         if i > max_number:
#             max_number = i
#     return max_number
# print(get_maximum(list))
#
#
# # 6Minimum  numbers in Python
# lst = [10,40,50,70,30,50,20,4,90,20]
# def get_minumum(lst):
#     min_number = lst[0]
#     for i in lst:
#         if i < min_number:
#             min_number= i
#     return min_number
# print(get_minumum(lst))
#
#
#
#
# # 7Ways to check if element exists in list
# list = [20,30,50,60]
# def exit_list(list,y):
#     if y in list:
#         print("exit")
#     else:
#         print("not_exit")
# print(exit_list(y=50,list = [20,30,50,60]))
#
#
#
# # 8Different ways to clear a list in Python
# def clear_list(list):
#     for i in list:
#         print(i)
# list = ['ritu','naruka','rajput']
# list.clear()
# print(list)
#
# # 9 Reversing a List
# def reverse_list(list):
#     for i in list[::-1]:
#         print(i)
# list = ['ritu','naruka','rajput']
# list.reverse()
# print(list)
# #
# #10 Cloning or Copying a list
#
# def Cloning(list_1):
# 	list_copy = list_1[:]
# 	return list_copy
#
#
#
# list_1 = [4, 8, 2, 10, 15, 18]
# list_2 = Cloning(list_1)
# print(list_1)
# print(list_2)
#
#
# #11  Count occurrences of an element in a list
# def count_number(lst, x):
#     count_number = 0
#     for i in lst:
#         if (i == x):
#             count_number = count_number + 1
#     return count_number
# #
# #
# #
# lst = [10,20,30,10,30,20,40,20,40,30,30]
# x = 30
# print(x,"is",count_number(lst,x),"time persent")
# #
#
# #
# # 12 Python Program to find sum and average of List in Python
# list = [10,20,30,40]
# total = 0
# for i in list:
#     total += i
# print(total)
#
#
# list = [10,20,30,40,50,50]
# def average(list):
#     total = 0
#     for i in list:
#         total += i
#
#     avg_val = total / len(list)
#     return avg_val
#
# c = average(list)
# print(c)
#
#
#
# # 13Sum of number digits in List
#
# list = [1,20,30,40,30,10]
# total = 0
#
# for i in list:
#     total+=i
# print(total)
#
# # 14   Multiply all numbers in the list
# list = [2,3,4,5]
# def multiply_list(list):
#     total = 1
#     for i in list:
#         total = total * i
#     return total
# print(multiply_list(list))
#
# #  15 Python program to find smallest number in a list
# list = [9,9,8,4,1]
# smallest = list[0]
# for i in list:
#     if i < smallest:
#         smallest = i
# print(smallest)
#
#
# # 16 Python program to find largest number in a list
# list = [50,9,9,4,5,20,90,1000]
# def largest_number(list):
#     largest_numbers = 0
#     for i in list:
#         if i > largest_numbers:
#             largest_numbers = i
#     return largest_numbers
# print(largest_number(list))
#
#
#
#
#
# # 17 Python program to find second largest number in a list
# list = [90,80,30,40,50,800]
# def second_largest_number(list):
#     second_larest = 0
#     largest = min(list)
#     for i in range(len(list)):
#         if list[i] > largest:
#             second_largest = largest
#             largest = list[i]
#         else:
#             second_largest = max(second_largest,list[i])
#     return second_largest
# print(second_largest_number(list))
#
#
#
# # 18  Python program to print even numbers in a list
# list = [10,20,5,9,90,7,58]
# def even_number(list):
#     even = []
#     for i in list:
#         if i % 2 == 0:
#             even.append(i)
#     return even
# print(even_number(list))
#
# # 19 Python program to print odd numbers in a List
# list = [10,20,5,9,90,7,58]
# def odd_numbers(list):
#     odd = []
#     for i in list:
#         if i % 2 != 0:
#             odd.append(i)
#     return odd
# print(odd_numbers(list))
# # 20  Python program to print all even numbers in a range
# def even_num(list):
#     even = []
#     for i in range(0,100):
#         if i % 2 == 0:
#             even.append(i)
#     return even
# print(even_num(100))
#
# #21 Python program to print all odd numbers in a range
# def odd_num(list):
#     odd = []
#     for i in range(0,100):
#         if i % 2 != 0:
#             odd.append(i)
#     return odd
# print(odd_num(100))
#
#
# # 22  Python program to count Even and Odd numbers in a List
# def count_odd_numbers(n):
#     odd = []
#     for i in range(n + 1):
#         if i % 2 != 0:
#             odd.append(i)
#     return odd
#
#
# print(len(count_odd_numbers(100)))
#
#
# def count_even_number(n):
#     even = []
#     for i in range(n+1):
#         if i % 2 == 0:
#             even.append(i)
#     return even
# print(len(count_even_number(100)))
#
#
#
# # 23  Python program to print positive numbers in a list
# list = [-4,-5,-3,9,3,8]
#
#
# for i in list:
#
#     if i < 0:
#         print(i,end = " ")
#
# #
# # 24Python program to print negative numbers in a list
# list1 = [-3,-4,-5,6,9,8]
# for i in list1:
#
#     if i < 0:
#         print(i,   end = " ")
#
# #  25 Python program to print all positive numbers in a range
#
# def positive_number(list):
#     positive = 0
#     for i in range(-3,3):
#         if i >= 0:
#             positive += 1
#
#     return positive
# print(positive_number(3))
# #   26  Python program to print all negative numbers in a range
#
# def negetive_number(list):
#     negetive = 0
#     for i in range(-9,2):
#         if i <= 0:
#             negetive += 1
#
#
#     return negetive
# print(negetive_number(2))
#
#
#
# # 27 Python program to count positive and negative numbers in a list
# list = [1,2,4,5,6,-4,-5,-6,7,-7]
# def count_negetive_number(list):
#     negetive = 0
#     for i in list:
#         if i <= 0:
#             negetive += 1
#     return negetive
# print(count_negetive_number(list))
#
#
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
#
#
# # 28 Remove multiple elements from a list in Python
# list1 = [11, 5, 17, 18, 23, 50,37 ,90, 77]
#
#
# for ele in list1:
#     if ele % 2 == 0:
#         list1.remove(ele)
#
# print(list1)
#
# # 29 Remove empty tuples from a list
# tuples = [(),('ritu'),(),('naruka')]
# def Remove(tuples):
#     for i in tuples:
#         if (len(i) == 0):
#             tuples.remove(i)
#     return tuples
#
#
#
# print(Remove(tuples))
#
#
# # 30 Program to print duplicates from a list of integers
#
# list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 7, 8, 9, 9]
# x = []
# y = []
# for i in list:
#     if i not in x:
#         x.append(i)
# for i in x:
#     if list.count(i) > 1:
#         y.append(i)
# print(y)
#
# #
# # d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# # print(d)
# # sorted_d = sorted(d.items())
# # print(sorted_d)
# # sorted_d = dict( sorted(d.items(),reverse=True))
# # print(sorted_d)
#
#
# # dictionary =  {0: 10, 1: 20}
# # dictionary_2 = {2:30}
# # def add_key_dictionary(dictionary,dictctionary_2):
# #     for key,values in dictionary.items():
# #         for a,b in dictionary_2.items():
# #             print(key,value)
# #             print(a,b)
# # print(add_key_dictionary(dictionary = {0:10,1:20},dictionary_2 = {2:30}))
# # print(iterate(d = {'Red': 1, 'Green': 2, 'Blue': 3},a = {"q":4}))
#
#
#
#
#
# # dictionary exerscise
# # question 1
# dictionary = {
#     5: 'e',
#     4: 'd',
#     3: 'c',
#     2: 'b',
#     1: 'a',
# }
# sorted_dictionary = {}
# for key,value in sorted(dictionary.items()):
#     sorted_dictionary[key]=value
# print(sorted_dictionary)
#
# #2
# def add_key(dict_1,dict_2):
#     x = dict_1.copy()
#     x.update(dict_2)
#     return x
# print(add_key(dict_1 = {0:10,1:20},dict_2 = {2:30}))
#
#
# # # 3
# # def add_key(dict_1,dict_2,dict_3):
# #     x =( dict_1,dict_2.copy())
# #     x.update(dict_3)
# #     return x
# # print(add_key(dict_1={1:10, 2:20}, dict_2={3:30, 4:40}, dict_3={5:50,6:60}))
#
# dict_0 = {'a':1, 'b':2, 'c':3}
# dict_1 = {'a':1, 'd':2, 'c':'foo'}
# dict_2 = {'e':57,'c':3}
#
# # super_dict = {'a':[1], 'b':[2], 'c':[3,'foo'], 'd':[2], 'e':[57]}
# # I wrote the following code:
# def add_three_dic(dictionary):
#     dictionary = {}
#     for d in dict_0:
#         for k, v in d.items():
#             if dictionary.get(k) is None:
#                 dictionary[k] = []
#             if v not in dictionary.get(k):
#                 dictionary[k].append(v)
#
# print(add_three_dic(dictionary))
#
#
# # list practice
# #Declare an empty list
# empty_list = []
# print(len(empty_list))
#
# #Declare a list with more than 5 items
# names = ['ritu','seema','ranu','riya','ridhi']
# print(names)
#
#
#
# #Find the length of your list
# list = ['ritu','seema','ranu','riya','ridhi']
# print(len(list))
#
#
#
#
# #Get the first item, the middle item and the last item of the list
# list = ['ritu','seema','ranu','riya','ridhi']
#
# first_list = list[0]
# print(first_list)
# middle_list = list[2]
# print(middle_list)
# last_name = list[-1]
# print(last_name)
#
#
#
#
#
#
# # Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# print(it_companies)
#
#
#
#
# #Print the list using print()
# list = []
# print(list)
#
#
#
#
#
#
# #Print the number of companies in the list
# company = ['google','amazon','vivo','facebook','Mi']
# print(len(company))
#
#
#
# #Print the first, middle and last company
# company = ['google','amazon','vivo','facebook','Mi']
# first_company = company[0]
# print(first_company)
# middle_company = company[2]
# print(middle_company)
# last_company = company[-1]
# print(last_company)
#
#
# #Print the list after modifying one of the companies
# company = ['google','amazon','vivo','facebook','Mi']
# company[0] = 'apple'
# print(company)
#
#
# #Add an IT company to it_companies
# it_companies = ['apple','microsoft','google','IBM','dell']
#
# it_companies.append('intl')
# print(it_companies)
#
#
# #Insert an IT company in the middle of the companies list
# it_companies = ['apple','microsoft','google','IBM','dell']
# middle_company = it_companies[2] = ('Intl')
# print(it_companies)
#
#
# #Change one of the it_companies names to uppercase (IBM excluded!)
# it_companies = ['apple','microsoft','google','IBM','dell']
# it_companies = [i.upper() for i in it_companies]
# print(it_companies)
#
#
# #Join the it_companies with a string '#;  '
# list_1 = ['vivo','microsoft','facebook']
# list_2 = ['mi','google']
# companies = list_1 + list_2
# print(companies)
#
#
# #Check if a certain company exists in the it_companies list.
# it_company = ['apple','microsoft','google','IBM','dell']
# does_exist = 'apple' in it_company
# print(does_exist)
#
#
#
# #Sort the list using sort() method
# name = ['priya','ridhi','tiya','sidhi','nidhi']
# name.sort()
# print(name)
#
#
#
# list = [90,70,80,30,50]
# list.sort()
# print(list)
#
#
#
#
# #Reverse the list in descending order using reverse() method
# list = [20,90,80,70,30]
# list.reverse()
# print(list)
#
#
# #Slice out the first 3 companies from the list
# it_companies = ['apple','microsoft','google','IBM','dell','intel']
# del it_companies[0:3]
# print(it_companies)
#
#
# #Slice out the last 3 companies from the list
# it_companies = ['apple','microsoft','google','IBM','dell','intel']
# del it_companies[-3:]
# print(it_companies)
#
#
# #Slice out the middle IT company or companies from the list
# it_companies = ['apple','microsoft','google','IBM','dell']
# del it_companies[2:3]
# print(it_companies)
#
# #Remove the first IT company from the list
# it_companies = ['apple','microsoft','google','IBM','dell']
# it_companies.remove('apple')
# print(it_companies)
#
# #Remove the middle IT company or companies from the list
# it_companies = ['apple','microsoft','google','IBM','dell']
# it_companies.remove('google')
# print(it_companies)
#
#
#
# #Remove the last IT company from the list
# it_companies = ['apple','microsoft','google','IBM','dell']
# it_companies.pop()
# print(it_companies)
#
#
#
#
#
# #Remove all IT companies from the list
# it_companies = ['apple','microsoft','google','IBM','dell']
# it_companies.clear()
# print(it_companies)
#
# #Destroy the IT companies list
# it_companies = ['apple','microsoft','google','IBM','dell']
# del it_companies[0:5]
# print(it_companies)
#
#
# #Join the following lists:
# # front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# # back_end = ['Node','Express', 'MongoDB']
#
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
# front_end.extend(back_end)
# print(front_end)
#
#
#
# #Find the middle country(ies) in the countries list
#
# countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
# middle_country = ['Finland']
# print(middle_country)
#
# #['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
#
# list = ['china','russia','usa','finland','sweden','norway','denmark']
# china,russia,usa,finland,*scandic,es = list
# print('china')
# print(russia)
# print(usa)
# print(finland)
# print(scandic)
# print(es)
#
#
# # function
# # # functions
# # 1# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
# def add_two_numbers ():
#     number_one = 50
#     number_two = 80
#     total = number_one + number_two
#     print(total)
# add_two_numbers()
# #
# # 2#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
# def area_of_circle (r):
#     PI = 3.14
#     area = PI * r ** 2
#     return area
# print(area_of_circle(16))
#
# #
# #
# # 3#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
# # Check if all the list items are number types. If not do give a reasonable feedback.
# #
# def add_all_nums(nums):
#     total = 0
#     for i in nums:
#         total += i
#     return total
# # print(add_all_nums(2, 3, 5))
# print(area_of_circle(10))
#
#
#
# # 4Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
# # Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) +32
# print(celsius_to_fahrenheit(2))
#
#
#
# # 5Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
# def  check_season(month):
#     if month in ['september','october','november']:
#         print('autumn')
#     if month in ['december','january','fabruary']:
#         print('winter')
#     if month in ['march','april','may']:
#         print('spring')
#     if month in ['june', 'july', 'august']:
#         print('summer')
#
#     # else:
#     #     print('summer')
# print(check_season('november'))
#
# #6Write a function called calculate_slope which return the slope of a linear equation
# def calculate_slope(x1, x2, y1, y2):
#     m = (y2 - y1) / (x2 - x1)
#     return m
# print(calculate_slope(10,20,50,70))
#
#
#
# #8
# # Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
#
# n = [3,5,7]
#
# def print_list(x):
#     for i in range(0,len(x)):
#         print (x[i])
# print_list(n)
#
#
#
# # 9
# # Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# # print(reverse_list([1, 2, 3, 4, 5]))
# # # [5, 4, 3, 2, 1]
# # print(reverse_list1(["A", "B", "C"]))
# # # ["C", "B", "A"]
# def reverse_of_list(reverse_list):
#     for i in reverse_list[::-1]:
#         print(i)
# reverse_list = [1,2,3,4,5,6]
# reverse_list.reverse()
# print(reverse_list)
#
#
#
# def reverse_of_list(reverse_list):
#     for i in reverse_list[::-1]:
#         print(i)
# reverse_list = ["A","B","C"]
# reverse_list.reverse()
# print(reverse_list)
#
#
#
#
#
# #10  Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
#
# list = ['ritu','naruka']
# def capiatl_list_items(list):
#     for i in list:
#         list[list.index(i)] = i.capitalize()
#     return list
# print(capiatl_list_items(list))
#
#
#
# # 11Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# # food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# # print(add_item(food_staff, 'Meat'))
# # numbers = [2, 3, 7, 9];
# # print(add_item(numbers, 5))
# def add_items(food_staff):
#
#     for i in food_staff:
#         return i
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# food_staff.append('orange')
# print(food_staff)
#
#
#
# def add_items(numbers):
#     for i in numbers:
#         return i
#
# numbers = [2,3,7,9]
# numbers.append(5)
# print(numbers)
#
#
#
# # 12
# # Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# # food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# # print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# # numbers = [2, 3, 7, 9];
# # print(remove_item(numbers, 3))  # [2, 7, 9]
# #
# #
# def removed_items(food_staff):
#     for i in food_staff:
#         return i
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# food_staff.remove('Mango')
# print(food_staff)
#
#
# def removed_items(numbers):
#     for i in food_staff:
#         return i
# numbers = [2,3,7,9]
# numbers.remove(3)
# print(numbers)
#
#
#
# # 13
# # Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# # print(sum_of_numbers(5))  # 15
# # print(sum_all_numbers(10)) # 55
# # print(sum_all_numbers(100)) # 5050
# #
#
# def sum_of_numbers(n):
#     total = 0
#     for i in range(n+1):
#         total+=i
#     print(total)
# print(sum_of_numbers(5))
# print(sum_of_numbers(10))
# print(sum_of_numbers(100))
#
#
# # 15Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
# def add_of_evens(n):
#     evens = []
#     for i in range(n + 1):
#         if i % 2 == 0:
#             evens.append(i)
#     return evens
# print(add_of_evens(10))
# add_even_number = [0+2+4+6+8+10]
# print(add_even_number)
#
#
#
# # #14Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
# def add_of_odd(n):
#     odd = []
#     for i in range(n + 1):
#         if i % 2 != 0:
#             odd.append(i)
#     return odd
# print(add_of_odd(10))
# add_odd_numbers = [1+3+5+7+9]
# print(add_odd_numbers)
# #level 2Declare a function named evens_and_odds . It takes a positive integer
# # as parameter and it counts number of evens and odds in the number.
# #     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.
#
#
#
# # 1Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
# #     print(evens_and_odds(100))
# #     # The number of odds are 50.
# #     # The number of evens are 51.
# def add_of_odd(n):
#     odd = []
#     for i in range(n + 1):
#         if i % 2 != 0:
#             odd.append(i)
#     return odd
#
# all_odd_numbers = add_of_odd(100)
# print(len(all_odd_numbers))
#
#
#
# def add_of_evens(n):
#     evens = []
#     for i in range(n + 1):
#         if i%2 == 0:
#             evens.append(i)
#     return evens
# all_evens_numbers = add_of_evens(100)
# print(len(all_evens_numbers))
#
# #2
# # #Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
# def fectorial(a):
#     b = 1
#     for i in range(a + 1):
#         b *= 1
#     return a
# print(fectorial(1))
# #3Call your function is_empty, it takes a parameter and it checks if it is empty or not
# def is_empty(check):
#     if check:
#         return True
#     else:
#         return False
# print(is_empty(90))
#
#
#
# #4Write different functions which take lists.
# # They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
# list = [10,20,30, 50, 40, 50]
# def calculate_mean(list):
#
#     return sum(list)/len(list)
# c = calculate_mean(list)
# print(c)
# #
# #
# list = [10, 20, 30, 50 ,40 ,50]
# def calculate_midean(list):
#     data = sorted(list)
#     index = len(data)//2
#     if len(list)%2 != 0:
#         return data[index]
#     return (data[index - 1] + data[index])/ 2
# a = calculate_midean(list)
# print(a)
#
# list = [10,20,30,50,40,50]
# def calculate_mode(list):
#     mode = max(list,key = list.count)
#     return mode
# print(calculate_mode(list))
#
#
#
# for i in range(10):
#     print(i)
#
#
#
# list =  [10,20]
# def variance(list):                                                #[10,20 close 15
#     n = len(list)                                                  #(10-15)**2+(20-15)**2/2
#     mean = sum(list)/n                                          #   25+25/2 = 25]
#     deviations = [(x - mean)**2for x in list]
#     variance = sum(deviations)/n
#     return variance
# print(variance(list))
#
#
#
# list = [10,20]
#
# def standard_deviation(list):
#
#     n = len(list)
#     mean = sum(list) / n
#     deviations = [(x - mean) ** 2 for x in list]
#     variance = sum(deviations) / n
#     standard_deviation = variance ** 0.5
#     return standard_deviation
# print(standard_deviation(list))
#
#
#
#
#
# # level 3
# # 1 Write a function called is_prime, which checks if a number is prime.
# def is_prime(n):
#     for i in range(2,n):
#         if (n%i) == 0:
#             return True
#         return False
# #
# print(is_prime(4))
#
#
#
# # 2
# # Write a functions which checks if all items are unique in the list.
# list = ['apple','banana','orange']
# def function(list):
#
#     if (len(set(list)) == len(list)):
#         print("all elements are unique")
#     else:
#         print("all elements  are not unique")
# print(list)
#
#
# # 3Write a function which checks if all the items of the list are of the same data type.
# list = [1,2,3,4,5,6]
# def check_list(list):
#     return len(set(list)) == 1
# list = [1, 1]
# if check_list(list) == True:
#     print('same')
# else:
#     print('not same')
#
#
# # loop_practice
# # count = 0
# # while count < 5:
# #     print(count)
# #     count = count + 1
#
# # count = 0
# # while count < 5:
# #     print(count)
# #     count = count + 1
# # else:
# #     print(count)
# #
# #
# # count = 0
# # while count < 5:
# #     print(count)
# #     count = count + 1
# #     if count == 3:
# #         break
#
#
# #
# # count = 0
# # while count < 5:
# #     if count == 4:
# #         continue
# #     print(count)
# #     count = count + 1
#
#
# # numbers = [0, 1, 2, 3, 4, 5]
# # for number in numbers:
# #     print(number)
#
# #
# #
# # language = 'Python'
# # for letter in language:
# #     print(letter)
# #
# #
# # for i in range(len(language)):
# #     print(language[i])
#
#
# # numbers = [0, 1, 2, 3, 4, 5]
# # for number in numbers:
# #     print(number)
#
#
# #
# # person = {
# #     'first_name':'Asabeneh',
# #     'last_name':'Yetayeh',
# #     'age':250,
# #     'country':'Finland',
# #     'is_marred':True,
# #     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
# #     'address':{
# #         'street':'Space street',
# #         'zipcode':'02210'
# #     }
# # }
# #
# #
# # for key, value in person.items():
# #      print(key, value)
#
#
# # it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# # for company in it_companies:
# #     print(company)
#
# # numbers = (0,1,2,3,4,5)
# # for number in numbers:
# #     print(number)
# #     if number == 3:
# #         break
#
# # numbers = (0,1,2,3,4,5)
# # for number in numbers:
# #     print(number)
# #     if number == 3:
# #         continue
# #     print('Next number should be ', number + 1)\
# #         if number != 5 else print("loop's end")
# # print('outside the loop')
#
# # lst = list(range(11))
# # print(lst)
#
# # st = set(range(1, 11))
# # print(st)
# #
# # lst = list(range(0,11,2))
# # print(lst)
# # st = set(range(0,11,2))
# # print(st)
#
# # for number in range(11):
# #     print(number)
#
# # person = {
# #     'first_name': 'Asabeneh',
# #     'last_name': 'Yetayeh',
# #     'age': 250,
# #     'country': 'Finland',
# #     'is_marred': True,
# #     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
# #     'address': {
# #         'street': 'Space street',
# #         'zipcode': '02210'
# #     }
# # }
# # for key in person:
# #     if key == 'skills':
# #         for skill in person['skills']:
# #             print(skill)
# #
# # for number in range(11):
# #     print(number)
# # else:
# #     print('The loop stops at', number)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #quesions()
# #
# #
# #
# # 1
# for i in range(0,10):
#     print(i)
#     k = 0
#     while k <= 10:
#
#         k += 1
# # #2
# for i in range(10,-1,-1):
#     print(i)
#     k = 10
#     while k >= 10:
#
#         k -= 1
# #3
# def seven_calls(hash):
#     hash = '#'
#     for i in range(1,9):
#         print(hash * i)
# a = seven_calls(hash)
# #4
# def functions(hash):
#     hash = "#"
#     for i in range(1,9):
#         for j in range(1,9):
#             print("#", end = '')
#         print()
#
# x = functions(hash)
#
#
#
#
# #5
# first = [0,1,2,3,4,5,6,7,8,9,10]
# for i in first:
#
#         print(i, " x", i, "=", i * i)
#
# #6
# for i in  ['Python', 'Numpy','Pandas','Django', 'Flask']:
#     print(i)
#
# #
# #7
# def find_even_numbers(lst):
#     evens = []
#     for i in range(0,100):
#         if i % 2 == 0:
#             evens.append(i)
#     return evens
# print(find_even_numbers(list))
#
# # 8
# def find_odd_numbers(lst):
#     odd = []
#     for i in range(0,100):
#         if i % 2 != 0:
#             odd.append(i)
#     return odd
# print(find_odd_numbers(list))
#
#
#
# #level 2
# # 1
# def sum_of_numbers(n):
#     total = 0
#     for i in range(n+1):
#         total+=i
#     print(total)
#
# print(sum_of_numbers(100))
#
#
#
# #2
# def sum_of_even(lst):
#     even = 0
#     for i in range(0,101):
#         if i % 2 == 0:
#             even += i
#     return even
# print(sum_of_even(list))
#
# def sum_of_odd(lst):
#     odd = 0
#     for i in range(0,101):
#         if i % 2 != 0:
#             odd += i
#     return odd
# print(sum_of_odd(list))
#
#
#
#
# # # level 3
# list = ['banana', 'orange', 'mango', 'lemon']
# def reverse_list(list):
#
#         return list[::-1]
#
# print(reverse_list(list))
#
# # dictionary_practice
# # Create an empty dictionary called dog
# dictionary = {}
# print("empty dictionary", dictionary)
# #first i make a empty dictionary. then i print a "empty sictonary" and i use comma and run this.
# # then my answer empty dictionary{} in came.
# #
#
#
# dog = {
#     'name':'tomy',
#     'ages': 8,
#     'breed':'german',
#     'color':'black'
# }
# print(dog)
# # fir i make a dog name variable then i enter dictionary acording to question.
# # then i print(dog)
#
#
#
#
#
# student = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'gender':'male',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
#     }
# print(student)
#
#
#
#
#
# # Get the length of the student dictionary
# students =  {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'gender':'male',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
# }
# print(len(students))
#
#
#
# student = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
# }
# print(type(student))
# # Get the value of skills and check the data type, it should be a list
# #first i make a student name dictionary. then i print type of values .
# # then my answer is dictionary
#
#
#
# student = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#         }
# }
#
# student['skills'].append('c+')
# student['skills'].append('HTML')
# print(student)
# # Modify the skills values by adding one or two skills
# # first i make a students name dictionary then i  add two values  in skills.
# # so i did student ['skills'].append('c+' and 'HTML') then  i print this and result
# # is ['JavaScript', 'React', 'Node', 'MongoDB', 'Python','c+','HTML']
#
# student = {
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'gender': 'male',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }
# keylist = list(student.keys())
# print(keylist)
# # Get the dictionary keys as a list
# # first i make students name dictionary then question ask students key
# # then keylist = list(studen.key) ten i print this .
#
#
# student = {
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'gender': 'male',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }
#
# print(list(student.values()))
# # Get the dictionary values as a list
#
# # first i make a student name dictionary then then i entry dictionary detailsthen i print
# # list students values .
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# student = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
#     }
# list = list(student.items())
# print(list)
#
#
#
#
#
#
# student = {
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'gender': 'male',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }
# student.pop('last_name')
# print(student)
#
#
#
#
#
# student = {
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'gender': 'male',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
#     }
# del student['skills']
# print(student)

# python_course
#
#
# variable_1 = 120
# print(variable_1)
#
#
# variable_2 = 2.34
# print(variable_2)
#
#
# var_1 = 20
# var_2 = 30
# if var_1 > var_2:
#     print("False")
# else:
#     print("True")
# #
# # # 8
# # Create a variable and assign it the sum of two integers
# var_1 = 20
# var_2 = 30
# var = var_1 + var_2
# print(var)
#
#
# # Create a variable and assign it the difference of two integers
#
# var_1 = 30
# var_2 = 20
# var = var_1 - var_2
# print(var)
#
# # Create a variable and assign it the result of one integer being divided by another integer
# var_1  = 90
# var = var_1/3
# print(var)
#
# # Create a variable and assign it the product of two integers
#
#
# var_1 = 80
# var_2 = 90
# var = var_1 * var_2
# print(var)
# #Create a variable and assign it the result of 3 raised to the 8th power
# var = 3**8
# print(var)
#
# Create a variable and assign it the result of 10 floor division 3
var_1 = 10
var = var_1 // 3
print(var)



# 27ex.

# q1 What is your name?
# name = input("what is your name")
# print("my name is", name ,'.')

# quest = input("what is your quest")
# print("my quest is", quest,".")
# print(type(quest))
#
#
# color = input("what is your fav color")
# print("my fav color is",color,".")
# print(str)

# 30ex.
# number =int(input("enter your number"))
# print(number + 10)


# ex 33


# Create a function called hello_world_printer() which takes no parameters and prints the string "hello world"
# def hello_world_printer():
#     print("hello_world")
# hello_world_printer()


# ex 35
# Create a variable called name and assign it user input().  input()'s message should ask the user to enter their name.
# def name_printer(user_name):
#     print(user_name)
# name = input("Please enter your name.")
# name_printer(name)



# # ex 37
# length = int(input("Enter length in feet."))
# width = int(input("Enter width in feet."))
# height = int(input("Enter height in feet."))
#
#
# def prism_vol(l, w, h):
#     return l * w * h
#
#
# print("The volume of the rectangular prism is " + str(prism_vol(length, width, height)) + " cubic feet.")

#
# score = int(input("Please enter the student's score. "))
#
# if score >= 90:
#     print("This student's score of " + str(score) + " is an A.")
# else:
#     if score >= 80:
#         print("This student's score of " + str(score) + " is a B.")
#     else:
#         if score >= 70:
#             print("This student's score of " + str(score) + " is a C.")
#         else:
#             if score >= 60:
#                 print("This student's score of " + str(score) + " is a D.")
#             else:
#                 print("This student's score of " + str(score) + " is a F.")


# user_str = input("Please enter a string.")
#
# count = 0
# for char in user_str:
#     count += 1
#
# print(user_str)
# print(count)

#
# for key, value in {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant").items():
#     print(key, value)
#
# fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
# print(fast_food_items.pop("McDonald's"))
#
# fast_food_items.popitem()
# print(fast_food_items)


# internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
# another_one = {"shroud": "Twitch"}
# internet_celebrities.update(another_one)  # 2
# gamers = internet_celebrities.copy()  # 3
# internet_celebrities.clear()  # 4
# print(internet_celebrities)  # 5
# print(gamers)