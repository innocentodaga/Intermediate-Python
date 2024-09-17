# Question: 
# Alice has some cards with numbers written on them, 
# She arranges the cards in decreasing order, 
# and lays them out face down in a sequence on a table.
# She challenges Bob to pick out the card containing
# a given number by turning over as few cards as possible. 
# Write a function to help Bob locate the card

#----------------Solution to the above problem-------------------------#

#=====1. State the problem clearly, Identify the inputs and outputs formats
# i) PROBLEM :- write a program to find the position of a given number in a list of numbers arranged
# in descending order, we need to minimize the number of times we access elements from the list
# ii) INPUTS :- cards-- list of sorted descending numbers e.g [13,12,11,10,9,8,7,6,5,4,3,2,1,0]
# query -- the number whose position is to be determined
# iii) OUTPUTS :- position - the index of the query in the list e.g 4

# Possible variations to take into consideration---What if...
# a) The number query occurs somewhere in the middle of the list cards
# b) query is the first element in cards
# c) query is the last element in cards
# d) The list cards contains just one element, which is query
# e) The list cards does not contain number query
# f) The list cards is empty
# g) The list cards contains repeating numbers?
# h) The number query occurs at more than one position in cards

# a function that takes on inputs (cards and query) then locates the card or the index of a given card
def locate_card(cards, query):
    pass

#===== 2. Come up with some example inputs and outputs, Try to cover all edge cases
# Before going to far, start with some example inputs and outputs which we can use later to test out problem
cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3

result = locate_card(cards, query)
print(result)

print(result==output)

## Go check to the testcases.py for more

# 3. Come up with a correct solution for the problem, State it in plain English.
# Our first goal is to come up with a correct solution which may not necessarily be the most efficient soln
# The simplest soln involves checking all possible answers i.e brute force solution

# i) Create a variable position with value 0
# ii) Check whether the number at index position in card equals query
# iii) If it does, position the answer and can be returned from the function
# iv) if not,increment the value of position by 1 and repeat steps 2 to 5 till we reach the last position 
# v) if the number was not found, return -1

# 4. Implement the solution and test it using example inputs, Fix bugs if any.

# 5. Analyze the algorithm's complexity and identify inefficiency. Repeat steps 3 to 6.