#A graph G is a set V(G) of vertices and a set E(G) of edges which are pairs of vertices.

v = {'a', 'b', 'c', 'd', 'e'}

e = {('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'a')}

# a path of length k is a sequence v0, v1,...,vk of vertices such that (vi, vi+1) for i = 0, 1,..., k-1 
# are edges of G.

# strong and weak connectivity; A directed graph is a strongly connected if every two vertices are reachable
# from each other. A directed graph is weakly connected if the underlying undirected graph is connected.

# Traversals: Breadth-first search (BFS) behaves much like a level-order traversal
# and Depth-first search (DFS) behaves much like a pre-order traversal.

# take a graph where s has a b and c as neighbors, then all the have d as a neighbor.
# Breath-first search: uses queue

def bfs(graph, start):
    visited = set() # set of visited nodes
    queue = [start] # queue of nodes to visit
    while queue:
        node = queue.pop(0) # get the first node in the queue
        if node not in visited:
            visited.add(node) # mark the node as visited
            neighbors = graph[node] # get the neighbors of the node
            for neighbor in neighbors:
                queue.append(neighbor) # add the neighbors to the queue
    return visited

graph = {
    's': ['a', 'b', 'c'],
    'a': ['d'],
    'b': ['d'],
    'c': ['d'],
    'd': []
}

print(bfs(graph, 's'))
# Output: {'s', 'a', 'b', 'c', 'd'}

# Depth-first search: uses stack
# what does it look like out of code?
# start at the root node, visit the node, then recursively visit the children of the node.
# if the node has no children, return.
# if the node has children, recursively visit each child.

def dfs(graph, start):
    visited = set() # set of visited nodes
    stack = [start] # stack of nodes to visit
    while stack:
        node = stack.pop() # get the last node in the stack
        if node not in visited:
            visited.add(node) # mark the node as visited
            neighbors = graph[node] # get the neighbors of the node
            for neighbor in neighbors:
                stack.append(neighbor) # add the neighbors to the stack
    return visited

print(dfs(graph, 's'))
# Output: {'s', 'a', 'd', 'b', 'c'}


# DFS
# 1, 2, 3, 4, 5, 6, 7
# push 1, push 2, push 4, push 3, push 5, push 6, push 7

# spanning tree: a subset of graph G with minimum edges. n-1 edhes n->number of nodes
# complete graph has n-1 edges, -> n^n-2 possibility of spanning tree
# remove one edhe -> disconnected
# add one edge -> cycle

# example code:
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
    
    def dfs(self, start):
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                if node in self.graph:
                    for neighbor in self.graph[node]:
                        stack.append(neighbor)
        return visited
    
    def bfs(self, start):
        visited = set()
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                if node in self.graph:
                    for neighbor in self.graph[node]:
                        queue.append(neighbor)
        return visited
    
    def __str__(self):
        return str(self.graph)
    
g = Graph()
g.add_edge('s', 'a')

g.add_edge('s', 'b')
g.add_edge('s', 'c')
g.add_edge('a', 'd')
g.add_edge('b', 'd')
g.add_edge('c', 'd')
print(g)
print(g.dfs('s'))
print(g.bfs('s'))
# Output: {'s': ['a', 'b', 'c'], 'a': ['d'], 'b': ['d'], 'c': ['d'], 'd': []}
# Output: {'s', 'a', 'd', 'b', 'c'}
# Output: {'s', 'a', 'b', 'c', 'd'}

# Kruskal's algorithm: find the minimum spanning tree of a graph
# 1. Sort the edges in increasing order of their weights.
# 2. Add the edge with the smallest weight to the tree.
# 3. If adding the edge creates a cycle, discard it.
# 4. Repeat steps 2 and 3 until n-1 edges are added.

# Prim's algorithm: find the minimum spanning tree of a graph
# 1. Start with an arbitrary vertex as the root of the tree.
# 2. Add the edge with the smallest weight that connects a vertex in the tree to a vertex outside the tree.
# 3. Repeat step 2 until n-1 edges are added.

# Dijkstra's algorithm: find the shortest path from a source vertex to all other vertices in a graph
# 1. Initialize the distance to the source vertex as 0 and all other distances as infinity.
# 2. Relax the edges of the graph in a greedy manner.
# 3. Repeat step 2 until all vertices are visited.

# Bellman-Ford algorithm: find the shortest path from a source vertex to all other vertices in a graph
# 1. Initialize the distance to the source vertex as 0 and all other distances as infinity.
# 2. Relax the edges of the graph n-1 times.
# 3. Check for negative cycles.
