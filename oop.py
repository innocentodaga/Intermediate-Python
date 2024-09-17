# we define a new class by providing a name and a set of method definitions that are
# syntactically similar to function definitions.

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    
    def show(self):
        print(self.num, "/", self.den)
    
    # using the __str__() method to return data as string
    def __str__(self):
        return str(self.num) + ' / ' + str(self.den)
        
object = Fraction(3,5).show()
object2 = Fraction(5, 7)
print("I ate",object2, "of the pizza")
print(object)

# trying to add two fractions
f1 = Fraction(1,4)
f2 = Fraction(1, 2)

# this causes and error due to "+" not understanding the fraction operands
# print(f1 + f2)

# we use this instead
# (f1).__add__(f2)

# We can use this method by writinga standard arithmetic expression 
# involving fractions, assigning the result of the addition, and then printing our result.
class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
        
    def __add__(self, other_fraction):
        newNumber = self.num * other_fraction.den + self.den * other_fraction.num
        newDen = self.den * other_fraction.den
        
        return Fraction(newNumber, newDen)

# trying to add two fractions
f1 = Fraction(1, 4)
f2 = Fraction(1, 2)

f3 = f1 + f2
print(f3)

# finding the GCD
def gcd(m, n):
    while m % n != 0:
        oldM = m
        oldN = n
        
        m = oldN
        n = oldM
    return n
print(gcd(6, 2))