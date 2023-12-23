

# 1 Create an empty tuple
tuple = ()
print(tuple)


# 2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
family_tuple = ('ritu','kuldeep','bittu','gunnu','lucky','sheru')
print(family_tuple)

# 3 Join brothers and sisters tuples and assign it to siblings
sister_tuple = ("ritu","bittu")
bro_tuple = ("kuldeep","lucky")
siblings = sister_tuple + bro_tuple
print(siblings)

# 4 How many siblings do you have?
print(len(siblings))


# 5Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = ('ritu_naruka','kuldeep_naruka')
father = "ram_singh"
mother = "kiran_rathore"
family_members = siblings + (mother,father)
print(family_members)


"""EXERCISE_LEVEL_2"""
# 1 Unpack siblings and parents from family_members
family_members = ('ritu_naruka', 'kuldeep_naruka', 'ram_singh', 'kiran kanwar')

# Unpack siblings and parents
siblings = family_members[:2]
parents = family_members[2:]

print("Siblings:", siblings)
print("Parents:", parents)



# 2Create fruits, vegetables and animal products tuples. Join the three tuples and
# assign it to a variable called food_stuff_tp.
fruits = ("apple","banana","orange")
vegetables = ("patota","tomato","chilly")
animal = ("cow","buffalo","dog")

food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)


# 3 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_tp = ('apple', 'banana', 'orange', 'patota', 'tomato', 'chilly', 'cow', 'buffalo', 'dog')
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# 4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_stuff_tp = ('apple', 'banana', 'orange', 'patota', 'tomato', 'chilly', 'cow', 'buffalo', 'dog')


middle_index = len(food_stuff_tp) // 2
if len(food_stuff_tp) % 2 != 0 :
    middle_items = food_stuff_tp[middle_index]
    print(middle_items)
else:
    print("no-one")

food_stuff_lt = ['apple', 'banana', 'orange', 'patota', 'tomato', 'chilly', 'cow', 'buffalo', 'dog']
middle_index = len(food_stuff_tp) // 2
if len(food_stuff_lt) % 2 != 0:
    midlle_items = food_stuff_lt[middle_index]
    print(middle_items)
else:
    print("no_one")


# 5Slice out the first three items and the last three items from food_staff_lt list
food_stff_lt = ['apple', 'banana', 'orange', 'patota', 'tomato', 'chilly', 'cow', 'buffalo', 'dog']
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(first_three)
print(last_three)

# 6 Delete the food_staff_tp tuple completely
food_stuff_tp = ('apple', 'banana', 'orange', 'patota', 'tomato', 'chilly', 'cow', 'buffalo', 'dog')
del food_stuff_tp



# 7check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
#
# Check if 'Iceland' is a nordic country
#
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

is_estonia_nordic = 'Estonia' in nordic_countries
print(is_estonia_nordic)
is_iceland_nordic = 'Iceland' in nordic_countries
print(is_iceland_nordic)



