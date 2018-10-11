
# Q.1.2: 
# 
# Given two strings, write a method to decide if one is a permutation of the other.
#
# We can start by checking the lengths of both strings. 
# If either string is of a different length, then we know the strings are not permutations of eachother.
# Finally, we compare the sorted elements of each string and return the result.
#
#                       *NOTE*
#   Python's built in sort method is a spin off of TimSort.
#   It's essentially no better or worse than merge sort in terms of Time Complexity.
#     
# Time Complexity: O(n log n) 
# Space Complexity: O(N) (Worst Case)

def check_permutation(string_1, string_2):
    if len(string_1) != len(string_2):
        return False
    return sorted(string_1) == sorted(string_2)


    


        
