

# 1 Create an empty dictionary called dog
dog = {}
print(dog)

# 2 Add name, color, breed, legs, age to the dog dictionary
dog = {
    "name": 'huchu',
    'color': 'block_&_white',
    'breed': "lebra",
    'age' : 8
}
print(dog)



# 3 Create a student dictionary and add first_name, last_name, gender, age, marital
# status, skills, country, city and address as keys for the dictionary

student = {}
student["first_name"] = "ritu"
student["last_name"] = "naruka"
student["gender"] = "female"
student["age"] = 18
student["marital_status"] = "no"
student["skills"] = ["Programming", "Communication"]
student["country"] = "india"
student["city"] = "jaipur"
student["address"] = "chandma_kalan"

print(student)



# 4Get the length of the student dictionary
student = {'first_name': 'ritu',
           'last_name': 'naruka',
           'gender': 'female',
           'age': 18,
           'marital_status': 'no',
           'skills': ['Programming', 'Communication'],
           'country': 'india',
           'city': 'jaipur',
           'address': 'chandma_kalna'}
print(len(student))

# 5 Get the value of skills and check the data type, it should be a list
student = {'first_name': 'ritu',
           'last_name': 'naruka',
           'gender': 'female',
           'age': 18,
           'marital_status': 'no',
           'skills': ['Programming', 'Communication'],
           'country': 'india',
           'city': 'jaipur',
           'address': 'chandma_kalna'}

skills = student.get("skills")
print(skills)
print(type(skills))

# 6 Modify the skills values by adding one or two skills
student = {'first_name': 'ritu',
           'last_name': 'naruka',
           'gender': 'female',
           'age': 18,
           'marital_status': 'no',
           'skills': ['Programming', 'Communication'],
           'country': 'india',
           'city': 'jaipur',
           'address': 'chandma_kalna'}

more_skills = ["coding","cooking","dancing"]
student["skills"].extend(more_skills)
print(student)


#7 Get the dictionary keys as a list
student = {'first_name': 'ritu',
           'last_name': 'naruka',
           'gender': 'female',
           'age': 18,
           'marital_status': 'no',
           'skills': ['Programming', 'Communication'],
           'country': 'india',
           'city': 'jaipur',
           'address': 'chandma_kalna'}
def keys(student):
    keys_list = []
    for key in student.keys():
        keys_list.append(key)
    return keys_list
print(keys(student))


# 8 Get the dictionary values as a list
student = {'first_name': 'ritu',
           'last_name': 'naruka',
           'gender': 'female',
           'age': 18,
           'marital_status': 'no',
           'skills': ['Programming', 'Communication'],
           'country': 'india',
           'city': 'jaipur',
           'address': 'chandma_kalna'}
def values(student):
    value_list = []
    for value in student.values():
        value_list.append(value)
    return value_list
print(values(student))


# 9 Change the dictionary to a list of tuples using items() method

student = {'first_name': 'ritu',
           'last_name': 'naruka',
           'gender': 'female',
           'age': 18,
           'marital_status': 'no',
           'skills': ['Programming', 'Communication'],
           'country': 'india',
           'city': 'jaipur',
           'address': 'chandma_kalna'}
print(student.items())

# 10 Delete one of the items in the dictionary
student = {'first_name': 'ritu',
           'last_name': 'naruka',
           'gender': 'female',
           'age': 18,
           'marital_status': 'no',
           'skills': ['Programming', 'Communication'],
           'country': 'india',
           'city': 'jaipur',
           'address': 'chandma_kalna'}
student.pop('first_name')
print(student)


# 11 Delete one of the dictionaries
student = {'first_name': 'ritu',
           'last_name': 'naruka',
           'gender': 'female',
           'age': 18,
           'marital_status': 'no',
           'skills': ['Programming', 'Communication'],
           'country': 'india',
           'city': 'jaipur',
           'address': 'chandma_kalna'}

student.clear()
print(student)


