##a queue is a collection of entities that are main
# tained in a sequence and can be modified by the add
# ition of entities at one end of the sequence and the removal of entities from the o
# ther end of the sequence.

## queue operation:
# enqueue() > push()
# dequeue() > pop()

# applications of queues:
# 1.FIFO 
# ticket counter
# process request for cpu ram

class Queue:
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return self.items==[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

queue = Queue()

queue.isEmpty()

queue.enqueue("krish")
queue.enqueue("krsih2")
queue.enqueue("krsih2")

print(queue.items)
queue.dequeue()
print(queue.items)