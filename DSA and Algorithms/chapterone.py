listi = [1, 3, True, 6.5]
print(list)

my_list = [1, 3, True, 6.5]
print(my_list)

for i in my_list:
    print(i)

for i in my_list:
    if i == 3:
        print(i)

for i in my_list[:2]:
    print(i)  

my_list = [0] * 6
print(my_list)

my_list.insert(2, 5)
print(my_list)

# deletes the item
del my_list[4]
print(my_list)

# returns the index of the item
ind = my_list.index(5)
print(ind)

# counts the occurence of the item
count = my_list.count(0)
print(count)

listi  = [1, 2, 3, 4]
A = [my_list]*3
print(A)

# invoking  method
invoking_amethod = (54).__add__(21)
print(invoking_amethod)

#using the function range
rangee = range(10)
print(rangee)

listRange = list(range(1, 10))
print(listRange)

# Strings
string = "Tyson"

print(string)

# indexing string
print(string[2])

# Slicing the string
print(string[1:4])

# spliting string at a certain character  returns a list of the splitted characters
print(string.split("s"))

# changing all characters to uppercase
print(string.upper())


# changing all characters to lowercase
print(string.lower())

























