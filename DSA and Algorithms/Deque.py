# The deque abstract data type is defined by the following structure and operations. A deque is
# structured, as described above, as an ordered collection of items where items are added and
# removed from either end, either front or rear

class Deque():
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items ==[]

    def add_rear(self, item):
        self.items.insert(0, item)
    
    def add_front(self, item):
        self.items.insert(len(self.items), item)
    
    def size(self):
        return len(self.items)
    
    def remove_front(self):
        return self.items.pop(len(self.items)-1)

    def remove_rear(self):
        return self.items.pop(0)
    
    def show(self):
        return self.items
    
if __name__ == "__main__":
    newDeque = Deque()
    newDeque.add_front(7)
    newDeque.add_front("cat")
    newDeque.add_front(5)
    newDeque.add_rear(67)

    newDeque.remove_front()


    print(newDeque.show())
