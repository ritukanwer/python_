# 1 Declare your age as integer variable
int = 18
print(int)

# 2 Declare your height as a float variable
heigth = 5.3
print(heigth)

#3 Declare a variable that store a complex number
complex_number = (2,3)
print(complex_number)


# 4 Write a script that prompts the user to enter base and height of
# the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#     Enter base: 20
#     Enter height: 10
#     The area of the triangle is 100

# base = float(input("enter your base:"))
# hight = float(input("enter your hight:"))
# area = 0.5 * base * hight
# print(area)


#5 Write a script that prompts the user to enter side a, side b,
# and side c of the triangle. Calculate the perimeter of the
# triangle (perimeter = a + b + c).
# Enter side a: 5
# Enter side b: 4
# Enter side c: 3
# The perimeter of the triangle is 12
#
# side_a = float(input("enter side a:"))
# side_b = float(input("enter side b:"))
# side_c = float(input("enter side c:"))
# perimeter = side_a + side_b + side_c
# print(perimeter)

#6
# Get length and width of a rectangle using prompt. Calculate its area
# (area = length x width) and perimeter (perimeter = 2 x (length + width))

# length = float(input("enter your length: "))
# width = float(input("enter your width:"))
#
# area = length * width
# perimeter = 2 * (length * width)
#
# print("area:-", area)
# print("perimeter:-", perimeter)


#7 Get radius of a circle using prompt. Calculate the area (area = pi x r x r)
# and circumference (c = 2 x pi x r) where pi = 3.14

# redius = float(input("enter your redius:"))
#
# pi = 3.14
# area = pi * redius * redius
# circumference = 2 * pi * redius
# print("area:", area)
# print("circumference:", circumference)
#
# 8 Calculate the slope, x-intercept and y-intercept of y = 2x -2
# 9


# 12
# Find the length of the strings
length_python = len('python')
length_dragon = len('dragon')

if length_python == length_dragon:
    print("The lengths are equal")
else:
    print("The lengths are not equal")

# 13Use and operator to check if 'on' is found in both 'python' and 'dragon'

string1 = 'python'
string2 = 'dragon'

if 'on' in string1 and 'on' in string2:
    print("'on' is found in both 'python' and 'dragon'.")
else:
    print("'on' is not found in both 'python' and 'dragon'.")

#14 I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon."

if 'jargon' in sentence:
    print("'jargon' is present in the sentence.")
else:
    print("'jargon' is not present in the sentence.")

#15There is no 'on' in both dragon and python

string1 = 'python'
string2 = 'dragon'

if 'on' not in string1 and 'on' not in string2:
    print("'on' is not found in both 'dragon' and 'python'")
else:
    print("'on' is found in either 'dragon' or 'python'")




#16 Find the length of the text python and convert the value to float and convert it to string
text = "python"
print(len(text))
float = float(len(text))
print(float)
string = str(float)
print(string)

# 17 Even numbers are divisible by 2 and the remainder is zero.
# How do you check if a number is even or not using python?
number = 10
def find_even_or_not(number):
    if number % 2==0:
        print("even")
    else:
        print("odd")
find_even_or_not(number)

#18Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
def check_floor_division():
    result = 7 // 3
    value = 2.7
    if result == value:
        return "Equal to 2.7."
    else:
        return "Not equal to 2.7."

print(check_floor_division())


# 19Check if type of '10' is equal to type of 10
string = '10'
int = 10

if string == int:
    print("equal_to")
else:
    print("not_equal")


# 20 Check if int('9.8') is equal to 10
string = "9.8"
int = 10
if string == int:
    print("equal_to")
else:
    print("not_equal")

# 21Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120

# hours = input("Enter hours:- ")
# rate_per_hour = input("Enter rate per hour:- ")

weekly_earning = hours * rate_per_hour

print(weekly_earning)

#
# 22Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.

years_lived = input("Enter the number of years you have lived:- ")
seconds_lived = years_lived * 365.25 * 24 * 60 * 60
print(f"You have lived for {int(seconds_lived)}) seconds.")
#
# 23Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
for i in range(1, 6):
    print(f"{i} 1 {i} {i**2} {i**3}")
