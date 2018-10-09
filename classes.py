# This file is a simple implementation of a Fraction class i made to help refresh my understanding of Python OOP #

class Fraction:
    def __init__(self, top, bottom):
       self.num = top
       self.den= bottom

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

if __name__ == '__main__':
    myFrac = Fraction(1,4)
    print(f'I ate {myFrac} of the pizza we ordered last night.')