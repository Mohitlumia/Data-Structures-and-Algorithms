class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

def dfs(graph, start_node):
    visited = set()

    def dfs_recursive(node):
        visited.add(node)
        print(node, end=' ')

        for neighbor in graph.adj_list[node]:
            if neighbor not in visited:
                dfs_recursive(neighbor)

    dfs_recursive(start_node)

# Example usage:
# Constructing a graph
#   1 -- 2 -- 3
#   |    |
#   4 -- 5

graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 5)
graph.add_edge(4, 5)

# Calling DFS on the graph
print("DFS traversal:")
dfs(graph, 1)
