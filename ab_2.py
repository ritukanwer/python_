####1. Write a Python program to sum all the items in a list.
list  = [1,2,3,4,5,6,7,8,9]

def sum_all_items(list):
    sum = 0
    for i in list:
        sum += i
    return sum
print(sum_all_items(list))


# 2. Write a Python program to multiply all the items in a list.
list = [2,3,4]
def multiple_items(list):
    mult = 1
    for i in list:
        mult *= i
    return mult
print(multiple_items(list))


# 3. Write a Python program to get the largest number from a list.
list = [20,40,90,80,20,99,28]
def largest_num(list):
    max = 0
    for i in list:
        if i > max:
            max = i
    return max
print(largest_num(list))


# 4. Write a Python program to get the smallest number from a list.
list = [20,40,90,80,-5,20,99,28]
def smallest_no(list):
    min = None
    for i in list:
        if min is None or i < min:
            min = i
    return min
print(smallest_no(list))


# 5. Write a Python program to count the number of strings from a given list of strings.
# The string length is 2 or more and the first and last characters are the same.
list = ['abc', 'xyz', 'aba', '1221','yuy']

def list_f_l_c_same(list):
    count = 0
    for i in list:
        if len(i) > 1 and i[0] == i[-1]:
            count+=1
    return count
print(list_f_l_c_same(list))



# 7. Write a Python program to remove duplicates from a list.
list  = [2,3,4,2,305,5,4,32,43,2,3,4,5,6,42,2,4,42,305]

def remove_duplicate(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list
print(remove_duplicate(list))


# 8. Write a Python program to check if a list is empty or not.
def is_list_empty(input_list):
    if not input_list:
        return True
    else:
        return False

my_list = []
result = is_list_empty(my_list)
print(result)


#9. Write a Python program to find the list of words that are longer than n from a given list of words.
list = ['ritu','ravina','karishna',"saru",'tannu','gnu']
n = 4
def list_are_longer_than_n(list,n):
    new_list = []
    for i in list:
        if len(i) > n:
            new_list.append(i)
    return new_list
print(list_are_longer_than_n(list,n))


# 10 Write a Python function that takes two lists and returns True if they have at least one common member.
lst1 = [1,2,3,4,5]
lst2 = [5,6,7,8,9]
def commen_no_in_two_list(lst1,lst2):
    for i in lst1:
        if i in lst2:
            return True
    else:
        return False
print(commen_no_in_two_list(lst1,lst2))



# 11. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

my_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
def remove_elements(my_list):
    result_list = []
    for i in range(len(my_list)):
        if i not in [0,4,5]:
            result_list.append(my_list[i])
    return result_list

print(remove_elements(my_list))

# 12 Write a Python program to generate a 3*4*6 3D array whose each element is *.
three_d_array = [[[ '*' for _ in range(6)] for _ in range(4)] for _ in range(3)]

# 3D एरे को प्रिंट करें
for i in range(3):
    for j in range(4):
        for k in range(6):
            print(three_d_array[i][j][k], end=' ')
        print()
    print()

"""
#Write a Python program to count the number of unique sublists within a given list.
Original list:
[[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
Number of unique lists of the said list:
{(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
Original list:
[['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
Number of unique lists of the said list:
{('green', 'orange'): 2, ('black',): 1, ('white',): 1} """

list = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
