# There are two types of errors that typicaly occur when writting programs.
# The first one is syntax  error simply means that the programmer has made a mistake in the structure
# of a statement eg forgeting the colon
# The other is logic error that denotes a situation where the program executes but gives the wrong result. this 
# can be due to an error in the underlying algorithm

# Exception errors are runtime errors such as trying dividing by zero or trying to access a list
# where the index of the item is ourside the bounds of the list. 
import math

number = int(input("Please enter an integer: "))
print(math.sqrt(number))

# The above program throws and error if the negative value is input
# We can solve that by using except block
number = int(input("Please enter an integer: "))

try:
    print(math.sqrt(number))

except:
    print("Bad value for the square root")
    print("Using absolute value instead")
    print(math.sqrt(abs(number)))

# using raise to throw a runtime error that the programmer just created
number = int(input("Please enter an integer: "))
if number< 0:
    raise RuntimeError("You can't use a negative number")
else:
    print(math.sqrt(number))

