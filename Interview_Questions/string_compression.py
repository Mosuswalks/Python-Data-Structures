from itertools import groupby
# Question 1.6
# Implement a method to perform basic string compression usng the counts of repeated characters.
# 
# (1) Grouping by chars with groupby(string)

# (2) Counting length of group with sum(1 for _ in group) (because no len on group is possible)

# (3) Joining into proper format

# (4) Removing 1 chars for single items
#

def string_compress(string: str) -> str:
    return ''.join('%s%s' % (char, sum(1 for char in group)) for char, group in groupby(string)).replace('1', '')



        
