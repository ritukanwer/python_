# question_1

# write a python program that takes list of names asinput and return a dictionary here the keys are name and the values are
# length of the corresponding names. the program should ignore any names that have a length less than 4 charcters.


name = ["john", "alice", "sam", "sarah"]

def get_name_length(name):
    names_length = {}
    for i in name:
        if len(i) >= 4:
            names_length[i] = len(i)

    return names_length

result = get_name_length(name)
print(result)



# question_2
# how can i add a key value pair to an exsting dictionary.

my_dict = { "A" : 1,"B" : 2}
my_dict["C"] = 3
print(my_dict)



# question_3
# add two dictionaries
dict_1 = { "a":1, "b":2}
dict_2 = { "c":3,"d":4}
dict_1.update(dict_2)
print(dict_1)




# question_4
# convert dictionary value in list.
dict_1 = { "a":1, "b":2, "c":3}
my_list = list(my_dict.keys())
list = list(my_dict.values())
print(my_list)
print(list)




# question_5
# how i can remove a key-value pair from a dictionary?
my_dict = {"a":1,"b":2,"c":3,"d":4}
del my_dict["b"]
print(my_dict)













