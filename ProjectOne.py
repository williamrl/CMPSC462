class Stack():
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
    
class Queue():
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
    
# Tower of Hanoi is a simple game which is usually used to demonstrate the use of recursion in
# algorithms. Implement the game using
# i) recursive functions and
# ii) iterative functions. We are going to solve the game using stacks and/or queues.

# The game consists of three rods and a number of disks of different sizes which can slide onto any rod.
# The game starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top.
# The objective of the game is to move the entire stack to another rod, obeying the following simple rules:
# i) Only one disk can be moved at a time.
# ii) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack
#     i.e. a disk can only be moved if it is the uppermost disk on a stack.
# iii) No disk may be placed on top of a smaller disk.

# The game can be played with any number of disks, although many toy versions have around 7 to 9 of them.
# The minimum number of moves required to solve a Tower of Hanoi puzzle is 2^n - 1, where n is the number of disks.

# The recursive solution is as follows:
# i) Move n-1 disks from the source rod to the auxiliary rod.
# ii) Move the nth disk from the source rod to the destination rod.
# iii) Move the n-1 disks from the auxiliary rod to the destination rod.
# The iterative solution is as follows:
# i) If n is even, interchange destination rod and auxiliary rod.
# ii) for i = 1 to number of moves:
#     a) if i%3 == 1, then make legal move between source and destination rods.
#     b) if i%3 == 2, then make legal move between source and auxiliary rods.
#     c) if i%3 == 0, then make legal move between auxiliary and destination rods.

# Implement the game using the recursive solution.
def tower_of_hanoi_recursive(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi_recursive(n-1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi_recursive(n-1, auxiliary, destination, source)