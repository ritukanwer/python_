# first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True
#
# print(first_name, last_name, country, age, is_married)
# print('First name:', first_name)
# print('Last name: ', last_name)
# print('Country: ', country)
# print('Age: ', age)
# print('Married: ', is_married)
#
#
#
# # oprators
#
# a = 1
# b = 2
#
#
#
# sum = a +b
# diff = a - b
# multipl = a * b
# division = a /b
# remainder = a % b
# floor_dicision = a // b
# exponential = a ** b
# print(sum)
# print(diff)
# print(multipl)
# print(division)
# print(remainder)
# print(floor_dicision)
# print(exponential)
#
# num_one = 3
# num_two = 4
#
# total = num_one + num_two
# diff = num_two - num_one
# product = num_one * num_two
# div = num_two / num_two
# remainder = num_two % num_one
#
#
# print('total: ', total)
# print('difference: ', diff)
# print('product: ', product)
# print('division: ', div)
# print('remainder: ', remainder)
#
#
# # area of circle
# radius = 10
# area_of_circle = 3.14 * radius ** 2
# print("area of circle : " ,area_of_circle)
#
#
# # area of rectangle
# len = 10
# width = 20
# area_of_rectangle = len * width
# print("area_of_rectangle:",area_of_rectangle)
#
#
# # Calculating a weight of an object
# mass = 75
# gravity  =9.81
# weight = mass * gravity
# print(weight)
#
#
# print(3 > 2)
# print(3 >= 2)
# print(3 < 2)
# print(2 < 3)
# print(2 <= 3)
# print(3 == 2)
# print(3 != 2)

# print(3 > 2 and 4 > 3)
# print(3 > 2 and 4 < 3)
# print(3 < 2 and 4 < 3)
# print(3 > 2 or 4 > 3)
# print(3 > 2 or 4 < 3)
# print(3 < 2 or 4 < 3)
# print(not 3 > 2)



##string
# letter = 'P'
# print(letter)
# print(len(letter))
# greeting = 'Hello, World!'
# print(greeting)
# print(len(greeting))
# sentence = "I hope you are enjoying 30 days of python challenge"
# print(sentence)
# print(len(sentence))


# multiline_string = """I am a teacher and enjoy teaching.
# I didn't find anything as rewarding as empowering people.
# That is why I created 30 days of python."""
# print(multiline_string)
#
# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# space = ' '
# full_name = first_name  +  space + last_name
# print(full_name)
# print(len(first_name))
# print(len(last_name))
# print(len(first_name) > len(last_name))
# print(len(full_name))

# language = 'Python'
# a,b,c,d,e,f = language
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

# language = 'Python'
# first_letter = language[0]
# print(first_letter)
# second_letter = language[1]
# print(second_letter)
#
# last_letter = language[-1]
# print(last_letter)

#
# language = 'Python'
# first_three = language[0:3]
# print(first_three)
# last_three = language[3:6]
# print(last_three)
# last_three = language[-3:]
# print(last_three)
# last_three = language[3:]
# print(last_three)
#
#
# language = 'Python'
# pto = language[0:6:2]
# print(pto)


# print('I hope every one enjoying the python challenge.\nDo you ?') # line break
# print('Days\tTopics\tExercises')
# print('Day 1\t3\t5')
# print('Day 2\t3\t5')
# print('Day 3\t3\t5')
# print('Day 4\t3\t5')
#
#
#
# challenge = 'thirty days of python'
# print(challenge.capitalize())

# challenge = 'thirty days of python'
# print(challenge.count('y'))
# print(challenge.count('y', 7, 14))
# print(challenge.count('th'))


# challenge = 'thirty days of python'
# print(challenge.endswith('on'))
# print(challenge.endswith('tion'))
#
# challenge = 'thirty\tdays\tof\tpython'
# print(challenge.expandtabs())
# print(challenge.expandtabs(10))
#
#
# challenge = 'thirty days of python'
# print(challenge.find('y'))
# print(challenge.find('th'))

# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# job = 'teacher'
# country = 'Finland'
# sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
# print(sentence)


# radius = 10
# pi = 3.14
# area = pi
# result = 'The area of circle with {} is {}'.format(str(radius), str(area))
# print(result)

# # isalnum(): Checks alphanumeric character
# #
# challenge = 'ThirtyDaysPython'
# print(challenge.isalnum())
#
# challenge = '30DaysPython'
# print(challenge.isalnum())
#
# challenge = 'thirty days of python'
# print(challenge.isalnum())
#
# challenge = 'thirty days of python 2019'
# print(challenge.isalnum())
# # isalpha(): Checks if all characters are alphabets
#
# challenge = 'thirty days of python'
# print(challenge.isalpha())  # True
# num = '123'
# print(num.isalpha())  # False
#
# # isdecimal(): Checks Decimal Characters
#
# challenge = 'thirty days of python'
# print(challenge.find('y'))  # 5
# print(challenge.find('th'))  # 0
#
# # isdigit(): Checks Digit Characters
#
# challenge = 'Thirty'
# print(challenge.isdigit())
# challenge = '30'
# print(challenge.isdigit())
#
# # isdecimal():Checks decimal characters
#
# num = '10'
# print(num.isdecimal())
# num = '10.5'
# print(num.isdecimal())
#
# # isidentifier():Checks for valid identifier means it check if a string is a valid variable name
#
# challenge = '30DaysOfPython'
# print(challenge.isidentifier())
# challenge = 'thirty_days_of_python'
# print(challenge.isidentifier())
#
# # islower():Checks if all alphabets in a string are lowercase
#
# challenge = 'thirty days of python'
# print(challenge.islower())
# challenge = 'Thirty days of python'
# print(challenge.islower())
#
# # isupper(): returns if all characters are uppercase characters
#
# challenge = 'thirty days of python'
# print(challenge.isupper())
# challenge = 'THIRTY DAYS OF PYTHON'
# print(challenge.isupper())
#
# # isnumeric():Checks numeric characters
#
# num = '10'
# print(num.isnumeric())
# print('ten'.isnumeric())
#
# # join(): Returns a concatenated string
#
# web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
# result = '#, '.join(web_tech)
# print(result)
#
# # strip(): Removes both leading and trailing characters
#
# challenge = ' thirty days of python '
# print(challenge.strip('y'))
#
# # replace(): Replaces substring inside
#
# challenge = 'thirty days of python'
# print(challenge.replace('python', 'coding'))
#
# # split():Splits String from Left
#
# challenge = 'thirty days of python'
# print(challenge.split())
#
# # title(): Returns a Title Cased String
#
# challenge = 'thirty days of python'
# print(challenge.title())
#
# # swapcase(): Checks if String Starts with the Specified String
#
# challenge = 'thirty days of python'
# print(challenge.swapcase())
# challenge = 'Thirty Days Of Python'
# print(challenge.swapcase())
#
# # startswith(): Checks if String Starts with the Specified String
#
# challenge = 'thirty days of python'
# print(challenge.startswith('thirty'))
# challenge = '30 days of python'
# print(challenge.startswith('thirty'))



# #list
# empty_list = list()
# print(len(empty_list))
#
# fruits = ['banana', 'orange', 'mango', 'lemon']
# vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
# animal_products = ['milk', 'meat', 'butter', 'yoghurt']
# web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB']
# countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
#
# print(fruits)
# print(len(fruits))
# print(vegetables)
# print(len(vegetables))
# print(animal_products)
# print(len(animal_products))
# print(web_techs)
# print(len(web_techs))
# print(len(countries))

#
# fruits = ['banana', 'orange', 'mango', 'lemon']
# first_fruit = fruits[0]
# print(first_fruit)
# second_fruit = fruits[1]
# print(second_fruit)
# last_fruit = fruits[3]
# print(last_fruit)
# last_index = len(fruits) - 1
# last_fruit = fruits[last_index]
#
#
# fruits = ['banana', 'orange', 'mango', 'lemon']
# last_fruit = fruits[-1]
# second_last = fruits[-2]
# print(last_fruit)
# print(second_last)



#
# fruits = ['banana', 'orange', 'mango', 'lemon']
# all_fruits = fruits[0:4]
#
# all_fruits = fruits[0:]
# print(all_fruits)
# orange_and_mango = fruits[1:3]
#
# print(orange_and_mango)
# orange_mango_lemon = fruits[1:]
# print(orange_mango_lemon)

# fruits = ['banana', 'orange', 'mango', 'lemon']
# all_fruits = fruits[-4:]
# print(all_fruits)
# orange_and_mango = fruits[-3:-1]
# print(orange_and_mango)
# orange_mango_lemon = fruits[-3:]
# print(orange_mango_lemon)


#
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits[0] = 'papaya'
# print(fruits)
# fruits[1] = 'apple'
# print(fruits)
# fruits[-1] = 'lime'
# print(fruits)
#


# fruits = ['banana', 'orange', 'mango', 'lemon']
#
# if 'mango' in fruits:
#     print('True')
# else:
#     print('false')
#
# if 'apple' in fruits:
#     print('True')
# else:
#     print('false')



#
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.append('apple')
# print(fruits)
# fruits.append('lime')
# print(fruits)

#
# # insert  apple between orange and mango
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.insert(2, 'apple')
# print(fruits)
# fruits.insert(3, 'lime')
# print(fruits)



# ## remove
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.remove('banana')
# print(fruits)
# fruits.remove('lemon')
# print(fruits)
#
#
# # #pop
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.pop()
# print(fruits)
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.pop(0)
# print(fruits)

#
# # del
# fruits = ['banana', 'orange', 'mango', 'lemon']
# del fruits[0]
# print(fruits)
#
# del fruits[1]
# print(fruits)
#
#
#
# # clear
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.clear()
# print(fruits)


# #copying a lits

# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits_copy = fruits.copy()
# print(fruits_copy)
#
# # join
# positive_numbers = [1, 2, 3,4,5]
# zero = [0]
# negative_numbers = [-5,-4,-3,-2,-1]
# integers = negative_numbers + zero + positive_numbers
# print(integers)
#
# fruits = ['banana', 'orange', 'mango', 'lemon']
# vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
# fruits_and_vegetables = fruits + vegetables
# print(fruits_and_vegetables )

# ## join with extend
# num1 = [0, 1, 2, 3]
# num2= [4, 5,6]
# num1.extend(num2)
# print(num1)
# negative_numbers = [-5,-4,-3,-2,-1]
# positive_numbers = [1, 2, 3,4,5]
# zero = [0]
#
# negative_numbers.extend(zero)
# negative_numbers.extend(positive_numbers)
# print(negative_numbers)
#
# fruits = ['banana', 'orange', 'mango', 'lemon']
# vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
# fruits.extend(vegetables)
# print(fruits )
#
# # count
# fruits = ['banana', 'orange', 'mango', 'lemon']
# print(fruits.count('orange'))
# ages = [22, 19, 24, 25, 26, 24, 25, 24]
# print(ages.count(24))
#
# # index
# fruits = ['banana', 'orange', 'mango', 'lemon']
# print(fruits.index('orange'))
# ages = [22, 19, 24, 25, 26, 24, 25, 24]
# print(ages.index(24))
#
# # Reverse
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.reverse()
# print(fruits)
# ages = [22, 19, 24, 25, 26, 24, 25, 24]
# ages.reverse()
# print(ages)
#
# # sort
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.sort()
# print(fruits)
# fruits.sort(reverse=True)
# print(fruits)
#
# ages = [22, 19, 24, 25, 26, 24, 25, 24]
# ages.sort()
# print(ages)
#
# ages.sort(reverse=True)
# print(ages)


#
# ## TUPLE
# empty_tuple = ()
# empty_tuple = tuple()
# print(empty_tuple)
#
#
# tpl = ('a', 'b', 'c')
# print(len(tpl))
#
#
#
# tpl =  ('a', 'b', 'c')
# first_item = tpl[0]
# second_item = tpl[1]
#
# fruits = ('banana', 'orange', 'mango', 'lemon')
# first_fruit = fruits[-4]
# second_fruit = fruits[-3]
# last_fruit = fruits[-1]
# print(first_fruit)
# print(second_fruit)
# print(last_fruit)

#
# fruits = ('banana', 'orange', 'mango', 'lemon')
# all_fruits = fruits[0:4]
# all_fruits= fruits[0:]
# orange_mango = fruits[1:3]
#
# print(all_fruits)
# print(orange_mango)


# # set

# st = set()
# print(st)
#
#
#
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# print(len(fruits))
#
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# print('mango' in fruits )
#
#
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# fruits.add('lime')
# print(fruits)
#
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
# fruits.update(vegetables)
# print(fruits)
#
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# fruits.pop()
# print(fruits)
#
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# fruits.clear()
# print(fruits)

#
# ##dictionary
# person = {
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
# print(len(person))
#
#
# person = {
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
# print(person['first_name'])
# print(person['country'])
# print(person['skills'])
# print(person['skills'][0])
# print(person['address']['street'])
#
#
#
# person = {
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
# person['job_title'] = 'Instructor'
# person['skills'].append('HTML')
# print(person)
#
#
#
# person = {
#     'first_name':'risa',
#     'last_name':'Yetayeh',
#     'age':18,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
#     }
#
# person['first_name'] = 'ritu'
# person['age'] = 19
# print(person)
#
# person = {
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
# person.pop('first_name')
# person.popitem()
# del person['skills']
# print(person)
#
#
# # # conditional
# a = 3
# if a < 0:
#     print('A is a negative number')
# else:
#     print('A is a positive number')
#
#
# a = 0
# if a > 0:
#     print('A is a positive number')
# elif a < 0:
#     print('A is a negative number')
# else:
#     print('A is zero')
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


"""
Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive."""
# age_str = input("Enter your age: ")
#
# age = int(age_str)
#
# if age >= 18:
#     print("You are old enough to learn to drive.")
# else:
#     years_to_wait = 18 - age
#     print(f"You need {years_to_wait} more years to learn to drive.")
#
#
# numbers = [0, 1, 2, 3, 4, 5]
# for number in numbers:
#     print(number)
#
#
#
# language = 'Python'
# for letter in language:
#     print(letter)
#
# for i in range(len(language)):
#     print(language[i])
#
#
# person = {
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
# for key in person:
#     print(key)
#
# for key, value in person.items():
#     print(key, value)
#
#
#
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# for company in it_companies:
#     print(company)
#
#
# person = {
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
# }
# for key in person:
#     if key == 'skills':
#         for skill in person['skills']:
#             print(skill)
#
#
#
# # #function
# def generate_full_name ():
#     first_name = 'Asabeneh'
#     last_name = 'Yetayeh'
#     space = ' '
#     full_name = first_name + space + last_name
#     print(full_name)
# generate_full_name ()
#
#
#
# def add_two_numbers ():
#     num_one = 2
#     num_two = 3
#     total = num_one + num_two
#     print(total)
# add_two_numbers()


def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Asabeneh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10))
print(sum_of_numbers(100))

