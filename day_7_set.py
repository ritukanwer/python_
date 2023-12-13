# 1 Find the length of the set it_companies
it_companies = {'Facebook', 'google', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

# 2 Add 'Twitter' to it_companies
it_companies = {'Facebook', 'google', 'IBM', 'Oracle', 'Amazon'}
it_companies.add("twitter")
print(it_companies)


# 3 Insert multiple IT companies at once to the set it_companies
it_companies = {'Facebook', 'google', 'IBM', 'Oracle', 'Amazon'}
it_companies.update(['twitter','microsoft','apple'])
print(it_companies)


# 4 Remove one of the companies from the set it_companies
it_companies = {'Facebook', 'google', 'IBM', 'Oracle', 'Amazon'}
it_companies.remove('Facebook')
print(it_companies)


# 5 What is the difference between remove and discard
# remove :-  is used to remove a specified element from the set.
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print(my_set)

# dicard :- not present in the set
my_set = {1, 2, 3, 4, 5}
my_set.discard(10)
print(my_set)


# # level_2
# # (1) Join A and B
set_a = {1,2,3,4}
set_b = {4,5,6,7,9}
union_set = set_a.union(set_b)
print(union_set)
#
# # 2 Find A intersection B
set_a = {1,2,3,4}
set_b = {4,5,6,7,9}
intersection = set_a.intersection(set_b)
print(intersection)

# 3 # Is A subset of B
set_a = {1,2,3,4}
set_b = {4,5,6,7,9}
issubset = set_a.issubset(set_b)
print(issubset)
#

# 4 Are A and B disjoint sets
set_a = {1,2,3,4}
set_b = {4,5,6,7,9}
isdisjoint = set_a.isdisjoint(set_b)
print(isdisjoint)
#
# # # 5 Join A with B and B with A
set_a = {1,2,3,4}
set_b = {4,5,6,7,9}
a_with_b = set_a.union(set_b)
b_with_a = set_b.union(set_a)
print("a with b:", a_with_b)
print("b with a:", b_with_a)
#
#
#
# 6 Is A subset of B

set_a = {1,2,3,4}
set_b = {4,5,6,7,9}
is_subset_method = set_a.issubset(set_b)
print(is_subset_method)

# 7 What is the symmetric difference between A and B

set_a = {1,2,3,4}
set_b = {4,5,6,7,9}
symmetric_diff = set_a.symmetric_difference(set_b)
print(symmetric_diff)


# 8 Delete the sets completely

set_a = {1,2,3,4}
set_b = {4,5,6,7,9}
set_a.clear()
print(set_a)
del set_b

"""level_3"""
# 1 Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages_list = [18,19,20,13,24,15]
ages_set = set(ages_list)
# print(ages_set)
list_len = len(ages_list)
set_len = len(ages_set)
# print(set_len)
# print(list_len)
if set_len > list_len:
    print("set len is big")
elif set_len < list_len:
    print("list len is big")
else:
    print("both same")

