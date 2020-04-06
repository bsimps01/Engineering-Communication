'''Given an array of integers, return indices of the two numbers such that they add up to a specific target.'''
'''You may assume that each input would have exactly one solution, and you may not use the same element twice.'''


'''Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].'''

#Considering the set up of the problem, I would assume that with the array given I want to be able to use a loop to help find each index and find values in the index until it equals to the stated target

#For every number that is found that does not match up to the added target I want to add them to a dictionary until the combination of the integers matches up

nums = [2, 7, 11, 15]
target = 9

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dictionary = {}
    if len(nums) <= 1: #Verifies that any solution that is less or equal to one will not give us the correct solution
        return False
    for i in range(len(nums)): #Goes through the range and length of the array
        if nums[i] in dictionary: #if the index in the array is in the dictionary
            return [dictionary[nums[i]], i] #return the number found in the array and append it to the dictionary
        else:
            dictionary[target - nums[i]] = i #takes the indice found in the array and subtracts it from the target in the dictionary

print(twoSum(nums, target)) #prints out the location of the indices that give the target value