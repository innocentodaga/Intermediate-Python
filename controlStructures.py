# Algorithms require two important control structures 
# i.e iteration and selection


# while construct iterates a certain number of times while the condition is true
counter = 1
while counter <= 5:
    print("Hello, world")
    counter += 1


# for construct iterates through the items of a collection
for item in [1, 2, 3, 4, 5, 6 ]:
    print(item)


word_list = ["cat", "dog", "rabbit"]

letter_list = []

for a_word in word_list:
    for a_letter in a_word:
        letter_list.append(a_letter)

print(letter_list)


# Selection statements allow programmers to ask questions and then based on the result perform different actions.
import math

n = input("Enter the integer: ")
if int(n) < 0:
    print("Sorry, value is negative")
else:
    print(math.sqrt(int(n)))

# nesting the selection construct
score = 78
if score >= 90:
    print("A")
else:
    if score >= 80:
        print("B")
    else:
        if score >= 70:
            print("C")
        else:
            if score >= 60:
                print("D")
            else:
                print("F")

# computing the result regardless of the result of the selection construct
n = -4
if n < 0:
    n = abs(n)

print(math.sqrt(n))

# list comprehension, allows to create alist on some processing or selection criteria
# creating alist of the first 10 perfect squares
sq_list = []
for x in range(1, 11):
    sq_list.append(x * x)
print(sq_list)


# using list comprehension 
sq_list = [x * x for x in range(1, 11)]
print(sq_list)

# adding the selection construct to the above
sq_list = [x * x for x in range(1, 11) if x % 2 !=0]
print(sq_list)

# comprehension in string
print([ch.upper() for ch in "comprehension" if ch not in "aeiou"])

lisst = []
for ch in "comprehension":
    if ch not in "aeiou":
        lisst.append(ch.upper())
        
print(lisst)