import Deque

def pal_checker(a_string):
    char_deque = Deque.Deque()
    
    for char in a_string:
        char_deque.add_rear(char)
    
    still_equal = True
    
    while char_deque.size() > 1 and still_equal:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        
        if first != last:
            still_equal = False
        
        return still_equal
print(pal_checker("fsafafa"))
print(pal_checker('radar'))