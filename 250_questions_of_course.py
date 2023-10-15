
"""
question_1
Given the code below, insert the correct negative index on line 3 in order to get
the last character in the string."""

my_string ="In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string[-1])



"""
question_2
Given the code below, insert the correct positive index on line 3 in order to return
the comma character from the string."""
my_string ="In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string[7])



"""
question_3
Given the code below, insert the correct negative index on line 3 in order 
to return the w character from the string.
"""
my_string ="In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string[-10])


"""
question_4
Given the code below, insert the correct method on line 3 in order to return 
the index of the B character in the string.
"""

my_string ="In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string.index("B"))


"""
question_5
Given the code below, insert the correct method on line 3 in order to return the
 number of occurrences of the letter o in the string.
"""
my_string ="In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string.count("o"))


"""
question_6
Given the code below, insert the correct method on line 3 in order to 
convert all letters in the string to uppercase."""
my_string ="In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string.upper())


"""
question_7
Given the code below, insert the correct method on line 3 in order to get
 the index at which the substring Bitcoin starts.
"""
my_string ="In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string.find("Bitcoin"))


"""
question_8
Given the code below, insert the correct method on line 3 in order 
to check of the string starts with the letter X."""

my_string ="In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string.startswith("X"))


"""
question_9
Given the code below, insert the correct method on line 3 in order
 to convert all uppercase letters to lowercase and all lowercase letters to uppercase."""

my_string ="In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string.swapcase())


"""
question_10
Given the code below, insert the correct method on line 3 in order to remove all spaces 
(single Space characters from the keyboard) from the string."""
my_string ="In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string.replace(" ",""))



"""
question_11
Given the code below, insert the correct method on line 3 in order to replace all
 the occurrences of letter i with the substring btc."""
my_string ="In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string.replace("i","btc"))

"""
question_12
Given the code below, insert the correct method on line 3 in order to split
 the entire string in two parts, using the comma as a delimiter.Given the code 
 below, insert the correct method on line 3 in order to split the entire string 
 in two parts, using the comma as a delimiter."""

my_string ="In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string.split(","))


"""
question_13
Given the code below, insert the correct method on line 3 in order to 
join the characters of the string using the & symbol as a delimiter."""
my_string ="In 2010, someone paid 10k Bitcoin for two pizzas."

print("&".join(my_string))




"""
question_14
Given the code below, insert the correct code on line 4 in order to 
concatenate my_string with the following string:

my_other_string = "Poor guy!"""
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
my_other_string = "Poor guy!"

print(my_string + my_other_string)

"""
question_15
Given the code below, insert the correct method on line 3 in order to 
convert the first letter of each word in the string to uppercase."""
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string.title())



"""
question_16
Given the code below, use string formatting with the % operator on line 3 
to map the values of 2010, 10k and Bitcoin to the corresponding formatting operators."""

my_string = "In %s, someone paid %s %s for two pizzas."

print(my_string % ("2010", "10k", "Bitcoin"))


"""
question_17
Given the code below, use string formatting with the format()
 method on line 3 to map the values of 2010, 10k and Bitcoin to the 
 corresponding formatting operators
"""

my_string = "In {}, someone paid {} {} for two pizzas."

print(my_string.format("2010","10k","Bitcoin"))



"""
question_18
Given the code below, use slicing and insert the correct code on line 3
 in order to return the substring 2010 from the string. Use positive indexes!

"""

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[3:7])



"""
question_19
Given the code below, use slicing and insert the correct code on line 3 in 
order to return the substring Bitcoin from the string. Use negative indexes!

"""

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[-23:-16])


"""
question_20
Given the code below, use slicing and insert the correct code on line 3 in 
order to return the first 12 characters in the string. Use a single, positive index!"""

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[:12])


"""
question_21
Given the code below, use slicing and insert the correct code on line 3 in order to return the last 9 
characters of the string. Use a single, negative index!"""
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[-9:])



"""
question_22
Given the code below, use slicing and insert the correct code on line 3 in order to return the entire 
string in reversed order"""

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[::-1])


"""
question_23
Given the code below, use slicing and insert the correct code on line 3 in
 order to return every 7th character of the string, starting with the first character.

The final result should be I,n top"""

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[::7])


"""
question_24    
Given the code below, use slicing and insert the correct code on line 3
 in order to return the string except the first 10 characters. Use a single, positive index!

"""
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[10:])


"""
question_25
Given the code below, use slicing and insert the correct code on line 3 in order to return the 
string except the last 4 characters. Use a single, negative index!"""
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[:-4])

"""
question_26
Given the code below, use the correct function on line 3 in order to convert num1 from integer to float.

"""

num1 = 25

num2 = float(num1)

print(type(num2))


"""
question_27
Given the code below, use the correct function on line 3 in order to convert num1 from float to integer."""

num1 = 13.67

num2 = int(num1)

print(type(num2))


"""
question_28
Given the code below, use the correct math operator
 in between num1 and num2 on line 4 in order to obtain the result shown."""

num1 = 25
num2 = 8

num3 = num1 %num2

print(num3 == 1)

"""
question_29

Given the code below, use the correct math operator in between num1 and num2
on line 4 in order to obtain the result shown.

"""

num1 = 10
num2 = 3

num3 = num1 ** num2

print(num3 == 250 * 4)


"""
question_30
Given the code below, use the correct math operator in between num1 and num2 on 
line 4 in order to obtain the result shown"""
num1 = 5
num2 = 2

num3 = num1 //num2

print(num3 == 5 % 3)

"""
question_31
Given the code below, use the correct function on line 3 in order to obtain the distance between num1 and 0."""
num1 = -11
num2 = abs(num1)

print(num2 == 11)


"""
question_32
Given the code below, use the correct function on line 4 in order to raise num1 to the power of num2."""
num1 = 10
num2 = 5

num3 =pow(num1, num2)

print(num3 == 100000)


"""
question_33
Given the code below, use the correct logical operator in between the two expressions
 on line 1 in order for the final result to be False.

"""

result = ((25 % 7 + 10 / 2) % 3 == 0) and ((abs(-19) / 2 - 2) > 9)

print(result)


"""
question_34
Given the code below, use the correct logical operator in between the two 
expressions on line 1 in order for the final result to be True.
"""
result = (min(pow(2, abs(3)), 9) == 3 ** 2 - 1) or (66 % 20 + 2 > 2 ** 3)
print(result)


"""
question_35
Given the code below, use the correct function on line 1 (for which the argument sits inside the parentheses) 
in order for the final result to be False.

"""

result = bool(150 % (10 ** 2 / 2))
print(result)



"""
question_36
Given the code below, use the correct method on line 3 in order to find out the number of elements in my_list.

"""

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
char = len(my_list)
print(char)


"""
question_37
Given the code below, use the correct code on line 3 in order to remove the element of my_list located at index 5."""
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
my_list.pop(5)
print(my_list)




"""
question_38
Given the code below, use the correct method on line 3 in order to add the element 'C++' at the end of my_list.

"""
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
my_list.append("c++")
print(my_list)


"""
question_39
Given the code below, use the correct method on line 3 in order to remove the element 30 from my_list.

"""
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
my_list.remove(30)
print(my_list)



"""
question_40
Given the code below, use the correct method on line 3 in order to return the index of the element 10.5 in my_list.


"""

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']


index = my_list.index(10.5)

print(index)


"""
question_41
Given the code below, use the correct method on line 3 in order to insert the element 77 at index 4 in my_list.

"""

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_list.insert(4, 77)

print(my_list)


"""
question_42
Given the code below, use the correct method on line 3 in order to concatenate my_list
 with [100, 101, 102], by adding the latter at the end of my_list.

"""
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_list.extend([100,101,102])

print(my_list)


"""
question_43
Given the code below, use the correct method on line 3 in order to find out how many times does the element 20 occur in my_list."""
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

howmany = my_list.count(20)

print(howmany)



"""question_44
Given the code below, use the correct function on line 3 in order to sort the elements of my_list in ascending order.
"""

my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]

asc = sorted(my_list)

print(asc)

"""
question_45
Given the code below, use the correct function (and argument) on line 3 in order to sort the elements of my_list in descending order.

"""
my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]

asc = sorted(my_list, reverse= True)

print(asc)
"""
question_46
Given the code below, use the correct function on line 3 in order to find out the smallest number in my_list.

"""

my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]

small = min(my_list)

print(small)


""""
question_47
Given the code below, use the correct function on line 3 in order to find out the largest number in my_list."""
my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]
large = max(my_list)
print(large)



"""
question_48
Given the code below, use the correct function on line 3 in order to get the sum of all the elements of my_list.

"""

my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]

def sum_of_all_numbers(my_list):
    total = 0
    for i in my_list:
        total += i
    return total

x = sum_of_all_numbers(my_list)
print(x)


"""
question_49
Given the code below, use the correct method on line 3 in order to delete all the elements from my_list and obtain an empty list.

"""
my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]
my_list.clear()
print(my_list)



"""
question_50
Given the code below, use the correct operators and parentheses on line 3 in order to add the
 elements of [30.01, 30.02, 30.03] to my_list and multiply the resulting list by 2."""
my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]

add = (my_list + [30.01, 30.02, 30.03])*2

print(add)


"""
question_51
Given the code below, use the correct code on line 3 in order to return the element 20 from my_list based on its index"""

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

element = my_list[2]

print(element)

"""
question_52
Given the code below, use the correct code on line 3 in order to return the element Java from my_list based on its index (negative).


"""
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

element = my_list[-2]

print(element)


"""
question_53
Given the code below, use the correct code on line 3 in order to return a slice made of
 [30, 'Python', 'Java'] from my_list based on positive indexes."""

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_slice = my_list[3:6]

print(my_slice)


"""
question_54
Given the code below, use the correct code on line 3 in order to return a slice made of 
[30, 'Python', 'Java'] from my_list based on negative indexes."""


my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_slice = my_list[-4:-1]

print(my_slice)


"""
question_55
Given the code below, use the correct code on line 3 in order to return my_list 
except the first 3 elements, using a single, positive index."""

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_slice = my_list[3:]

print(my_slice)


"""question_56
Given the code below, use the correct code on line 3 in order to return my_list except 
the last 4 elements, using a single, negative index.

"""
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_slice = my_list[:-4]

print(my_slice)


"""
question_57
Given the code below, use the correct code on line 3 in order to return my_list 
except the first 3 elements, using a single, negative index."""
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_slice = my_list[-4:]

print(my_slice)


"""
question_58
Given the code below, use the correct code on line 3 in order to return my_list except the last 2
 elements, using a single, positive index.

"""
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
my_slice = my_list[:5]
print(my_slice)



"""
question_59
Given the code below, use the correct code on line 3 in order to return every third element
 of my_list starting with the first element of the list.

"""

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
my_slice = my_list[::3]
print(my_slice)


"""
question_60
Given the code below, use the correct code on line 3 in order to return every fourth element
 of my_list starting with the last element of the list.

"""

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
my_slice = my_list[::-4]
print(my_slice)


# set
"""question_61
Given the code below, use the correct function on line 3 in order to convert my_list to a set.

"""

my_list = [1, 2, 3, 4, 4, 5, 2, 9, 8, 8, 4, 3]
my_set = set(my_list)
print(my_set)

"""
question_62
Given the code below, use the correct function on line 3 in order to convert my_list to a frozen set.

"""

my_list = [1, 2, 3, 4, 4, 5, 2, 9, 8, 8, 4, 3]

my_set = frozenset(my_list)

print(type(my_set))



"""
question_63
Given the code below, use the correct code on line 3 in order to verify if element 10 is in my_set.

"""

my_set = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}

check = 10 in my_set

print(check)


"""
question_64
Given the code below, use the correct method on line 3 in order to add the element 19 to my_set.

"""

my_set = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}

my_set.add(19)

print(my_set)



"""
question_65
Given the code below, use the correct method on line 3 in order to delete the element 9 from my_set.

"""

my_set = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}

my_set.remove(9)

print(my_set)



"""
question_66
Given the code below, use the correct method on line 4 in order to find out the common elements of my_set1 and my_set2.

"""

my_set1 = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}
my_set2 = {12, 9, 4, 2, 0, 6}

common = my_set1.intersection(my_set2)

print(sorted(list(common)))


"""question_67
Given the code below, use the correct method on line 4 in order to join the elements of my_set1 and my_set2.

"""
my_set1 = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}
my_set2 = {12, 9, 4, 2, 0, 6}

join = my_set1.union(my_set2)

print(sorted(list(join)))


"""
question_68
Given the code below, use the correct method on line 4 in order to find out the elements of my_set2 that are not members of my_set1.

"""
my_set1 = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}
my_set2 = {12, 9, 4, 2, 0, 6}

diff = my_set2.difference(my_set1)

print(sorted(list(diff)))


"""
question_69
Given the code below, use the correct method on line 3 in order to find out the number of elements in my_tup.

"""

my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

number = len(my_tup)

print(number)


"""
question_70
Given the code below, use the correct method on line 3 in order to find out the index of Slovakia in my_tup.

"""

my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

index = my_tup.index("Slovakia")

print(index)


"""
question_71
Given the code below, write code in order to perform tuple assignment on line 3 and obtain the results below.

"""
my_tup = ("Romania", "Poland", "Estonia")

(ro, po, es) = my_tup

print(ro + ", " + po + ", " + es)




"""
question_72
Given the code below, use the correct method on line 3 in order to find out the last element of my_tup in alphabetical order.

"""

my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

last = max(my_tup)

print(last)

"""
question_73
Given the code below, use the correct method on line 3 in order to find out the number of occurrences of Estonia in my_tup.

"""

my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Estonia", "Romania", "Hungary", "Slovenia")

number = my_tup.count("Estonia")

print(number)




"""

question_74

Given the code below, use the correct slice on line 3 in order to return all the elements of my_tup, except the first two of them, using a negative index.

"""

my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

my_slice = my_tup[-5:]

print(my_slice)


"""
questio_75
Given the code below, use the correct slice on line 3 in order to return all the elements of my_tup, except the last three of them, using a negative index.

"""

my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

my_slice = my_tup[:-3]

print(my_slice)


"""
question_76
Given the code below, use the correct slice on line 3 in order to return all the elements of my_tup, except the first three of them, using a positive index.

"""

my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

my_slice = my_tup[3:]

print(my_slice)


"""
question_77
Given the code below, use the correct slice on line 3 in order to return all the elements of my_tup, except the last two of them, using a positive index.

"""
my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

my_slice = my_tup[:5]

print(my_slice)


"""
question_78
Given the code below, use the correct argument(s) for the range() function on line 1 in order to return a range
 of consecutive integers from 0 to 9 inclusively. Use a single argument inside the parentheses of range()!

"""

my_range = range(10)
print(list(my_range))


"""
question_79
Given the code below, use the correct argument(s) for the range() function on line 1 in order to
 return a range of consecutive integers from 0 to 9 inclusively. Use two arguments inside the parentheses of range()!"""


my_range = range(0,10)
print(list(my_range))


"""
question_80
Given the code below, use the correct argument(s) for the range() function on line 1 in order
 to return a range of consecutive integers from 117 to 129 exclusively."""


my_range = range(117,129)
print(list(my_range))

"""
question_81
Given the code below, use the correct argument(s) for the range() function on line 1 in order to return [10, 13, 16, 19] when converted to a list.

"""


my_range = range(10,20,3)
print(list(my_range))


"""
question_82
Given the code below, add the correct step as the third argument of the range() function on line
 1 in order to return [115, 120] when converted to a list."""

my_range = range(115,125,5)
print(list(my_range))

"""
question_83
Given the code below, add the correct step as the third argument of the range() 
function on line 1 in order to return [-75, -60, -45, -30] when converted to a list.

"""

my_range = range(-75,-25,15)
print(list(my_range))


"""
question_84
Given the code below, add the correct step as the third argument of the range()
 function on line 1 in order to return [-25, 5, 35, 65, 95, 125] when converted to a list.

"""
my_range = range(-25,126,30)
print(list(my_range))

"""
question_85
Given the code below, write the correct range on line 1 in order to return [-10] when converted to a list.

"""
my_range = range(-10,-9)
print(list(my_range))


"""
question_86
Given the code below, use the correct code on line 3 in order to return the value
 associated with key 4. Do not use a method as a solution for this exercise!"""

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

value = crypto[4]

print(value)


"""question_87
Given the code below, use the correct code on line 3 in order to return the value associated with key 4. This time, use a method as a solution for this exercise!"""

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

value = crypto.get(4)

print(value)

"""
question_88
Given the code below, use the correct code on line 3 in order to update the value associated with key 4 to "Cardano"."""
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

crypto[4]="Cardano"

print(crypto[4])

"""
question_89
Given the code below, use the correct code on line 3 in order to add a new key-value pair to the dictionary: 6: "Monero"""

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

crypto[6] = "Monero"

print(crypto[6])
print(crypto)


"""
question_90
Given the code below, use the correct code on line 3 in order to return the number of key-value pairs in the dictionary.


"""
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

number = len(crypto)

print(number)


"""
question_91
Given the code below, use the correct code on line 3 in order to delete the key-value pair associated with key 3. Do not use a method as a solution for this exercise!

"""

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

del crypto[3]

print(crypto)


"""
question_92
Given the code below, use the correct code on line 3 in order to delete the key-value pair associated with key 3. This time, use a method as a solution for this exercise!

"""

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

crypto.pop(3)

print(crypto)



"""question_93
Given the code below, use the correct code on line 3 in order to verify that 7 is not a key in the dictionary.

"""

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

check = 7 not in crypto

print(check)



"""
question_94
Given the code below, use the correct method on line 3 in order to delete all the elements in the dictionary.

"""

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

crypto.clear()

print(crypto)

"""
question_95
Given the code below, use the correct code on line 3 in order to get a list of tuples,
 where each tuple represents a key-value pair in the dictionary.

"""

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

result = crypto.items()

print(list(result))


"""
question_96
Given the code below, use the correct function on line 3 in order to get the sum of all the keys in the dictionary.
"""
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

def sum_of_values(crypto):
    total = 0
    for i in crypto.keys():
        total += i
    return total

print(sum_of_values(crypto))


"""
question_97
Given the code below, use the correct method on line 3 in order to get a list of all the values in the dictionary.
"""
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

for key,value in crypto.items():
    print(value)




"""
question_98
Given the code below, use the correct function on line 3 in order to get the smallest key in the dictionary.

Given the code below, use the correct function on line 3 in order to get the smallest key in the dictionary.

"""

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
def min_number(crypto):
    min =  list(crypto.keys())[0]
    for i in crypto.keys():
        if i < min:
            min = i
    return min

print(min_number(crypto))


"""question_99
Given the code below, use the correct method on line 3 in order to get a list of all the keys in the dictionary."""

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

for key,value in crypto.items():
    print(key)


"""   

question_100
Given the code below, use the correct method on line 3 in order to return and remove an arbitrary key-value pair from the dictionary."""


crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

crypto.popitem()

print(len(crypto))


"""
question_101
Given the code below, use the correct function on line 3 in order to convert value to a string."""
value = 5
conver = str(value)
print(type(conver))


"""
question_102
Given the code below, use the correct function on line 3 in order to convert value to an integer.

"""
value = "10"
conver = int(value)
print(type(conver))



"""
question_103
Given the code below, use the correct function on line 3 in order to convert value to a floating-point number."""

value = "10"
conver = float(value)
print(type(conver))

"""
question_104
Given the code below, use the correct function on line 3 in order to convert value to a list.

"""

value = "hello"
conver = list(value)
print(type(conver))



"""
question_105
Given the code below, use the correct function on line 3 in order to convert value to a tuple."""
value = [1, 2, 3, 10, 20, 30]
conver = tuple(value)

print(type(conver))



"""
question_106
Given the code below, use the correct function on line 3 in order to convert value to a frozen set.

"""
value = (10, 20, 40, 10, 25, 30, 45)
conver = frozenset(value)
print(type(conver))


"""
question_107
Given the code below, use the correct function on line 3 in order to convert value to a binary representation.

"""

# value = "Hello!"
#
# conv =  bin(value)

# print(type(conv))



"""
question_-108
Given the code below, use the correct function on line 3 in order to convert value to a hexadecimal representation.

"""
value = 10

conv =  hex(10)

print(type(conv))


"""
question_109
Given the code below, use the correct function on line 3 in order to convert value from binary to decimal notation."""

value = '0b1010'

conv = int(value, 2)

print(conv)


"""
question_110
Given the code below, use the correct function on line 3 in order to convert value from hexadecimal to decimal notation."""
value = '0xa'

conv = int(value, 16)

print(conv)


"""
question_111
Considering the code below, write code that prints out True! if x has 50 characters or more."""

x = "The days of Python 2 are almost over. Python 3 is the king now."

if len(x) >= 50:
    print("true")



"""
question_112
Considering the code below, write code that prints out True! if x is a string and the first character in the string is T.

"""
x = "The days of Python 2 are almost over. Python 3 is the king now."
if type(x) is str and x.startswith("T"):
    print("true")


"""
question_113
Considering the code below, write code that prints out True! if at least one of the following conditions occurs:

the string contains the character z

the string contains the character y at least twice"""

x = "The days of Python 2 are almost over. Python 3 is the king now."
if "z" in x or x.count("y") >= 2:
    print("true")

"""
question_114
Considering the code below, write code that prints out True!
 if the index of the first occurrence of letter f is less than
  10 and prints out False! if the same condition is not satisfied."""
  
x = "The days of Python 2 are almost over. Python 3 is the king now."

if x.index("f") < 10:
    print("true")
else:
    print("false")


"""
question_115
Considering the code below, write code that prints out True! if the last 3
 characters of the string are all digits and prints out False! otherwise.
    
"""
x = "The days of Python 2 are almost over. Python 3 is the king now."
if x[-3:].isdigit():
    print("true")
else:
    print("false")


"""
question_116
Considering the code below, write code that prints out True! if x has 
at least 8 elements and the element positioned at index 6 is a 
floating-point number and prints out False! otherwise.

"""
x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]
if len(x) >= 8 and type(x[6]) is float:
    print("true")
else:
    print("false")

"""
question_117
Considering the code below, write code that prints out True! if the second string of the first list in
x ends with the letter h and the first string of the second list in x also ends with the letter h, and 
prints out False! otherwise."""


x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]
if x[3][1].endswith("h") and x[7][0].endswith("h"):
    print("true")
else:
    print("false")



"""
question_118
Considering the code below, write code that prints out True! if one of the following two conditions are satisfied and prints out False! otherwise.

the third string of the first list in x ends with the letter h

the second string of the second list in x also ends with the letter h"""
x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]
if x[3][2].endswith("h") or x[7][1].endswith("h"):
    print("true")
else:
    print("false")


"""
question_119
Considering the code below, write code that prints out True! if the largest value among the first 3 elements of 
the list is less than or equal to the smallest value among the next 3 elements of the list. Otherwise, print out False!"""

x = [115, 115.9, 116.01, 109, 115, 119.5, ["length", "width", "height"]]
if max(x[:3]) <= min(x[3:6]):
    print("true")
else:
    print("false")

"""
question_120
Considering the code below, write code that prints out True! if 115 appears at least once inside the list or
 if it is the first element in the list. Otherwise, print out False!"""

x = [115, 115.9, 116.01, 109, 115, 119.5, ["length", "width", "height"]]

if x.count(115) >= 1 or x.index(115) == 0:
    print("true")
else:
    print("false")

