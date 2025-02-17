class Stack:
    def __init__(self, name):
        self.stack = []  # Initialize an empty list to represent the stack
        self.name = name  # Name of the stack for identification
    
    def push(self, item):
        self.stack.append(item)  # Add an item to the top of the stack
    
    def pop(self):
        if self.isEmpty():
            return None  # Return None if the stack is empty
        return self.stack.pop()  # Remove and return the top item of the stack
    
    def peek(self):
        if self.isEmpty():
            return None  # Return None if the stack is empty
        return self.stack[-1]  # Return the top item of the stack without removing it
    
    def isEmpty(self):
        return len(self.stack) == 0  # Check if the stack is empty
    
    def size(self):
        return len(self.stack)  # Return the number of items in the stack

class Queue:
    def __init__(self):
        self.queue = []  # Initialize an empty list to represent the queue
    
    def enqueue(self, item):
        self.queue.append(item)  # Add an item to the end of the queue
    
    def dequeue(self):
        if self.isEmpty():
            return None  # Return None if the queue is empty
        return self.queue.pop(0)  # Remove and return the front item of the queue
    
    def isEmpty(self):
        return len(self.queue) == 0  # Check if the queue is empty
    
    def size(self):
        return len(self.queue)  # Return the number of items in the queue

class StackTower:
    def __init__(self, n):
        self.n = n  # Number of disks
        self.rod1 = Stack("Rod 1")  # Initialize the first rod as a stack
        self.rod2 = Stack("Rod 2")  # Initialize the second rod as a stack
        self.rod3 = Stack("Rod 3")  # Initialize the third rod as a stack
        
        # Push disks onto the first rod in descending order
        for i in range(n, 0, -1):
            self.rod1.push(i)
    
    def moveDisk(self, n, source, destination, auxiliary):
        if n == 1:
            disk = source.pop()  # Move the disk from source to destination
            destination.push(disk)
            print(f"Move disk {disk} from {source.name} to {destination.name}")
        else:
            # Move n-1 disks from source to auxiliary, so they are out of the way
            self.moveDisk(n-1, source, auxiliary, destination)
            disk = source.pop()  # Move the nth disk from source to destination
            destination.push(disk)
            print(f"Move disk {disk} from {source.name} to {destination.name}")
            # Move the n-1 disks from auxiliary to destination
            self.moveDisk(n-1, auxiliary, destination, source)
    
    def solve(self):
        self.moveDisk(self.n, self.rod1, self.rod3, self.rod2)  # Solve the Tower of Hanoi problem
        
    def printRods(self):
        # Print the contents of all three rods
        print(f"{self.rod1.name}: {self.rod1.stack}")
        print(f"{self.rod2.name}: {self.rod2.stack}")
        print(f"{self.rod3.name}: {self.rod3.stack}")

# Create a StackTower object with 3 disks
tower = StackTower(3)
tower.printRods()  # Print the initial state of the rods
tower.solve()  # Solve the Tower of Hanoi problem
tower.printRods()  # Print the final state of the rods


print("-------------------------------------------------")
print("Simulating customers at a grocery store check-out")
# Simulation of customers at a grocery store check-out using a queue
import random

class GroceryStore:
    def __init__(self):
        self.checkout = Queue()  # Initialize a queue to represent the checkout line
        self.customers = 0  # Initialize the number of customers
    
    def addCustomer(self):
        self.customers += 1  # Increment the number of customers
        self.checkout.enqueue(self.customers)  # Add the customer to the checkout line
    
    def processCustomer(self):
        if self.checkout.isEmpty():
            print("Checkout line is empty")  # Print a message if the checkout line is empty
        else:
            customer = self.checkout.dequeue()  # Remove the first customer from the checkout line
            print(f"Processing customer {customer}")  # Print a message to process the customer

# Create a GroceryStore object
store = GroceryStore()

# Simulate customers arriving at the grocery store
for i in range(5):
    store.addCustomer()
    
# Process customers at the checkout
for i in range(5):
    store.processCustomer()