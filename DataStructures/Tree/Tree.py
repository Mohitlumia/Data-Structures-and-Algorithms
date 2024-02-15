
class tree:
    def __init__(self,data):
        self.val = data
        self.child = []
    
    def add_child(self,child):
        self.child.append(child)

root = tree(0)

child1 = tree(1)
child2 = tree(2)
child3 = tree(3)
child4 = tree(4)

root.add_child(child1)
root.add_child(child2)
root.add_child(child3)
root.add_child(child4)