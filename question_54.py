
# Given the code below, use the correct code on line 3 in order to return a slice made of [30, 'Python', 'Java'] from
# my_list based on negative index
#
#
# my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
#
# my_slice = my_list[-4:-1]
#
# print(my_slice)

# program ka flow
list = ["ritu_naruka","risa","bitu","risa_naruka","lucky"]
def check_srname(list):

    check = 'naruka'

    res = []
    for i in list:
        if  "naruka" in i:
            print('yes')
            res.append(i)
    return res
print(check_srname(list))

























