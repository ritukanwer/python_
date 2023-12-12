


"""
Variables store data in a computer memory. Mnemonic variables are recommended to
use in many programming languages. A mnemonic variable is a variable name that
can be easily remembered and associated. A variable refers to a memory address
in which data is stored. Number at the beginning, special character, hyphen are
not allowed when naming a variable. A variable can have a short name (like x, y, z),
but a more descriptive name (firstname, lastname, age, country) is highly recommended.
"""
"""Python Variable Name Rules

1)A variable name must start with a letter or the underscore character
2)A variable name cannot start with a number
3)A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
4)Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)
"""

# Variables in Python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }


"""
Declaring Multiple Variable in a Line
Multiple variables can also be declared in one line:
"""
# Example:

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

"""
Data Types
There are several data types in Python. To identify the data type we use the
type built-in function. I would like to ask you to focus on understanding
different data types very well. When it comes to programming, it is all 
about data types. I introduced data types at the very beginning and it 
comes again, because every topic is related to data types. We will cover
data types in more detail in their respective sections."""


