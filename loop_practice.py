# count = 0
# while count < 5:
#     print(count)
#     count = count + 1

# count = 0
# while count < 5:
#     print(count)
#     count = count + 1
# else:
#     print(count)
#
#
# count = 0
# while count < 5:
#     print(count)
#     count = count + 1
#     if count == 3:
#         break


#
# count = 0
# while count < 5:
#     if count == 4:
#         continue
#     print(count)
#     count = count + 1


# numbers = [0, 1, 2, 3, 4, 5]
# for number in numbers:
#     print(number)

#
#
# language = 'Python'
# for letter in language:
#     print(letter)
#
#
# for i in range(len(language)):
#     print(language[i])


# numbers = [0, 1, 2, 3, 4, 5]
# for number in numbers:
#     print(number)


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
#
#
# for key, value in person.items():
#      print(key, value)


# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# for company in it_companies:
#     print(company)

# numbers = (0,1,2,3,4,5)
# for number in numbers:
#     print(number)
#     if number == 3:
#         break

# numbers = (0,1,2,3,4,5)
# for number in numbers:
#     print(number)
#     if number == 3:
#         continue
#     print('Next number should be ', number + 1)\
#         if number != 5 else print("loop's end")
# print('outside the loop')

# lst = list(range(11))
# print(lst)

# st = set(range(1, 11))
# print(st)
#
# lst = list(range(0,11,2))
# print(lst)
# st = set(range(0,11,2))
# print(st)

# for number in range(11):
#     print(number)

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
# for number in range(11):
#     print(number)
# else:
#     print('The loop stops at', number)
#
#
#
#
#
#
#
#
#
#quesions()
#
#
#
# 1
for i in range(0,10):
    print(i)
    k = 0
    while k <= 10:

        k += 1
# #2
for i in range(10,-1,-1):
    print(i)
    k = 10
    while k >= 10:

        k -= 1
#3
def seven_calls(hash):
    hash = '#'
    for i in range(1,9):
        print(hash * i)
a = seven_calls(hash)
#4
def functions(hash):
    hash = "#"
    for i in range(1,9):
        for j in range(1,9):
            print("#", end = '')
        print()

x = functions(hash)




#5
first = [0,1,2,3,4,5,6,7,8,9,10]
for i in first:

        print(i, " x", i, "=", i * i)

#6
for i in  ['Python', 'Numpy','Pandas','Django', 'Flask']:
    print(i)

#
#7
def find_even_numbers(lst):
    evens = []
    for i in range(0,100):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(list))

# 8
def find_odd_numbers(lst):
    odd = []
    for i in range(0,100):
        if i % 2 != 0:
            odd.append(i)
    return odd
print(find_odd_numbers(list))



#level 2
# 1
def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)

print(sum_of_numbers(100))



#2
def sum_of_even(lst):
    even = 0
    for i in range(0,101):
        if i % 2 == 0:
            even += i
    return even
print(sum_of_even(list))

def sum_of_odd(lst):
    odd = 0
    for i in range(0,101):
        if i % 2 != 0:
            odd += i
    return odd
print(sum_of_odd(list))




# # level 3
list = ['banana', 'orange', 'mango', 'lemon']
def reverse_list(list):

        return list[::-1]

print(reverse_list(list))