
num = 11
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "false")
            break
    else:
        print(num, "true")
else:
    print(num, "false")

#
list = [5,6,7,8,9,4]
print("the original list is : " + str(list))
res = False
x = list[0]
c=0
for i in list:
    if(type(x))==type(i):
        c+=1
if(c==len(list)):
    res = True
print(str(res))







a = 3
if a > 0:
    print('A is a positive number')



a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')



a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')




a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')






# question :-

#1
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback:
# You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to
#


age = int(input("enter your age: "))
if (age >= 18):
    print("You are old enough to learn to drive.")
elif (age == 15):
    print("You need 3 more years to learn to drive.")
#
else:
    print("not eligible to drive")

#2
# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”)
# to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger
# differences, and a custom text if my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me.
age = int(input("enter your age: "))
my_age = 25

if age == my_age:
    print("we are the same age")
elif age > my_age:
    print("you are", age - my_age, "years older then me" )
else:
    print("i am", my_age - age,"years older then you")



#3
# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3



a = input("enter your first number: ")
b = input("enter your second number: ")

if a > b:
    print("4 is greater than 3")

else:
    print(" 4 is less then 3")
# 1
# Write a code which gives grade to students according to theirs scores:

80-100, A
70-89, B
60-69, C
50-59, D
0-49, F

mar = int(input("enter the marks"))
if mar>=80 and mar< 100:
    print("your gread is =", "A")
elif  mar >=70 and mar<=79:
    print("your gread is =","B")
elif  mar >=60 and mar<=69:
    print("your gread is =","C")
elif  mar >=50 and mar<=59:
    print("your gread is =","D")
elif  mar >=0 and mar<=49:
    print("your gread is =","F")
#2
# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November,
# the season is Autumn. December, January or February, the season is Winter.
# March, April or May, the season is Spring June, July or August, the season is Summer
month  = input("Enter season name")
if month in ("september","october","november"):
    print("season is :","Autumn")
elif month in ("december", "january", "february"):
    print("season is :", "winter")
elif month in ("march", "april", "may"):
    print("season is :", "spring")
elif month in ("june", "july","august"):
    print("season is :", "summer")



#3
fruits = ['banana', 'orange', 'mango', 'lemon']

if('banana' in fruits):
    print("That fruit already exist in the fruits list")

else:
    print("that fruit in not already exit")


# 4
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if person['skills']:
    print(person['skills'][len(person['skills'])//2])
    print("python" in person['skills'])
if ['Javascript','React'] == person['skills']:
    print('front end developer')
elif ['Node','MongoDB','React'] == person['skills']:
    print('full stack developer')
else:
    print('unknown title')
if person['is_marred']:
    print(person['first_name'],person['last_name'], "lives in", person['country'],'he is married')
else:
    print(person['first_name'],person['last_name'], "lives in", person['country'],'he is not married')