"""
its follow fifo - first in first out

enqueue -  insertion at tail 

dequeue -  deletion at front 


"""

# IMPLEMENTATION OF QUEUE USING LINKED LIST

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self,value):
        node = Node(value)
        if self.rear == None:
            self.front = node
            self.rear = self.front
        
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front==None:
            return "Empty"
        else:
            self.front = self.front.next
        
    def traverse(self):
        temp = self.front
        while(temp!=None):
            print(temp.data,end=" ")
            temp = temp.next
    def isempty(self):
        return self.front == None
    
    def size(self):
        if self.front == None:
            return 0
        else:
            n=0
            temp = self.front
            while(temp!=None):
                n+=1
                temp = temp.next
            return n
    
    def frontItem(self):
        return self.front.data
    
    def rearItem(self):
        return self.rear.data

q = Queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.traverse()

q.dequeue()
print()
q.traverse()
print("\n",q.isempty())

print(q.size())
print()

print(q.frontItem())
print(q.rearItem())