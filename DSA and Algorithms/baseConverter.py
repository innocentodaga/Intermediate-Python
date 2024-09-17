import Stack

def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"
    
    stack = Stack.Stack()
    
    while dec_number > 0:
        rem = dec_number % base
        stack.push(rem)
        
        dec_number = dec_number // base
        
    
    newString = ""
    
    while not stack.is_empty():
        newString = newString + digits[stack.pop()]
    return newString

print(base_converter(26, 16))