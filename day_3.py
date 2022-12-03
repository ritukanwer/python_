# # functions
# 1# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers ():
    number_one = 50
    number_two = 80
    total = number_one + number_two
    print(total)
add_two_numbers()
#
# 2#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(16))

#
#
# 3#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback.
#
def add_all_nums(*nums):
    total = 0
    for i in nums:
        total += i
    return total
# print(add_all_nums(2, 3, 5))
print(area_of_circle(10))



# 4Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) +32
print(celsius_to_fahrenheit(2))



# 5Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def  check_season(month):
    if month in ['september','october','november']:
        print('autumn')
    if month in ['december','january','fabruary']:
        print('winter')
    if month in ['march','april','may']:
        print('spring')
    if month in ['june', 'july', 'august']:
        print('summer')

    # else:
    #     print('summer')
print(check_season('november'))

#6Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, x2, y1, y2):
    m = (y2 - y1) / (x2 - x1)
    return m
print(calculate_slope(10,20,50,70))



#8
# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

n = [3,5,7]

def print_list(x):
    for i in range(0,len(x)):
        print (x[i])
print_list(n)



# 9
# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]
def reverse_of_list(reverse_list):
    for i in reverse_list[::-1]:
        print(i)
reverse_list = [1,2,3,4,5,6]
reverse_list.reverse()
print(reverse_list)



def reverse_of_list(reverse_list):
    for i in reverse_list[::-1]:
        print(i)
reverse_list = ["A","B","C"]
reverse_list.reverse()
print(reverse_list)





#10  Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

list = ['ritu','naruka']
def capiatl_list_items(list):
    for i in list:
        list[list.index(i)] = i.capitalize()
    return list
print(capiatl_list_items(list))



# 11Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(add_item(food_staff, 'Meat'))
# numbers = [2, 3, 7, 9];
# print(add_item(numbers, 5))
def add_items(food_staff):

    for i in food_staff:
        return i
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
food_staff.append('meat')
print(food_staff)


def add_items(numbers):
    for i in numbers:
        return i

numbers = [2,3,7,9]
numbers.append(5)
print(numbers)



# 12
# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9];
# print(remove_item(numbers, 3))  # [2, 7, 9]
#
#
def removed_items(food_staff):
    for i in food_staff:
        return i
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
food_staff.remove('Mango')
print(food_staff)


def removed_items(numbers):
    for i in food_staff:
        return i
numbers = [2,3,7,9]
numbers.remove(3)
print(numbers)



# 13
# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_all_numbers(10)) # 55
# print(sum_all_numbers(100)) # 5050
#

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))


# 15Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def add_of_evens(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(add_of_evens(10))
add_even_number = [0+2+4+6+8+10]
print(add_even_number)



# #14Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def add_of_odd(n):
    odd = []
    for i in range(n + 1):
        if i % 2 != 0:
            odd.append(i)
    return odd
print(add_of_odd(10))
add_odd_numbers = [1+3+5+7+9]
print(add_odd_numbers)
#level 2Declare a function named evens_and_odds . It takes a positive integer
# as parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.



# 1Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.
def add_of_odd(n):
    odd = []
    for i in range(n + 1):
        if i % 2 != 0:
            odd.append(i)
    return odd

all_odd_numbers = add_of_odd(100)
print(len(all_odd_numbers))



def add_of_evens(n):
    evens = []
    for i in range(n + 1):
        if i%2 == 0:
            evens.append(i)
    return evens
all_evens_numbers = add_of_evens(100)
print(len(all_evens_numbers))

#2
# #Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def fectorial(a):
    b = 1
    for i in range(a + 1):
        b *= 1
    return a
print(fectorial(1))
#3Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(check):
    if check:
        return True
    else:
        return False
print(is_empty(90))



#4Write different functions which take lists.
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



for i in range(10):
    print(i)



list =  [10,20]
def variance(list):                                                #[10,20 close 15
    n = len(list)                                                  #(10-15)**2+(20-15)**2/2
    mean = sum(list)/n                                          #   25+25/2 = 25]
    deviations = [(x - mean)**2for x in list]
    variance = sum(deviations)/n
    return variance
print(variance(list))



list = [10,20]

def standard_deviation(list):

    n = len(list)
    mean = sum(list) / n
    deviations = [(x - mean) ** 2 for x in list]
    variance = sum(deviations) / n
    standard_deviation = variance ** 0.5
    return standard_deviation
print(standard_deviation(list))





# level 3
# 1 Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    for i in range(2,n):
        if (n%i) == 0:
            return True
        return False
#
print(is_prime(4))



# 2
# Write a functions which checks if all items are unique in the list.
list = ['apple','banana','orange']
def function(list):

    if (len(set(list)) == len(list)):
        print("all elements are unique")
    else:
        print("all elements  are not unique")
print(list)


# 3Write a function which checks if all the items of the list are of the same data type.
list = [1,2,3,4,5,6]
def check_list(list):
    return len(set(list)) == 1
list = [1, 1]
if check_list(list) == True:
    print('same')
else:
    print('not same')






