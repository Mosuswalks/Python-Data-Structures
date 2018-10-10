import sys
sys.path.append('../Python-Data-Structures')
from stack import Stack
# Bonus: 
# Write an algorithm that will read a string of parentheses from
# left to right and decide whether the symbols are balanced.
#
#

def valid_parentheses(string: str) -> bool:
    s = Stack()
    balanced = True
    index = 0

    while index < len(string) and balanced:
        if string[index] == '(':
            s.push(string[index])
        elif s.isEmpty():
            balanced = False
        else:
            s.pop()
        index += 1
    if balanced and s.isEmpty():
        return True
    return False

val