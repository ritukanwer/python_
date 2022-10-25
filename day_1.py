from day_2 import find_even_numbers, length_of_dictionary, average_of_students, oldest_student

lst = [1,2,3,5,6,8,9,10,4]
x= find_even_numbers(lst)
print(x)


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

y = length_of_dictionary(ages)
print("the length of dictionary:- ",y)

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
a = average_of_students(ages)
print(a)

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
a = oldest_student(ages)
print(a)

