import Deque

def pal_checker(string):
    newDeque = Deque.Deque()
    
    for char in string:
        newDeque.add_rear(char)
        
    Equal = True    
    
    while newDeque.size() > 1 and Equal:
        first =  newDeque.remove_front()
        last = newDeque.remove_rear()

        if first != last:
            Equal = False
        return Equal

print(pal_checker("hjh"))