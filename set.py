
# question_61
# Given the code below, use the correct function on line 3 in order to convert my_list to a set.

my_list = [1, 2, 3, 4, 4, 5, 2, 9, 8, 8, 4, 3]

my_set = set(my_list)
print(my_set)
print(type(my_set))



# question_62
# Given the code below, use the correct function on line 3 in order to convert my_list to a frozen set.
my_list = [1, 2, 3, 4, 4, 5, 2, 9, 8, 8, 4, 3]

my_set = frozenset(my_list)
print(type(my_set))


my_set = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}

check = 10 in my_set

print(check)