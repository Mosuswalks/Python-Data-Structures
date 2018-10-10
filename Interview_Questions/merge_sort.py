# Bonus: For a given 2d Array, return a new sorted merged list from K sorted lists, each with size N.
#
#
# Time Complexity: O(N²)
# Space Complexity: O(1)

def merge_2d_sort(arr):
    flattened_array = [item for sublist in arr for item in sublist]
    flattened_array.sort()
    return flattened_array

# Bonus: 
#
#