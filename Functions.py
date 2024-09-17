# A function definition requires a name, a group of
# parameters, and a body. It may also explicitly return a value. 
# For example, the simple function defined below returns the 
# square of the value you pass into it.

def Square(n):
    return n ** 2

ObjectCreation = Square(6)
print(ObjectCreation)

squareSquare = Square(Square(5))
print(squareSquare)

# Newton's Method to guess the square root of a number
def square_root(n):
    root = n/2
    for k in range(20):
        root = (1/2)*(root + (n/root))
    return root

createOject = square_root(9)
print(createOject)