# directed graph also known as digraph
# it cointains link between start and end node

class DirectedGraph:

    def __init__(self):
        self.graph_dict = {}
        
    def add_edge(self, start, end):
        if start in self.graph_dict:
            self.graph_dict[start].append(end)
        else:
            self.graph_dict[start] = [end]

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths



# Helper function to add all edges into graph

def add_all_edges(routes):
    # Initiate object of class DirectedGraph
    obj = DirectedGraph()
    for start, end in routes:
        obj.add_edge(start, end)
    return obj


if __name__ == '__main__':

    # routes are the edges which connects two nodes
    # let say Mumbai and Pune called as node pair
    routes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]

    route_graph = add_all_edges(routes)

    # get all paths from start edge to end edge
    start = "Mumbai"
    end = "Bangaluru"

    paths = route_graph.get_paths(start, end)

    print(f"All paths between: {start} and {end}: ",paths)
