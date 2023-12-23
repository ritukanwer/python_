
nums = [2,5,6,4,5]
target = 6
def sum_two_elements(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]+nums[j] == target:


                return[i,j]