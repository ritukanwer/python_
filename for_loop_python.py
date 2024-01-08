
# Print the first 10 natural numbers using for loop.
for i in range(0,11):
    print(i)


# Python program to print all the even numbers within the given range.
def evens_in_range():
    for i in range(10):
        if i %2 == 0:
            print(i)

evens_in_range()


# Example 3: Python program to calculate the sum of all numbers from 1 to a given number.

def sum_of_all_in_range():
    sum = 0
    for i in range(10):
        sum = sum+i
    return sum
print(sum_of_all_in_range())


# Example 4: Python program to calculate the sum of all the odd numbers within the given range.
def sum_of_odd():
    sum = 0
    for i in range(10):
        if i % 2 != 0:
            sum = sum + i
    return sum
print(sum_of_odd())


# Example 5: Python program to print a multiplication table of a given number
def multiplication_of_5():
    given_number = 5

    for i in range(11):
        print(given_number, "x", i, "=", 5 * i)
multiplication_of_5()



# Example 6: Python program to display numbers from a list using a for loop.
list = [2,3,4,1,4,56,7,5,7]
def display_numbers(list):
    for i in list:
        print(i)

display_numbers(list)



# Example 7: Python program to count the total number of digits in a number.
num = 123456
num = str(num)
def count_digits(num):
    count = 0
    for i in num:
        count += 1
    return count
print(count_digits(num))


# Example 8: Python program to check if the given string is a palindrome.

string = "mumum"
def palindrome_or_not(string):
    reverse = ""
    for i in string:
        reverse = i + reverse
    if (string == reverse):
        print("The string", string, "is a Palindrome.")
    else:
        print("The string", string, "is NOT a Palindrome.")
palindrome_or_not(string)



# Example 9: Python program that accepts a word from the user and reverses it.
given_string = "ritu"
def reverse_word(given_string):
    reverse_string = ""
    for i in given_string:
        reverse_string = i + reverse_string
    return reverse_string
print(reverse_word(given_string))


# # Example 10: Python program to check if a given number is an Armstrong number
given_number = 153
def armstrong_number(given_number):
    given_number = str(given_number)
    string_length = len(given_number)
    sum = 0
    for i in given_number:
        sum += int(i) ** string_length
    if sum == int(given_number):
        print("Amstrong number")
    else:
        print("Not an Amstrong number")
armstrong_number(given_number)

# #11 Example  Python program to find what is even and odd numbers from a series of numbers.
num_list = [1, 3, 5, 6, 99, 134, 55]
def the_number_is_even_or_odd(num_list):

    for i in num_list:
        if i % 2 == 0:
            print(i, "even number.")
        else:
            print(i, "odd number.")
the_number_is_even_or_odd(num_list)

# # Example 12: Python program to count the number of even and odd numbers from a series of numbers.
num_list = [1, 3, 5, 6, 99, 134, 55]
def count_even_numbers(num_list):
    count_even = 0
    for i in num_list:
        if i % 2 == 0:
            count_even += 1

    return count_even
print(count_even_numbers(num_list))


def count_odd_numbers(num_list):
    count_odd = 0
    for i in num_list:
        if i % 2 != 0:
            count_odd += 1

    return count_odd
print(count_odd_numbers(num_list))



# Example 14: Python program to find the factorial of a given number.
given_number = 5
factorial = 1
for i in range(1, given_number + 1):
    factorial = factorial * i

print(factorial)


#