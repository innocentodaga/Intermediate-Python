import Stack

def binary_convert(decNumber):
    s = Stack.Stack()
    
    while decNumber > 0:
        rem = decNumber % 2
        s.push(rem)
        decNumber = decNumber//2
        
    
    binary_string = ""
    
    while not s.is_empty():
        binary_string = binary_string + str(s.pop())
    return binary_string

print(binary_convert(55))
        