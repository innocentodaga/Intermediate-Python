# A set is an unordered collection of zero or more immutable Python data objects. Sets do not
# allow duplicates and are written as comma-delimited values enclosed in curly braces. The
# empty set is represented by set(). Sets are heterogeneous, and the collection can be assigned
# to a variable as below.

# they reurn the result starting with the bool datatype, followed by strings or integers 
set1 = {3, 5, "cat", 4.5, False}
print(set1)

set2 = {3, 4, 1, 'try'}

# union of two sets
union = set1 | set2
print(union)

# length of the sets
legth = len(union)
print(legth)

# intersection of two sets
inter = set1 & set2
print(inter)

# only elements in the first set
only = set1 - set2
print(only)


# adding elements in a set
set2.add("today")
print(set2)

# removing an element 
set2.remove(4)
print(set2)

# clear removes all the elements of the set
set2.clear()
print(set2)

