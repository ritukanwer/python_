#try:
#    print(10 + '5')
#except:
#    print('something went wrong')


#try:
#    name = input('enter your name:')
#    year_born = input('year you were born:')
#    age = 2019 - year_born
#    print(f'you are {name}.and your age is {age}.')
#except:
#    print('something went wrong')

#try:
#    name = input('enter your name')
#    year_born = input('year you werenborn:')
#    age = 2019 - year_born
#    print(f'you are {name}.and your age is{age}:')
#except TypeError:
#    print('Type error occured')
#except ValueError:
#    print('Value error occured')
#except ZeroDivisionError:
#print('zero division error occured')


#try:
 #   name = input('enter your name:')
 #   year_born = input('year you born: ')
 #   age = 2019 - int(year_born)
 #   print('you are {name}.and your age is {age}.')
#except TypeError:
 #   print('Type error occur')
#except ValueError:
#    print('value error occur')
#except ZeroDivisionError:
#    print('zero division error occue')
#else:
#    print('I usually run with the try block')
#finally:
#    print('I alway run.')

#try:
#    name = input('Enter your name :')
#    year_born = input('year you born:')
#    age = 2019 - int(year_born)
#   print('you are {name}. and your age is {age}.')
#except Exception  as e:
#    print(e)

#def sum_of_five_nums(a,b,c,d,e):
#    return  a + b + c + d + e
#lst = [1,2,3,4,5]
#print(sum_of_five_nums(lst))


#def sum_of_five_nums(a,b,c,d,e):
#    return a + b + c + d + e
#lst = [1,2,3,4,5]
#print(sum_of_five_nums(*lst))

#numbers = range(2, 7)
#print(list(numbers))
#args = [2, 7]
#numbers = range(*args)
#print(numbers)

#countries = ['finland','sweden','norway','denmark','iceland']
#fin, sw, nor, *rest = countries
#print(fin, sw, nor, rest)
#numbers = [1,2,3,4,5,6,7]
#one, *middle,last = numbers
#print(one, middle, last)


#def unpacking_person_info(name,country,city,age):
#    return f'{name} lives in {country}{city}.he is {age} year old'
#dct = {'name':'ritu','country':'india','city':'jaipur','age':17}
#print(unpacking_person_info(**dct))


#def sum_all(*args):
#     s = 0
#     for i in args:
#         s += i
#     return s
#Print(sum_all(1,2,3))
#print(sum_all(1,2,3,4,5,6,7))

#def packing_person_info(**kwargs):
#    for key in kwargs:
#        print("{key} = {kwargs[key]}")
#    return kwargs
#print(packing_person_info(name = "ritu",
#country = "india", city = "jaipur",age=250))



#lst_one = [1,2,3]
#lst_two = [4,5,6,7]
#lst = [0,*lst_one, *lst_two]
#print(lst)
#country_lst_one = ['india','sweden','norway']
#country_lst_two = ['denmark','iceland']
#nordic_countries = [*country_lst_one, *country_lst_two]
#print(nordic_countries)

#for index, item in enumerate([20,30,40]):
#    print(index, item)

#for index, i in enumerate(countries):
 #   print('hi')
 #   if i == 'Finland':
#        print('the country {i} has been found at index {index}')


fruits = ['banana','orange','mango','lemon','lime']
vegetables = ['tomato','potato','cabbage','onion','carrot']
fruits_and_veges = []
for f, v in zip(fruits,vegetables):
    fruits_and_veges.append({'fruit':f,'veg':v})

print(fruits_and_veges)