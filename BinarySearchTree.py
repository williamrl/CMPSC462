# Develop a BinarySearchtree.py which can perform the following functions:
# • Insert node to a tree
# • Perform In-order traversal
# • Perform Pre-order traversal
# • Perform Post-order traversal
# • Find a node

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)
        else:
            print("Value is already present in the tree.")

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None
        
    def _find(self, data, current_node):
        if data < current_node.data and current_node.left:
            return self._find(data, current_node.left)
        elif data > current_node.data and current_node.right:
            return self._find(data, current_node.right)
        if data == current_node.data:
            return True
        
    def inorder_traversal(self):
        if self.root:
            self._inorder_traversal(self.root)
        else:
            return None
        
    def _inorder_traversal(self, current_node):
        if current_node:
            self._inorder_traversal(current_node.left)
            print(current_node.data)
            self._inorder_traversal(current_node.right)
            
    def preorder_traversal(self):
        if self.root:
            self._preorder_traversal(self.root)
        else:
            return None
        
    def _preorder_traversal(self, current_node):
        if current_node:
            print(current_node.data)
            self._preorder_traversal(current_node.left)
            self._preorder_traversal(current_node.right)

    def postorder_traversal(self):
        if self.root:
            self._postorder_traversal(self.root)
        else:
            return None
        
    def _postorder_traversal(self, current_node):
        if current_node:
            self._postorder_traversal(current_node.left)
            self._postorder_traversal(current_node.right)
            print(current_node.data)

bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
        
# Write a function to remove a node from a tree data structure? This function should consider all
# the three cases: case-1: remove a leaf node, case-2: remove a node with one child and case-3:
# remove a node with two children.
# Perform the time complexity for this function. Briefly explain?

def remove(self, data):
    if self.root:
        self.root = self._remove(data, self.root)
    else:
        return None
    
def _remove(self, data, current_node):
    if data < current_node.data and current_node.left:
        current_node.left = self._remove(data, current_node.left)
    elif data > current_node.data and current_node.right:
        current_node.right = self._remove(data, current_node.right)
    else:
        if current_node.left is None and current_node.right is None:
            del current_node
            return None
        if current_node.left is None:
            temp_node = current_node.right
            del current_node
            return temp_node
        elif current_node.right is None:
            temp_node = current_node.left
            del current_node
            return temp_node
        temp_node = self._min(current_node.right)
        current_node.data = temp_node.data
        current_node.right = self._remove(temp_node.data, current_node.right)
    return current_node

def _min(self, current_node):
    if current_node.left:
        return self._min(current_node.left)
    return current_node

# Time complexity: O(log n)
# Explanation: The time complexity of the remove function is O(log n) because the function will traverse the tree
# in a recursive manner until the node to be removed is found. The function will then perform the removal operation