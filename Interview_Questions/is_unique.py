# Q.1.1: Implement an algorithm to determine if a string has all unique characters. 
#
# First let's create a Set(temp) object and add each character of the string to the Set.
# Since Python Sets don't allow for duplicates, we can simply compare the lengths and return the results.
#
# Time Complexity = O(N)
# Space Complexity = O(N)

def is_unique(string: str) -> bool:
    temp = set()
    for x in range(len(string)):
        temp.add(string[x])
    return len(temp) == len(string)


# Bonus: What if you cannot use additional Data Structures?
# 
# Loop through our string and compare each character to our character at x index. 
# If any character matches then we know that the string is not unique and infact does have repeat characters.
#
# Time Complexity = O(N²)
# Space Complexity = O(1)

def is_unique_chars(string: str) -> bool:
    for x in range(len(string)):
        for y in range(x + 1,len(string)):
            if string[x] == string[y]:
                return False
    return True


