#creat a function
# def great():
#    print("hello")
#    print("good morning")
# great()
#
#
#
# def add(x,y):
#    c = x+y
#    return c
# x = int(input("enter your first number: "))
# y = int(input("enter your second number: "))
# z  = (x+y)
# print(z)
#
#
#
# #calling function
# def add_two_numbers ():
#    num_one = 2
#    num_two = 3
#    total = num_one + num_two
#    print(total)
# add_two_numbers()
#
# #function return a value part 1
# def add_two_numbers ():
#    num_one = 2
#    num_two = 3
#    total = num_one + num_two
#    return total
# print(add_two_numbers())
#
#
# #function with perameters
# def add_ten(num):
#    ten = 10
#    return num + ten
# print(add_ten(5000))
#
#
# def square_number(y):
#    return y * y
# print(square_number(50))
#
# def area_of_circle(r):
#    PI= 3.14
#    area = PI * r**2
#    return area
# print(area_of_circle(10))
#
#
# def sum_of_numbers(n):
#    total = 0
#    for i in range(n+1):
#        total+=i
#    print(total)
# print(sum_of_numbers(10))
# print(sum_of_numbers(100))
#
#
# list
# list = ['ritu','naruka']
# for i in list:
#     print(i)
#
#for loop

# language = 'python'
# for i in language:
#     print(i)
# num = (1,2,4,6,9,8)
# for i in num:
#     print(i)

# numbers = (0,1,2,3,4,5)
# for number in numbers:
#     print(numbers)
#     if number == 2:
#         break


# num = (0,1,2,3,4,5)
# for i in num:
#     print(i)
#     if i == 3:
#         continue
#     print(i + 1)
#


#dictionary
# person = {'first_name':'ritu',
#           'last_name':'naruak',
#           'age': 17,
#           'country':'india'}
# for key in person:
#     print(key)
# for key, value in person.items():
#     print(key,value)

# companies = {'facebook','google','microsoft','apple'}
# for i in companies:
#     print(i)

# lst = list(range(1,11))
# print(lst)

# for number in range(11):
#     print(number)

person = {'first_name':'ritu',
          'last_name':'naruka',
          'age':17,
          'country':'india',
          'is_marred': False,
          'skills':['javascript','react','node','python']}
for key in person:
    if key == 'skills':
        for skills in person['skills']:
            print(skills)