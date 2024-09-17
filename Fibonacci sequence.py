# The Fibonacci sequece is a sequence of numbers such that any number, 
# except for the first and second is the sum of the previous two:
#  0, 1, 1, 2, 3, 5, 8, 13, 21...

# formular : fib(n) = fib(n - 1) + fib(n - 2)

def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)

if __name__ == "__main__":
    print(fib1(5))

