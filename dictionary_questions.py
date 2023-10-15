#dictionary
# # question 1
# # two sum
#
#
# nums = [2,15,7,11]
# target = 9
# def sum_two_elements(nums):
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if nums[i]+nums[j] == target:
#
#
#                 return[i,j]
#
#
# print(sum_two_elements(nums))
#
#
# nums = [2,5,6,4,5]
# target = 6
# def sum_two_elements(nums):
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if nums[i]+nums[j] == target:
#
#
#                 return[i,j]
#
#
# print(sum_two_elements(nums))
#
# nums = [3,3,2]
# target = 6
# def sum_two(nums):
#     for i in range(len(nums)):
#         for j in range(i+1,(len(nums))):
#             if nums[i]+nums[j] == target:
#
#
#                 return[i,j]
#
#
# print(sum_two(nums))
#
#
#
#
#add two list
# l1 =[2,4,3]
# l2 =[5,6,4]
# list  = []
# def add_two_numbers(l1,l2):
#
#     for i in range(len(l1)):
#         list.append(l1[i]+l2[i])
#
#     return list
# print(add_two_numbers(l1,l2))
#
#
#
#
#
#
#
#
#
#
# # question = 4
# # Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# num_1 = [1,3]
# num_2 = [2]
# num = num_1+num_2
# num.sort()
# print(num)
# def calculate_medean(num):
#     sum = 0
#     for i in num:
#         sum += i
#
#     midean_val = sum / len(num)
#     return midean_val
#
# c = calculate_medean(num)
# print(c)
#
#
#
# num_1 = [1,2]
# num_2 = [3,4]
# num_3 = num_1+num_2
# num_3.sort()
# print(num_3)
# def calculate_medean(num_3):
#     sum = 0
#     for  i in num_3:
#         sum += i
#     medean_value = sum/len(num_3)
#     return medean_value
# print(calculate_medean(num_3))
#
#
#
# #
# #
# # # question 7 reverse integer
# def reverse(x):
#
#     if x >= 0:
#
#         r = int(str(x)[::-1])
#         return r
#
# x = -123
#
# print(reverse(x))
# def reverse(x):
#
#     if x >= 0:
#
#         r = int(str(x)[::-1])
#         return r
#
# x = 120
#
# print(reverse(x))
# def reverse(x):
#
#     if x >= 0:
#
#         r = int(str(x)[::-1])
#         return r
#
# x = 123
#
# print(reverse(x))
# #
# #
# #
#
#
#
#
#
# #
#
# def reve(x):
#     x=str(x)
#     if x[0]=='-':
#         a=x[::-1]
#         return f"{x[0]}{a[:-1]}"
#     else:
#         return x[::-1]
# x = 120
#
# print(reve(x))
# num  = '10'
# def string_to_interger(num):
#     print(type(num))
#     con_num = int(num)
#     print(type(con_num))
#     print(con_num)
# print(string_to_interger(num))
#
#
#
#
#
#
# #question 9 Palindrome Number
# x = '121'
# def palindrome(x):
#     revers = reversed(x)
#     if list(x) == list(revers):
#         print('True','palindrome')
#
#     else:
#         print('False','not  palindrome')
#
# print(palindrome(x))
#
#
#
#
# x = '-121'
# def palindrome(x):
#     revers = reversed(x)
#     if list(x) == list(revers):
#         print('True','palindrome')
#
#     else:
#         print('False','not  palindrome')
#
# print(palindrome(x))
#
# x = '10'
# def palindrome(x):
#     revers = reversed(x)
#     if list(x) == list(revers):
#         print('True','palindrome')
#
#     else:
#         print('False','not  palindrome')
#
# print(palindrome(x))
#13
#

# #
# def interger_to_roman(s):
#     roman = {'I':1,
#              'V':5,
#              'X':10,
#              'L':50,
#              'C':100,
#              'D':500,
#              'M':1000
#              }
#     n = len(s)
#     i = n - 1
#     sum =  0
#     while i >= 0:
#         if i < n-1 and roman[s[i]]<roman[s[i+1]]:
#             sum -= roman[s[i]]
#         sum += roman[s[i]]
#         i -= 1
#     return sum
# print(interger_to_roman("III"))
#
#
#
# def interger_to_roman(s):
#     roman = {'I':1,
#              'V':5,
#              'X':10,
#              'L':50,
#              'C':100,
#              'D':500,
#              'M':1000
#              }
#     n = len(s)
#     i = n - 1
#     sum =  0
#     while i >= 0:
#         if i < n-1 and roman[s[i]]<roman[s[i+1]]:
#             sum -= roman[s[i]]
#         sum += roman[s[i]]
#         i -= 1
#     return sum
# print(interger_to_roman("LVIII"))
#
#
# def interger_to_roman(s):
#     roman = {'I':1,
#              'V':5,
#              'X':10,
#              'L':50,
#              'C':100,
#              'D':500,
#              'M':1000
#              }
#     n = len(s)
#     i = n - 1
#     sum =  0
#     while i >= 0:
#         if i < n-1 and roman[s[i]]<roman[s[i+1]]:
#             sum -= roman[s[i]]
#         sum += roman[s[i]]
#         i -= 1
#     return sum
# print(interger_to_roman("MCMXCIV"))
#
# def roman_to_interger(num):
#     res = ' '
#     roman = [(1, 'I'),
#              (5, 'V'),
#              (10 , 'X'),
#              (50 , 'L'),
#              (100, 'C'),
#              (500, 'D'),
#              (100, 'M')
#              ]
#
#
#
#
# print(roman_to_interger(1520))





# 12
# def solve(num):
#    res = ""
#    table = [
#       (1000, "M"),
#       (500, "D"),
#       (100, "C"),
#       (50, "L"),
#       (10, "X"),
#       (5, "V"),
#       (1, "I"),
#    ]
#    for key, value in table:
#       d, m = divmod(num, key)
#       res += value * d
#       num = m
#
#    return res
#
# num = 3
# print(solve(num))
#
#
def solve(num):
   res = ""
   table = [
      (1000, "M"),
      (500, "D"),
      (100, "C"),
      (50, "L"),
      (10, "X"),
      (5, "V"),
      (1, "I"),
   ]
   for key, value in table:
      d, m = divmod(num, key)
      res += value * d
      num = m

   return res

num = 58
print(solve(num))


def solve(num):
   res = ""
   table = [
      (1000, "M"),
      (500, "D"),
      (100, "C"),
      (50, "L"),
      (10, "X"),
      (5, "V"),
      (1, "I"),
   ]
   for key, value in table:
      d, m = divmod(num, key)
      res += value * d
      num = m

   return res

num = 1994
print(solve(num))