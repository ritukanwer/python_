# QUESTION 1
# How many students are in the dictionary? Search for the "len" function.

ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}




def length_of_dictionary(ages):
   length  = len(ages)
   return length

x= length_of_dictionary(ages)
print("the length of dictionary:-",x)

# #
# #
# QUESTION 2
# Implement a function that receives the "ages" dictionary as parameter and returns the average age of the students.
# Traverse all items on the dictionary using the "items" method as above.


ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}

#
def average_num(ages):
    total = 0
    for i in ages.values():
        total += i

    avg_val = total / len(ages)
    return avg_val

c = average_num(ages)
print(c)




# QUESTION 3
# Implement a function that receives the "ages" dictionary as parameter and returns the name of the oldest student.

ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}


def oldest_person(ages):
    max_age = 0
    max_age_name= ' '
    for name, age in ages.items():
        # print(name, age)
        if age > max_age:
            max_age = age
            max_age_name= name
    return  max_age_name

x = oldest_person(ages)
print(x)



#quesition 4
# Implement a function that receives the "ages" dictionary and a number "n" and returns
# a new dict where each student is (n) years older. For instance, new_ages(ages, 10) returns a copy of "ages" where each student is
# 10 years older.


def function(ages,n):
    new_ages = {}
    for name, age in ages.items():

        if age == n:

            new_ages[name] = age
    return new_ages

ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}
n=10

x= function(ages,n)
print(x)


#QUESTION 5
# #How many students are in the "students" dict? Use the appropriate function.

students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}
#


def student_length(students):
   length  = len(students)
   return length

a = student_length(students)
print("students_length:-",a)



#QUESTION 7
#Implement a function that receives the students dict and an address,
# and returns a list with names of all students whose address matches the address in the argument.
# For instance, invoking "find_students(students, ’Lisbon’)" should return Peter and Anna
students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}


def function(student, x):
    new_dictionary = {}
    for p, q in students.items():
        # print(x,y)
        for a, b in q.items():
            if x == b:
                new_dictionary[p] = b
    return new_dictionary



y = function(students, x='Lisbon')
print(y)







# 6
# Implement a function that receives the students dict and returns the average age.
students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}


def average_of_student(students):
    total = 0
    for i in students.keys():
        total += students[i]['age']
    average = total/len(students)
    return average
average = average_of_student(students)

print(average)





















