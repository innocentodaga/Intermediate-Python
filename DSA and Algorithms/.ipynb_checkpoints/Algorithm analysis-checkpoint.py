# This helps to compare two programs doing the same thing
# and see which one uses fewer resources 

import time

def sum_of_n(n):
    start = time.time()
    the_sum = 0
    
    for i in range(1, n+1):
        the_sum = the_sum + i
        
    end = time.time()
    return the_sum, end-start
print("Sum is %d required %10.7f seconds" % sum_of_n(10))



def foo(tom):
    start = time.time()
    fred = 0
    
    for bill in range(1, tom+1):
        barney = bill
        fred = fred + barney
    
    end = time.time()
    return fred, end-start
print("Sum is %d required %10.7f seconds" % foo(10))

