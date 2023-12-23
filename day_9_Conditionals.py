

#
# """1
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough
# to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive."""
# age_str = input("Enter your age: ")
#
# age = int(age_str)
#
# if age >= 18:
#     print("You are old enough to learn to drive.")
# else:
#     years_to_wait = 18 - age
#     print(f"You need {years_to_wait} more years to learn to drive.")
#
# """2
# Compare the values of my_age and your_age using if … else. Who is older (me or you)?
# Use input(“Enter your age: ”) to get the age as input. You can use a nested condition
# to print 'year' for 1 year difference in age, 'years' for bigger differences, and a
# custom text if my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me."""
def compare_ages(my_age, your_age):
    if my_age < your_age:
        age_difference = your_age - my_age
        return f"You are {age_difference} {'year' if age_difference == 1 else 'years'} older than me."
    elif my_age > your_age:
        age_difference = my_age - your_age
        return f"I am {age_difference} {'year' if age_difference == 1 else 'years'} older than you."
    else:
        return "We are the same age."
your_age = int(input("Enter your age: "))
my_age = 25
result = compare_ages(my_age, your_age)
print(result)

#
#
# """3
# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b,
#  if a is less b return a is smaller than b, else a is equal to b. Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
# """
#
# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
#
# if a > b :
#     print(" a in greater than b")
# elif a < b:
#     print("a is less than b")
# else:
#     print("a is equal to b")

# """level two
# 1 Write a code which gives grade to students according to theirs scores:
#
# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F"""

# score = float(input("Enter the student's score: "))
# def calculate_grade(score):
#     if 100 >= score >= 80:
#         return 'A'
#     elif 89 >= score >= 70:
#         return 'B'
#     elif 69 >= score >= 60:
#         return 'C'
#     elif 59 >= score >= 50:
#         return 'D'
#     elif 49 >= score >= 0:
#         return 'F'
#     else:
#         return 'Invalid Score'
# print(calculate_grade(score))
#
#

#"""2 Check if the season is Autumn, Winter, Spring or Summer.
# If the user input is: September, October or November,
# the season is Autumn. December, January or February, the season is Winter
# . March, April or May, the season is Spring June, July or August, the season is Summer
# """
# user_input = input("Enter a month: ")
# def get_season(month):
#     if month in ['september', 'october', 'november']:
#         return 'Autumn'
#     elif month in ['december', 'january', 'february']:
#         return 'Winter'
#     elif month in ['march', 'april', 'may']:
#         return 'Spring'
#     elif month in ['june', 'july', 'august']:
#         return 'Summer'
#     else:
#         return 'Invalid Month'
# season = get_season(user_input)
# print(season)



# """
# The following list contains some fruits:
#
# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and
#  print the modified list. If the fruit exists
#   print('That fruit already exist in the list')
# """
fruits = ['banana', 'orange', 'mango', 'lemon']


