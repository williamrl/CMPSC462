#stack is a LIFO data structure (Last in First out)
#queue is a FIFO data structure (First in First out)
#stacks ccan be minipulated with add delete peek size isEmpty and str
#queue can have elements appended non stop, but can only remove from the front

#stack implementation via class (ex. a stack of plates)
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
    
s1 = Stack() #creating a stack object
s1.push(1)
s1.push(2)
s1.push(3)
print(s1.stack) #prints [1, 2, 3]
s1.pop()
print(s1.stack) #prints [1, 2]

#queue implementation via class (ex. a line of people)
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        return self.queue.pop(0)
    def peek(self):
        return self.queue[0]
    def is_empty(self):
        return len(self.queue) == 0
    def size(self):
        return len(self.queue)
    
q1 = Queue() #creating a queue object
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3) 
print(q1.queue) #prints [1, 2, 3] 
q1.dequeue()
print(q1.queue) #prints [2, 3]