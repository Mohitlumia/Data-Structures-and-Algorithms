class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

# Example
cities = ["New York", "Los Angeles", "Chicago", "London", "Paris", "Tokyo"]
countries = {"New York": "USA", "Los Angeles": "USA", "Chicago": "USA", "London": "UK", "Paris": "France", "Tokyo": "Japan"}

# Initialize UnionFind with the number of cities
uf = UnionFind(len(cities))

# Merge cities based on their countries
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        if countries[cities[i]] == countries[cities[j]]:
            uf.union(i, j)

# Find which set each city belongs to
sets = {}
for i in range(len(cities)):
    root = uf.find(i)
    if root not in sets:
        sets[root] = []
    sets[root].append(cities[i])

print("Disjoint sets of cities based on countries:")
for cities_in_set in sets.values():
    print(cities_in_set)
