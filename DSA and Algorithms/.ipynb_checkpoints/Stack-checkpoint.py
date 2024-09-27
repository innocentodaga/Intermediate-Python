# a stack is an ordered collection of items where the addition of new items and the removal of existing items always
# takes place at the same end
# It uses the priciple of LIFO (last in first out)

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)

if __name__ == "__main__":
    createStackObject = Stack()
    print(createStackObject.is_empty())
    createStackObject.push(4)
    createStackObject.push('dog')

    print(createStackObject.size())
    print(createStackObject.peek())
