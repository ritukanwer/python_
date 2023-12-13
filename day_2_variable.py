

#1 Write a python comment saying 'Day 2: 30 Days of python programming'
day2 = "30 days of python programming"
print(day2)

# 2 Declare a first name variable and assign a value to it
first_name = "ritu"
print(first_name)

#3 Declare a last name variable and assign a value to it
last_name = "naruka"
print(last_name)

#4 Declare a full name variable and assign a value to it
full_name = "ritu_naruka"
print(full_name)

#5 Declare a country variable and assign a value to it
country = "india"
print(country)

#6 Declare a city variable and assign a value to it
city = "jaipur"
print(city)

#7 Declare an age variable and assign a value to it.
age = 18
print(age)

#8 Declare a year variable and assign a value to it
year = 2023
print(year)

#9 Declare a variable is_married and assign a value to it
is_married = "No, i am not married"
print(is_married)

#10 Declare a variable is_true and assign a value to it
is_true = "true"
print(is_true)

#11 Declare a variable is_light_on and assign a value to it
is_light_on = "yes"
print(is_light_on)

#12 Declare multiple variable on one line
first_name,last_name,age,city = "ritu","naruka",18,"jaipur"
print(first_name,last_name,age,city)
print(last_name)
print(age)
print(city)


# level_2
#1 Check the data type of all your variables using type() built-in function

number = 10
print(type(number))

#2 Using the len() built-in function, find the length of your first name
name ="ritu"
print(len(name))

#3 Compare the length of your first name and your last name

first_name ="ritu"
last_name = "naruka"
if len(first_name) > len(last_name):
    print("first is long")
elif len(first_name) < len(last_name):
    print("last is long")
else:
    print("both_same")

#4 Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
#(a) Add num_one and num_two and assign the value to a variable total
add = num_one + num_two
print(add)
# (b) Subtract num_two from num_one and assign the value to a variable diff
subtract = num_one - num_two
print(subtract)
# (c) Multiply num_two and num_one and assign the value to a variable product
multiply = num_one * num_two
print(multiply)
#(d) Divide num_one by num_two and assign the value to a variable division
divide = num_one/num_two
print(divide)
#(e) Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_one % num_two
print(remainder)
#(f) Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print(exp)
#(g) Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one//num_two
print(floor_division)


#5 The radius of a circle is 30 meters
radius = 30
#(a) Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = 3.14 * radius ** 2
print(area_of_circle)
#(b) Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * 3.14 *radius
print(circum_of_circle)
#(c) Take radius as user input and calculate the area.
# radius = int(input("enter the radius :"))
# area = 3.14 * (radius ** 2)
# print(area)

#6 Use the built-in input function to get first name, last name, country
# and age from a user and store the value to their corresponding variable names

# first_name = input("enter_your_first_name:")
# last_name = input("enter_your_last_name:")
# country = input("enter_your_country:")
# age = int(input('enter_your_age'))
#
# print("first_name:", first_name )
# print("last_name:",last_name)
# print("country:", country)
# print("age:", age)

