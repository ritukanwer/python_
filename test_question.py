


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



def name_and_count_fav_foods(input_list):
   answer = []
   for i in input_list:

      name = i['name']
      num_favorite_foods = len(i['favorite_foods'])
      answer.append({'name':name,'num_favorite_foods':num_favorite_foods})


   return answer
# print(input_list)
x = name_and_count_fav_foods(input_list)
print(x)







