
# Question 1.5
# There are three types of edits that can be performed on strings: Insert a character, replace a character and remove a character.
# Given two strings, write a function to check if they are one edit away.
#
# Time Complexity: O(N²)
# Space Complexity: O(1)

def one_away(first_string: str, second_string: str) -> bool:
    string_difference = [x in first_string for x in second_string]
    if sum(string_difference) == len(second_string) - 1:
        return True
    return False

print(one_away('pake', 'padd'))