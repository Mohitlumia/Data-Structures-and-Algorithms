from collections import defaultdict

class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        """
        BFS in graph has linear time and linear space complexity.
        
        Time Complexity:    O(v + e), where "v" is the number of vertices and "e" is the number of edges in the graph.
        Space Complexity:   O(v)
        """
        visited = set()
        queue = [start]
        traversal = []

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                traversal.append(vertex)
                visited.add(vertex)
                queue.extend([neighbor for neighbor in self.graph[vertex] if neighbor not in visited])

        return traversal

# Graph:
#
#     0 -----> 1
#     ^ \     / |
#     |   \  /  |
#     |    \/   |
#     |    /\   v
#     |   /  \> 2 -----> 3
#     |  /         ^
#      \<----------|

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("BFS Traversal:", g.bfs(2))
