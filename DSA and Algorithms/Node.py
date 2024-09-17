class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, item):
        self.data = item
    
    def set_next(self, next_data):
        self.next = next_data

class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
       return self.head == None
    
    def add(self, item):
        current = self.head 
        
        
        