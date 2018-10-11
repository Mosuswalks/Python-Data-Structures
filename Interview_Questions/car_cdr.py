
# Bonus:
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
#
#

def cons(a, b) -> int:
    return lambda f: f(a,b)

def cdr(f): 
    return f(lambda a, b: a)

def car(f):
    return f(lambda a, b: b)


if __name__ == '__main__':
    print(cdr(cons(3,4)))