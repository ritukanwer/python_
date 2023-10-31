# question 1
dictionary = {
    5: 'e',
    4: 'd',
    3: 'c',
    2: 'b',
    1: 'a',
}
sorted_dictionary = {}
for key,value in sorted(dictionary.items()):
    sorted_dictionary[key]=value
print(sorted_dictionary)

#2
def add_key(dict_1,dict_2):
    x = dict_1.copy()
    x.update(dict_2)
    return x
print(add_key(dict_1 = {0:10,1:20},dict_2 = {2:30}))


# # 3
# def add_key(dict_1,dict_2,dict_3):
#     x =( dict_1,dict_2.copy())
#     x.update(dict_3)
#     return x
# print(add_key(dict_1={1:10, 2:20}, dict_2={3:30, 4:40}, dict_3={5:50,6:60}))

dict_0 = {'a':1, 'b':2, 'c':3}
dict_1 = {'a':1, 'd':2, 'c':'foo'}
dict_2 = {'e':57,'c':3}

# super_dict = {'a':[1], 'b':[2], 'c':[3,'foo'], 'd':[2], 'e':[57]}
# I wrote the following code:
def add_three_dic(dictionary):
    dictionary = {}
    for d in dict_0:
        for k, v in d.items():
            if dictionary.get(k) is None:
                dictionary[k] = []
            if v not in dictionary.get(k):
                dictionary[k].append(v)

print(add_three_dic(dictionary))










