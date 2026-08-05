"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
#graph is 1 indexed
#input is node 1
#index 0 represents node 1
#undirected graph
class Solution:

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        #visited_nodes = set()
        #can combine curr and res 

        #curr = {}
        #res = Node(node.val, neighbors) 
        old_to_new = {}

        if not node:
            return None

        def DFS(node: Optional['Node']):
            if not node:
                return None
            if node in old_to_new:
                return old_to_new[node]
            copy = Node(node.val)
            old_to_new[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(DFS(n))
            
            return copy
        #either bfs or dfs

        return DFS(node)