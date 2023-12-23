# 1Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def sum_of_two_numbers(a,b):
    sum = a+ b
    return sum
print(sum_of_two_numbers(1,2))


# 2Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(radius):
    pi = 3.14
    area = pi * radius**2
    return area

radius = 5
result = area_of_circle(radius)
print(result)


# 3
# Write a function called add_all_nums which takes arbitrary number of
# arguments and sums all the arguments. Check if all the list items are
# number types. If not do give a reasonable feedback.

#
def add_all_nums(*nums):
    total = 0
    for i in nums:
        total += i
    return total
print(add_all_nums(2, 3, 5))

#
# # 4Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
# # Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) +32
print(celsius_to_fahrenheit(2))
#
#
#
# # 5 Write a function called check-season, it takes a month parameter and returns
# the season: Autumn, Winter, Spring or Summer.
# def check_season(month):
#     if month in {'december', 'january', 'february'}:
#         return 'Winter'
#     elif month in {'march', 'april', 'may'}:
#         return 'Spring'
#     elif month in {'june', 'july', 'august'}:
#         return 'Summer'
#     elif month in {'september', 'october', 'november'}:
#         return 'Autumn'
#     else:
#         return 'Invalid month'
#
#
# user_input = input("Enter a month: ")
# season = check_season(user_input)
# print(season)
#

#
#6Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, x2, y1, y2):
    m = (y2 - y1) / (x2 - x1)
    return m
print(calculate_slope(10,20,50,70))



# 8 Declare a function named print_list. It takes a list as a parameter
# and it prints out each element of the list.
list = [1,2,3,4]
def print_list(list):
    return list
print(print_list(list))

# 9

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# print(reverse_list([1, 2, 3, 4, 5]))
# print(reverse_list1(["A", "B", "C"]))

def reverse_list(arr):
    arr.reverse()
    return arr
arr1 = [1, 2, 3, 4, 5]
arr2 = ["A", "B", "C"]
result1 = reverse_list(arr1)
result2 = reverse_list(arr2)
print(result1)
print(result2)


# 10 Declare a function named capitalize_list_items.
# It takes a list as a parameter and it returns a capitalized list of items
list = ['apple','boy','cow','dog','eye']

def capitalized_list_of_items(input_list):
    capitalized_items = []
    for item in input_list:
        a = item.capitalize()
        capitalized_items.append(a)
    return capitalized_items

result = capitalized_list_of_items(list)
print(result)


# 11Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# numbers = [2, 3, 7, 9];
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
def add_item(food_staff, new_item):
    updated = food_staff.copy()
    updated.append(new_item)
    return updated
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
result = add_item(food_staff, 'Meat')
print(result)

numbers = [2,3,7,9]
def add_item(numbers,new_item):
    update = numbers.copy()
    update.append(new_item)
    return update
print(add_item(numbers,15))


# 12 Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9];
# print(remove_item(numbers, 3))
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
def remove_item(food_staff, item):
    updated = food_staff.copy()
    if item in updated:
        updated.remove(item)
    return updated
result = remove_item(food_staff, 'Mango')
print(result)

numbers = [2, 3, 7, 9]
def remove_item(numbers,item):
    update = numbers.copy()
    if item in update:
        update.remove(item)
    return update
print(remove_item(numbers,7))


# 13Declare a function named sum_of_numbers. It takes a number parameter and it adds
# all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_all_numbers(10)) # 55
# print(sum_all_numbers(100)) # 5050
def sum_all_numbers(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i
    return sum
print(sum_all_numbers(number = 5))
print(sum_all_numbers(number = 10))
print(sum_all_numbers(number = 100))



# 14 Declare a function named sum_of_odds. It takes a number parameter and
# it adds all the odd numbers in that range.
def sum_of_odds(number):
    sum = 0
    for i in range(101):
        if i % 2 != 0:
            sum += i
    return sum
print(sum_of_odds(number = 101))


# 15 Declare a function named sum_of_even. It takes a number parameter and it adds
# all the even numbers in that - range.

def sum_of_even(number):
    sum = 0
    for i in range(101):
        if i % 2 == 0:
            sum += i
    return sum
print(sum_of_even(number = 101))


"""LEVEL_2"""
# Declare a function named evens_and_odds . It takes a positive integer as
# parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.

def add_of_odd(number):
    odd = []
    for i in range(number+ 1):
        if i % 2 != 0:
            odd.append(i)
    return odd

all_odd_numbers = add_of_odd(100)
print(len(all_odd_numbers))



def add_of_evens(number):
    evens = []
    for i in range(number + 1):
        if i%2 == 0:
            evens.append(i)
    return evens
all_evens_numbers = add_of_evens(100)
print(len(all_evens_numbers))



# 2 Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number



#3Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(check):
    if check:
        return True
    else:
        return False
print(is_empty(90))
#
#
# #4Write different functions which take lists.
# They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
list = [10,20,30, 50, 40, 50]
def calculate_mean(list):

    return sum(list)/len(list)
c = calculate_mean(list)
print(c)
#
#
list = [10, 20, 30, 50 ,40 ,50]
def calculate_midean(list):
    data = sorted(list)
    index = len(data)//2
    if len(list)%2 != 0:
        return data[index]
    return (data[index - 1] + data[index])/ 2
a = calculate_midean(list)
print(a)

list = [10,20,30,50,40,50]
def calculate_mode(list):
    mode = max(list,key = list.count)
    return mode
print(calculate_mode(list))

#
#
for i in range(10):
    print(i)
#
#
#
list =  [10,20]
def variance(list):                                                #[10,20 close 15
    n = len(list)                                                  #(10-15)**2+(20-15)**2/2
    mean = sum(list)/n                                          #   25+25/2 = 25]
    deviations = [(x - mean)**2for x in list]
    variance = sum(deviations)/n
    return variance
print(variance(list))
#
#

list = [10,20]

def standard_deviation(list):

    n = len(list)
    mean = sum(list) / n
    deviations = [(x - mean) ** 2 for x in list]
    variance = sum(deviations) / n
    standard_deviation = variance ** 0.5
    return standard_deviation
print(standard_deviation(list))
# #
#
#
#
#
# # level 3
# # 1 Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    for i in range(2,n):
        if (n%i) == 0:
            return True
        else:
            return False

print(is_prime(4))



# 2
# Write a functions which checks if all items are unique in the list.
list = ['apple','banana','orange']
def function(list):

    if (len(set(list)) == len(list)):
        print("all elements are unique")
    else:
        print("all elements  are not unique")
print(function(list))



# 3# Write a function which checks if all the items of the list are of the same data type.
def check_all_items_same(input_list):
    first_item_type = type(input_list[0])
    for item in input_list:
        if type(item) == first_item_type:
            return True
        else:
            return False

my_list = [1, 2, 3, 'A']
print(check_all_items_same(my_list))
