


"""
Write a function that takes in a list of dictionaries, each containing information about a person
's name, age, and a list of their favorite foods. The function should return a new list of dictionaries,' \
' where each dictionary contains the person's name and the number of favorite foods they have.
"""

"""

output -
[{'name': 'Alice', 'num_favorites': 3}, {'name': 'Bob', 'num_favorites': 3}, {'name': 'Charlie', 'num_favorites': 3},
 {'name': 'David', 'num_favorites': 3}]"""



input_list = [{'name': 'Alice', 'age': 25, 'favorite_foods': ['pizza', 'tacos', 'sushi']},
 {'name': 'Bob', 'age': 30, 'favorite_foods': ['burgers', 'fries', 'ice cream']},
 {'name': 'Charlie', 'age': 35, 'favorite_foods': ['ramen', 'pho', 'pad thai']},
 {'name': 'David', 'age': 40, 'favorite_foods': ['steak', 'lobster', 'chocolate']}]


"""i am create a function name is name_and_count_fav_food. then i a take a peramiter input_list"""
def name_and_count_fav_foods(input_list):
   #  then i take a variable answer name and create a empty list
   answer = []
   # then i started for loop in input_list. the loop is read one by one read all input_list items.
   for i in input_list:
        # then i take a variable and write name = i['name'] access all name.
      name = i['name']
        # then i took len of all number of fav_foods.
      num_favorite_foods = len(i['favorite_foods'])
        # then i append answer name of empty list and add name and favorate foods .
      answer.append({'name':name,'num_favorite_foods':num_favorite_foods})

# then i return the answer
   return answer
# then i take a  x name variable and print THIS
x = name_and_count_fav_foods(input_list)
print(x)







