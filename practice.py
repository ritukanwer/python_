#
#  # Write a Python program to iterate over dictionaries using for loops.
#
def iterate(d):
    for key, values in d.items():
        print(key, values)


print(iterate(d = {'Red': 1, 'Green': 2, 'Blue': 3}))



D = {1 : 4, 2 : 3,  5 : 6 }

sum = 0
total = 0
for key, valus in D.items():
    total += valus
    sum += key
print(sum,total)

def remove_keys(dict):
   if 'a' in dict:
      del dict['a']
   return dict
print(remove_keys(dict ={1:4,'a':3,5:6}))


def marge_two(dict_1,dict_2):
    x = dict_1.copy()
    x.update(dict_2)
    return x
print(marge_two(dict_1={'a':8,'b':5} ,dict_2 = {'c':3,'d':8}))



def already_exists(dict,x):
    if x in dict:
        print("already_exists")
    else:
        print("not_exists")
print(already_exists(x = 32, dict = {3:10,4:7,5:9}))



# Create a function in Python
def name(r):
    print(r)
name("ritu")


def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60)



# Check if a list contains an element. ...
list = [1,2,3,4,5,6,7]
print(list)



def iterate(d,a):
    for key, values in d.items():
        for name,age in a.items():

            print(key, values)
            print(name,age)


print(iterate(d = {'Red': 1, 'Green': 2, 'Blue': 3},a = {"q":4}))

list_1 = [2,3,5,8,90]
list_2 = [5,6,7,8,80]
list = list_1 + list_2
print(list)
#
#
# Reverse a list in Python
list = ['ritu','naruka','rajput']
list.reverse()
print(list)

# Concatenate two lists index-wise
li = ['ri','nar','raj']
st = ['tu','uka','put']
list=[]
for i in range(len(li)):
    list.append(li[i]+st[i])
print(list)

list = [2,3,4,5]

for i in list:
        print(i*i)

list = ['ritu']
list_2 = ['naruka']
for i in list:
    for j in list_2:
        print(i + j)



list = [1,2,3,4,5]
list_2 = [3,4,5,6,7,7]
for i in list:
    for j in list_2:
        print(i)
        print(j)


# Write a Python program to add a key to a dictionary


def add_key(name,name_2):
    x = name.copy()
    x.update(name_2)
    return x
print(add_key(name= {"rohit": 18, "ritu": 17, "bitu": 21} ,name_2 = {"kuldeep":19}))



name= {"rohit": 18, "ritu": 17, "bitu": 21}
print(name)
name["kuldeep"]=19
print(name)






# LIST EXERCISE

# 1Python program to interchange first and last elements in a list
list = [2,7,9,6]

list[3] = 2
list[0] = 6
print(list)


# 2 Python program to swap two elements in a list
list = ['ritu','nidhi','ridhi','sidhi','pooja']
list[4] = 'ridhi'
list[2] = 'pooja'
print(list)


# 3Python – Swap elements in String list
list = ['ritu','kuldeep','rohit','bitu']
print(str(list))


# 4 Ways to find length of list
list = [1,2,3,4,5,'y']
print(len(list))

# 5Maximum numbers in Python
list = [10,20,30,40]
def get_maximum(list):
    max_number = 0
    for i in list:
        if i > max_number:
            max_number = i
    return max_number
print(get_maximum(list))


# 6Minimum  numbers in Python
lst = [10,40,50,70,30,50,20,4,90,20]
def get_minumum(lst):
    min_number = lst[0]
    for i in lst:
        if i < min_number:
            min_number= i
    return min_number
print(get_minumum(lst))




# 7Ways to check if element exists in list
list = [20,30,50,60]
def exit_list(list,y):
    if y in list:
        print("exit")
    else:
        print("not_exit")

print(exit_list(y=50,list = [20,30,50,60]))



# 8Different ways to clear a list in Python
def clear_list(list):
    for i in list:
        print(i)
list = ['ritu','naruka','rajput']
list.clear()
print(list)

# 9 Reversing a List
def reverse_list(list):
    for i in list[::-1]:
        print(i)
list = ['ritu','naruka','rajput']
list.reverse()
print(list)
#
#10 Cloning or Copying a list

def Cloning(list_1):
	list_copy = list_1[:]
	return list_copy



list_1 = [4, 8, 2, 10, 15, 18]
list_2 = Cloning(list_1)
print(list_1)
print(list_2)


#11  Count occurrences of an element in a list
def count_number(lst, x):
    count_number = 0
    for i in lst:
        if (i == x):
            count_number = count_number + 1
    return count_number
#
#
#
lst = [10,20,30,10,30,20,40,20,40,30,30]
x = 30
print(x,"is",count_number(lst,x),"time persent")
#

#
# 12 Python Program to find sum and average of List in Python
list = [10,20,30,40]
total = 0
for i in list:
    total += i
print(total)


list = [10,20,30,40,50,50]
def average(list):
    total = 0
    for i in list:
        total += i

    avg_val = total / len(list)
    return avg_val

c = average(list)
print(c)



# 13Sum of number digits in List

list = [1,20,30,40,30,10]
total = 0

for i in list:
    total+=i
print(total)

# 14   Multiply all numbers in the list
list = [2,3,4,5]
def multiply_list(list):
    total = 1
    for i in list:
        total = total * i
    return total
print(multiply_list(list))

#  15 Python program to find smallest number in a list
list = [9,9,8,4,1]
smallest = list[0]
for i in list:
    if i < smallest:
        smallest = i
print(smallest)


# 16 Python program to find largest number in a list
list = [50,9,9,4,5,20,90,1000]
def largest_number(list):
    largest_numbers = 0
    for i in list:
        if i > largest_numbers:
            largest_numbers = i
    return largest_numbers
print(largest_number(list))





# 17 Python program to find second largest number in a list
list = [90,80,30,40,50,800]
def second_largest_number(list):
    second_larest = 0
    largest = min(list)
    for i in range(len(list)):
        if list[i] > largest:
            second_largest = largest
            largest = list[i]
        else:
            second_largest = max(second_largest,list[i])
    return second_largest
print(second_largest_number(list))



# 18  Python program to print even numbers in a list
list = [10,20,5,9,90,7,58]
def even_number(list):
    even = []
    for i in list:
        if i % 2 == 0:
            even.append(i)
    return even
print(even_number(list))

# 19 Python program to print odd numbers in a List
list = [10,20,5,9,90,7,58]
def odd_numbers(list):
    odd = []
    for i in list:
        if i % 2 != 0:
            odd.append(i)
    return odd
print(odd_numbers(list))
# 20  Python program to print all even numbers in a range
def even_num(list):
    even = []
    for i in range(0,100):
        if i % 2 == 0:
            even.append(i)
    return even
print(even_num(100))

#21 Python program to print all odd numbers in a range
def odd_num(list):
    odd = []
    for i in range(0,100):
        if i % 2 != 0:
            odd.append(i)
    return odd
print(odd_num(100))


# 22  Python program to count Even and Odd numbers in a List
def count_odd_numbers(n):
    odd = []
    for i in range(n + 1):
        if i % 2 != 0:
            odd.append(i)
    return odd


print(len(count_odd_numbers(100)))


def count_even_number(n):
    even = []
    for i in range(n+1):
        if i % 2 == 0:
            even.append(i)
    return even
print(len(count_even_number(100)))



# 23  Python program to print positive numbers in a list
list = [-4,-5,-3,9,3,8]


for i in list:

    if i < 0:
        print(i,end = " ")

#
# 24Python program to print negative numbers in a list
list1 = [-3,-4,-5,6,9,8]
for i in list1:

    if i < 0:
        print(i,   end = " ")

#  25 Python program to print all positive numbers in a range

def positive_number(list):
    positive = 0
    for i in range(-3,3):
        if i >= 0:
            positive += 1

    return positive
print(positive_number(3))
#   26  Python program to print all negative numbers in a range

def negetive_number(list):
    negetive = 0
    for i in range(-9,2):
        if i <= 0:
            negetive += 1


    return negetive
print(negetive_number(2))



# 27 Python program to count positive and negative numbers in a list
list = [1,2,4,5,6,-4,-5,-6,7,-7]
def count_negetive_number(list):
    negetive = 0
    for i in list:
        if i <= 0:
            negetive += 1
    return negetive
print(count_negetive_number(list))


list = [1,2,4,5,6,-4,-5,-6,7,-7]
def count_positive_number(list):
    positive = 0
    for i in list:
        if i >= 0:
            positive += 1
    return positive
print(count_positive_number(list))





# 28 Remove multiple elements from a list in Python
list1 = [11, 5, 17, 18, 23, 50,37 ,90, 77]


for ele in list1:
    if ele % 2 == 0:
        list1.remove(ele)

print(list1)

# 29 Remove empty tuples from a list
tuples = [(),('ritu'),(),('naruka')]
def Remove(tuples):
    for i in tuples:
        if (len(i) == 0):
            tuples.remove(i)
    return tuples



print(Remove(tuples))


# 30 Program to print duplicates from a list of integers

list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 7, 8, 9, 9]
x = []
y = []
for i in list:
    if i not in x:
        x.append(i)
for i in x:
    if list.count(i) > 1:
        y.append(i)
print(y)

#
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# print(d)
# sorted_d = sorted(d.items())
# print(sorted_d)
# sorted_d = dict( sorted(d.items(),reverse=True))
# print(sorted_d)


# dictionary =  {0: 10, 1: 20}
# dictionary_2 = {2:30}
# def add_key_dictionary(dictionary,dictctionary_2):
#     for key,values in dictionary.items():
#         for a,b in dictionary_2.items():
#             print(key,value)
#             print(a,b)
# print(add_key_dictionary(dictionary = {0:10,1:20},dictionary_2 = {2:30}))
# print(iterate(d = {'Red': 1, 'Green': 2, 'Blue': 3},a = {"q":4}))

