# A list is a collection of items where each item holds a relative position with respect to the
# others. The list is a powerful, yet simple, collection mechanism that
# provides the programmer with a wide variety of operations

# The building block of the linked list is the node
# Each node object must hold at least two pieces of information First, the node must contain the list item
# itself, called the data field of the node, The second is the reference to the next node.

class Node:
    # creates an initial node
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
    
    # returns the data contained in the node
    def get_data(self):
        return self.data
    
    # returns the address to the next data item
    def get_next(self):
        return self.next
    
    # set / define the data item
    def set_data(self, new_data):
        self.data = new_data
    
    # set / define the address to the next item
    def set_next(self, new_next):
        self.next = new_next
    

# class to define the linked list
class UnorderedList:
    # creates an initial list
    def __init__(self):
        self.head = None

    # checks whether the list is empty
    def is_empty(self):
        self.head == None
    
    # adding item to the unordered list
    def add(self, new_item):
        # creates a new node 
        new_Node = Node(new_item)
        # set the address to the next node which is the previous node that was the head
        new_Node.set_next(self.head)
        # Set the head of the list to the newly createed node
        self.head = new_Node
    
    # getting the size of the linked list   
    def size(self):
        # Set the head as the current node and initialize the count to 0
        current = self.head
        count = 0
        
        # continue loop through the list if the head is not none
        while current != None:
            # increase the count by one each time we loop through the list
            count = count + 1
            # we reassign our current to the next address of the node each time we loop
            current = current.get_next()
        # we return the count after traversing all elements in the list 
        return count   
    
    # a method that returns the item we are searching for
    def search(self, item):
        # we start from the head 
        current = self.head
        # we initialize the found variable to False, since the head node is always a none
        found = False
        
        # we continue traversing the list if the current node is not none and the item is found
        while current !=None and not found:
            # check if the current data item is the same as the item we are searching for 
            if current.get_data() == item:
                # if the its the same then the found is initialized to true since the data is found 
                found = True
            # if the condition is false, the we continue to traverse the list by setting the current item to the next address to the item 
            else: 
                current = current.get_next()
        # we return the result found afte the loop is done  
        return found
    
    # method to remove an item
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        
        # continue as long as the condition is True
        while not found:
            # checks whether the current item is the same as the item entered
            if current.get_data() == item:
                found = True
            else:
                # assigns the previous node item as the current
                previous = current
                
                # we set the current to the next 
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())       
        
        
myList = UnorderedList()
myList.add(44)
myList.add(67)
myList.add("gg")
myList.remove(44)

print(myList.size())
