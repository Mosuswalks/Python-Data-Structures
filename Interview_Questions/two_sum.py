
# Bonus:
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#

def two_sum(array, target: int) -> []:
    temp = {}
    for x in range(len(array)):
        if array[x] not in temp:
            temp[array[x]] = x
        if target - array[x] in temp.keys() and temp[target - array[x]] != x:
            return [temp[target - array[x]], x]
    return False

