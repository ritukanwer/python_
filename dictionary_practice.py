# Create an empty dictionary called dog
dictionary = {}
print("empty dictionary", dictionary)
#first i make a empty dictionary. then i print a "empty sictonary" and i use comma and run this.
# then my answer empty dictionary{} in came.
#


dog = {
    'name':'tomy',
    'ages': 8,
    'breed':'german',
    'color':'black'
}
print(dog)
# fir i make a dog name variable then i enter dictionary acording to question.
# then i print(dog)





student = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'gender':'male',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(student)





# Get the length of the student dictionary
students =  {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'gender':'male',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
print(len(students))



student = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
print(type(student))
# Get the value of skills and check the data type, it should be a list
#first i make a student name dictionary. then i print type of values .
# then my answer is dictionary



student = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
        }
}

student['skills'].append('c+')
student['skills'].append('HTML')
print(student)
# Modify the skills values by adding one or two skills
# first i make a students name dictionary then i  add two values  in skills.
# so i did student ['skills'].append('c+' and 'HTML') then  i print this and result
# is ['JavaScript', 'React', 'Node', 'MongoDB', 'Python','c+','HTML']

student = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'gender': 'male',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
keylist = list(student.keys())
print(keylist)
# Get the dictionary keys as a list
# first i make students name dictionary then question ask students key
# then keylist = list(studen.key) ten i print this .


student = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'gender': 'male',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

print(list(student.values()))
# Get the dictionary values as a list

# first i make a student name dictionary then then i entry dictionary detailsthen i print
# list students values .


















student = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
list = list(student.items())
print(list)






student = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'gender': 'male',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
student.pop('last_name')
print(student)





student = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'gender': 'male',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
del student['skills']
print(student)





