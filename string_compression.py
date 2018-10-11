from itertools import groupby
# Question 1.6
# Implement a method to perform basic string compression usng the counts of repeated characters.
# 
#
#

def string_compress(string: str) -> str:
    return ''.join('%s%s' % (char, sum(1 for char in group)) for char, group in groupby(string)).replace('1', '')




    

print(string_compress('aabbcccddddd'))
        
