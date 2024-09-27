test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
},
    'output': 3
}

tests = []

# query occurs in the middle 
tests.append(test)
tests.append({
    'input':{
        'cards': [13, 11, 10, 7,  4, 3, 1, 0],
       'query': 1
    },
    'output': 6
})

# query for the first element
tests.append({
    'input':{
        'cards': [4, 2, 1, -1],
       'query': 1
    },
    'output': 4
})

# query is the last element
tests.append({
    'input':{
        'cards': [13, 11, 10, 7,  4, 3, 1, 0],
       'query': 0
    },
    'output': 7
})

# cards contains only one element
tests.append({
    'input':{
        'cards': [13],
       'query': 13
    },
    'output': 0
})

# cards does not contain query
tests.append({
    'input':{
        'cards': [13, 11, 10, 7,  4, 3, 1, 0],
       'query': 5
    },
    'output': -1
})

# card is empty
tests.append({
    'input':{
        'cards': [],
       'query': 88
    },
    'output': -1
})

# query repeats in cards
tests.append({
    'input':{
        'cards': [13, 11, 10, 10,  10, 3, 1, 0],
       'query': 10
    },
    'output': 2
})

# numbers in the list repeat other than the query
tests.append({
    'input':{
        'cards': [13, 13, 10, 7,  4, 13, 1, 0],
       'query': 10
    },
    'output': 2
})

print(tests)
