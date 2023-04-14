




 # # Write a program that takes a list of numbers and prints the sum of the positive numbers.
# [-2, 5, -10, 8, 3]
def add_positive_numbers(input: list) -> int:
    sum = 0
    for i in input:
        if i > 0:
            sum += i
    return sum
print(add_positive_numbers(input = 1))
def pick(l: list, index: int)  ->int:
    return l[index]
[3, 8, 2, 7, 4, 9]


# max of 2
def maximum(a, b):

    if a >= b:
        return a
    else:
        return b

a = 2
b = 4
print(maximum(a, b))


# Python program to find the
# minimum of two numbers


def minimum(a, b):
    if a <= b:
        return a
    else:
        return b

a = 2
b = 4
print(minimum(a, b))

# python code to Check if element exists in list or not

lst = [1, 6, 3, 5, 3, 4]

i = 4

if i in lst:
    print("exist")
else:
    print("not exist")


# Python program to find the sum
# and average of the list

List = [4, 5, 1, 2, 9, 7, 10, 8]

count = 0


for i in lst:
	count += i


avg = count/len(List)

print("sum = ", count)
print("average = ", avg)



# Python program to multiply all values in the
# list using traversal


def multiplyList(myList):


	result = 1
	for x in myList:
		result = result * x
	return result


list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))



# Given the code below, use the correct method on line 3 in order to find out the number of elements in my_list
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
print(len(my_list))


# Given the code below, use the correct code on line 3 in order to remove the element of my_list located at index 5.

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
my_list.pop(5)
print(my_list)


# Given the code below, use the correct method on line 3 in order to add the element 'C++' at the end of my_list.

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
my_list.append("C++")
print(my_list)



# Given the code below, use the correct method on line 3 in order to remove the element 30 from my_list.
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
my_list.remove(30)
print(my_list)



# Given the code below, use the correct method on line 3 in order to return the index of the element 10.5 in my_list.
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
index = my_list[1]
print(index)



# Given the code below, use the correct method on line 3 in order to insert the element 77 at index 4 in my_list.
my_list = [10,10.5,20,30,'Python','Java','Ruby']
my_list.insert(4,77)
print(my_list)



# Given the code below, use the correct method on line 3 in order to concatenate my_list with [100, 101, 102], by adding the
# latter at the end of my_list.

my_list =[10,10.5,20,30,'Python','Java''Ruby']
my_list.extend([100,101,102])
print(my_list)


# Given the code below, use the correct method on line 3 in order to find out how many times does the element 20 occur in my_list.

my_list =[10,10.5,20,30,'Python','Java''Ruby']

x = my_list.count(20)

print(x)


# Given the code below, use the correct function on line 3 in order to sort the elements of my_list in ascending order.
my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]
x = sorted(my_list)
print(x)






# Given the code below, use the correct function on line 3 in order to find out the smallest number in my_list.
my_list =  [10, 10.5, 11.01, 19.25, 20, 25.6, 29.99, 30]
def min_number(my_list):
    min = 0
    for i in my_list:
        if min <= 0:
            min = i
    return min
print(min_number(my_list))


# Given the code below, use the correct function on line 3 in order to find out the largest number in my_list.
my_list =  [10, 10.5, 11.01, 19.25, 20, 25.6, 29.99, 30]
def max_number(my_list):
    max = 0
    for i in my_list:
        if max >= 0:
            max = i
    return max
print(max_number(my_list))


# Given the code below, use the correct function on line 3 in order to get the sum of all the elements of my_list.
my_list =  [10, 10.5, 11.01, 19.25, 20, 25.6, 29.99, 30]
def sum_all_list(my_list):
    sum = 0
    for i in my_list:
       sum += i
    return sum
print(sum_all_list(my_list))



# Given the code below, use the correct method on line 3 in order to delete all the elements from my_list and obtain an empty list.
my_list =  [10, 10.5, 11.01, 19.25, 20, 25.6, 29.99, 30]
my_list.clear()
print(my_list)





# Given the code below, use the correct operators and parentheses on line 3 in order to add the
# elements of [30.01, 30.02, 30.03] to my_list and multiply the resulting list by 2.

my_list = [10,10.5,11.01,19.25,20,25.6,29.99,30]
add = (my_list + [30.01,30.02,30.03])*2
print(add)


# Given the code below, use the correct code on line 3 in order to return the element 20 from my_list based on its index.
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

element = my_list[2]

print(element)



# Given the code below, use the correct code on line 3 in order to return the element Java from my_list based on its index (negative).
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
element = my_list[-2]
print(element)




# Given the code below, use the correct code on line 3 in order to return a slice made of [30, 'Python', 'Java'] from my_list based on positive indexes.


my_list = [10,10.5, 20, 30, 'Python','Java','Ruby']
element = my_list[3:6]
print(element)




# question_54
# Given the code below, use the correct code on line 3 in order to return a slice made of [30, 'Python', 'Java'] from my_list based on negative indexes.
my_list = [10,10.5, 20, 30, 'Python','Java','Ruby']
element = my_list[-4:-1]
print(element)




# Given the code below, use the correct code on line 3 in order to return my_list except the first 3 elements, using a single, positive index.
my_list = [10,10.5,20,30, 'Python','Java','Ruby']
element = my_list[:3]
print(element)



# Given the code below, use the correct code on line 3 in order to return my_list except the last 4 elements, using a single, negative index.
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
element = my_list[-4:]
print(element)


# question_57
# Given the code below, use the correct code on line 3 in order to return my_list except the first 3 elements, using a single, negative index.
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
element = my_list[:-4]
print(element)



# Given the
# code below, use the correct code on line 3 in order to return my_list except the last 2 elements, using a single, positive index.

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
element = my_list[5:]
print(element)



# Given the code below, use the correct code on line 3 in order to return every third element of my_list starting with the first element of the list.
my_list = [10, 10.5, 20, 30,'Python', 'Java', 'Ruby']
slice = my_list[::3]
print(slice)





# Given the code below, use the correct code on line 3 in order to return every fourth element of my_list starting with the last element of the list.
my_list = [10, 10.5, 20, 30, 'Python', 'Java', ' Ruby']
slice = my_list[::-4]
print(slice)


