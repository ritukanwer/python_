


# 1 Declare an empty list
list1 = []
print(list1)


# 2Declare a list with more than 5 items
list1 = ['ritu','rina','rishi','savi','raj','ranu']
print(list1)

#3Find the length of your list
list1 = ['ritu','rina','rishi','savi','raj','ranu']
print(len(list1))


#4 Get the first item, the middle item and the last item of the list
list1 = ['ritu','rina','rishi','savi','raj']
first_item =list1[0]
print(first_item)

middle_item = list1[2]
print(middle_item)

last_item = list1[-1]
print(last_item)


# 5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_type = ["ritu",18,5.6,'chandma']
print(mixed_data_type)


#6 Declare a list variable named it_companies and assign initial values Facebook, Google,
# Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']
print(it_companies)

#7 Print the list using print()
list = ['ritu','naruka']
print(list)


#8 Print the list using print()
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']
print(len(it_companies))


# 9 Print the first, middle and last company
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']
first = it_companies[0]
middle = it_companies[3]
last = it_companies[-1]
print(first)
print(middle)
print(last)


# 10 Print the list after modifying one of the companies
it_companies = ['Facebook', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']
it_companies.append('google')
print(it_companies)

# 11 Add an IT company to it_companies
it_companies = ['Facebook', 'Microsoft', 'google', 'IBM', 'Oracle','Amazon']
it_companies.append('apple')
print(it_companies)


# 12 Insert an IT company in the middle of the companies list
it_companies = ['Facebook', 'Microsoft', 'google', 'IBM', 'Oracle','Amazon']
it_companies.insert(3,'apple')
print(it_companies)


# 13 Change one of the it_companies names to uppercase (IBM excluded!)

it_companies = ['Facebook', 'Microsoft', 'google', 'IBM', 'Oracle', 'Amazon']
index = -2
it_companies[index] = it_companies[index].upper()
print(it_companies)


# 14 Join the it_companies with a string '#;
it_companies = ['Facebook', 'Microsoft', 'google', 'IBM', 'Oracle', 'Amazon']
result_string = '#;'.join(it_companies)
print(result_string)


# 15 Check if a certain company exists in the it_companies list.
it_companies = ['Facebook', 'Microsoft', 'google', 'IBM', 'Oracle', 'Amazon']
string = "Facebook" in it_companies
print(string)


# 16 Sort the list using sort() method
lis = [90,10,20,40,30,60,70,91]
lis.sort()
print(lis)


# 17 Reverse the list in descending order using reverse() method
lis = [90,10,20,40,30,60,70,91]
lis.reverse()
print(lis)

# 18Slice out the first 3 companies from the list
it_companies = ['Facebook', 'google', 'IBM', 'Oracle', 'Amazon']
first_three_companies = it_companies[:3]
print(first_three_companies)

# 19 Slice out the last 3 companies from the list
it_companies = ['Facebook', 'google', 'IBM', 'Oracle', 'Amazon']
last_three = it_companies[-3:]
print(last_three)

# 20 Slice out the middle IT company or companies from the list
it_companies = ['Facebook', 'google', 'IBM', 'Oracle', 'Amazon']
middle = it_companies[2:4:2]
print(middle)


# 21Remove the first IT company from the list
it_companies = ['Facebook', 'google', 'IBM', 'Oracle', 'Amazon']
del it_companies[0]
print(it_companies)

# 22Remove the middle IT company or companies from the list
it_companies = ['Facebook', 'google', 'IBM', 'Oracle', 'Amazon']
it_companies.remove("IBM")
print(it_companies)

# 23 Remove the last IT company from the list
it_companies = ['Facebook', 'google', 'IBM', 'Oracle', 'Amazon']
it_companies.pop()
print(it_companies)


# 24Remove all IT companies from the list
it_companies = ['Facebook', 'google', 'IBM', 'Oracle', 'Amazon']
it_companies.clear()
print(it_companies)

# 25 Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)

# 26After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack.
# Then insert Python and SQL after Redux.

full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
full_stack.insert(5,'python')
full_stack.insert(6,'sql')
print(full_stack)



# level_2
# Q 1 The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# (A) Sort the list and find the min and max age
# ages.sort()
# print(ages)
#
# min = ages[0]
# print(min)
#
# max = ages[-1]
# print(max)

# a = min(ages)
# b = max(ages)
# print(ages)
# print(a)
# print(b)
#
# def max(ages):
#     max = 0
#     for i in ages:
#         if i > max:
#             max = i
#     return max
# print(max(ages))
#
# def min(ages):
#     min = ages[0]
#     for i in ages:
#         if i < min:
#             i = min
#     return min
# print(min(ages))


# (B)Add the min age and the max age again to the list

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.append(min(ages))
ages.append(max(ages))

print(ages)


# (C) Find the median age (one middle item or two middle items divided by two)


# (D) Find the average age (sum of all items divided by their number )
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

def find_average(ages):
    sum = 0
    for i in ages:
        sum += i
    average = sum/len(ages)
    return average
print(find_average(ages))

# (E)Find the range of the ages (max minus min)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
age_range = max(ages) - min(ages)
print(age_range)


# (F) Compare the value of (min - average) and (max - average), use abs() method
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Calculate average, minimum, and maximum
average_age = sum(ages) / len(ages)
min_age = min(ages)
max_age = max(ages)


min_difference = abs(min_age - average_age)
max_difference = abs(max_age - average_age)
#
print(min_difference)
print(max_difference)
