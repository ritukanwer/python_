# 1Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print(i)


counter = 0
while counter <= 10:
    print(counter)
    counter += 1


#
# # 2Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10,-1,-1):
    print(i)

counter = 10
while counter >= 0:
    print(counter)
    counter -= 1


# 3Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#
#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######

for i in range(1, 8):
    print("#" * i)


# 4 Use nested loops to create the following:
#
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
for i in range(8):
    for j in range(8):
        print("#",end = " ")
    print()


#
#5 Print the following pattern:
#
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100


for i in range(1,11):
    print(f"{i} x {i} = ",i* i)


#6 Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
list = ["python","numpy","pandas","django","flask"]
for i in list:
    print(i)

# 7Use for loop to iterate from 0 to 100 and print only even numbers
def sum_of_even():
    even = []
    for i in range(0,101):
        if i % 2 == 0:
            even.append(i)

    return even
print("even_numbers:-", sum_of_even())


def find_sum_of_odd():
    odd = []
    for i in range(0,101):
        if i % 2 != 0:
            odd.append(i)
    return odd
print("odd_numbers:-",find_sum_of_odd())
#
# Exercises: Level 2
# 1Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.

def find_sum_of_range():
    sum = 0
    for i in range(0,101):
        sum+=i
    return sum
print(find_sum_of_range())


# 2 Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
#
# The sum of all evens is 2550. And the sum of all odds is 2500.
def sum_even_numbers():
    sum_of_evens = 0
    for i in range(0,101):
        if i % 2 == 0:
            sum_of_evens+=i
    return sum_of_evens
print("sum_of_even_numbers:-",sum_even_numbers())


def sum_of_odd_numbers():
    sum_of_odd = 0
    for i in range(0,101):
        if i % 2 != 0:
            sum_of_odd = sum_of_odd + i
    return sum_of_odd
print("sum_of_odd_numbers:-", sum_of_odd_numbers())


# 3 This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit_list = ['banana', 'orange', 'mango', 'lemon']
def reverse_list(fruit_list):
    reverse_list = []
    for i in reversed(fruit_list):
        reverse_list.append(i)
    return reverse_list
print(reverse_list(fruit_list))
