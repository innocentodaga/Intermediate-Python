import Queue

def hot_potato(nameList, num):
    queue = Queue.Queue()
    for name in nameList:
        queue.enqueue(name)
        
    while queue.size() > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())
        
        queue.dequeue()
    return queue.dequeue()

newObject = hot_potato(['Bill','Sharon', 'Susan','Jane', 'Kent', 'Tom'], 7)
print(newObject)

