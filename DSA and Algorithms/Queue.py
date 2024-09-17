# The most recently added item in the queue must wait at the end of the collection. The item that
# has been in the collection the longest is at the front. This ordering principle is sometimes called
# FIFO, first-in first-out. It is also known as “first-come first-served.”
class Queue():
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def show(self):
        return self.items
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self)-1]
  
if __name__ == "__mani__":
    newQueue = Queue()
    newQueue.enqueue(44)
    newQueue.enqueue("me")
    newQueue.enqueue(5)

    print(newQueue.show())

    newQueue.dequeue()
    print(newQueue.show())

