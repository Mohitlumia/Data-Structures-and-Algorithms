
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def print_tree(node, level=0):
    if node is None:
        return
    print("   " * level + "|--", node.data)
    for child in node.children:
        print_tree(child, level + 1)

# Example usage:
if __name__ == "__main__":
    root = TreeNode("A")
    b = TreeNode("B")
    c = TreeNode("C")
    d = TreeNode("D")
    e = TreeNode("E")
    f = TreeNode("F")

    root.add_child(b)
    root.add_child(c)
    b.add_child(d)
    b.add_child(e)
    c.add_child(f)

    print_tree(root)
