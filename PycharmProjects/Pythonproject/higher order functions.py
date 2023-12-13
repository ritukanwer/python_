##def sum_numbers(nums):
  #  return sum(nums)
#
#def higher_order_function(f,lst):
# summation = f(lst)
  #  return summation
#result = higher_order_function(sum_numbers,[1,2,3,4,5])
#print(result)


#def square(x):
 #   return x ** 2

#def cube(x):
#    return x ** 3

#def absolute(x):
#    if x >= 0:
  #      return x
  #  else:
  #     return -(x)

#def higher_order_function(type):
   # if type == 'square':
    #    return square
   # if type == 'cube':
    #    return cube
   # elif type  ==  'absolute':
      #  return absolute

#result = higher_order_function('square')
#print(result(3))
#result =  higher_order_function('cube')
#print(result(3))
#result =  higher_order_function('absolute')
#print(result(-3))

#def add_ten():
#   ten = 10
    #def add(num):
   #     return num + ten
  #  return add
#closure_result  =  add_ten()
#print(closure_result(5))
#print(closure_result(10))


#def greeting():
 #   return 'welcome to python'
#def uppercase_decorator(function):
 #   def wrapper():
  #      func = function()
   #     make_uppercase =func.upper()
    #    return make_uppercase
    #return wrapper
#@uppercase_decorator
#def greeting():
 #   return 'welcome to python'
#print(greeting())


#def uppercase_decorator(function):
    #def wrapper():
    #    func = function()
   #     make_uppercase = func.upper()
  #      return make_uppercase
 #   return wrapper

#def split_string_decorator(function):
    #    def wrapper():
   #         splitted_string = func.split()
  #          return splitted_string

 #       return wrapper

#@split_string_decorator
#@uppercase_decorator
#def greeting():
 #   return 'welcome to python'
#print(greeting())


numbers = [1,2,3,4,5]
def square(x):
    return x ** 2
numbers_squared = map(square,numbers)
print(list(numbers_squared))
numbers_squared = map(lambda X : X ** 2, numbers)
print(list(numbers_squared))

#numbers_str = ['1','2','3','4','5']
#numbers_int = map(int,numbers_str)
#print(list(numbers_int))

#names = ['ritu','poonam','kumkum','rita']

#def change_to_upper(names):
#    return names.upper()

#names_upper_cased = map(change_to_upper,names)
#print(list(names_upper_cased))
#names_upper_cased = map(lambda name: name.upper(),names)
#print(list(names_upper_cased))

#numbers = [1,2,3,4,5]

#def is_even(num):
#    if num % 2 == 0:
#        return True
#    return False

#even_numbers = filter(is_even,numbers)
#print(list(even_numbers))

#numbers = [1,2,3,4,5]

#def is_odd(num):
#    if num % 2 != 0:
#        return True
#    return False

#odd_numbers = filter(is_odd,numbers)
#print(list(odd_numbers))


#names = ['ritu','poonam','kumkum','ritanaruka']
#def is_name_long(name):
 #  if len(name) > 7:
  #      return True
   # return False

#long_names = filter(is_name_long, names)
#print(list(long_names))

numbers_str = ['1','2','3','4','5']
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums,numbers_str)
print(total)