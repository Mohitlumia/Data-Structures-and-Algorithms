
# bfs in binary tree iterate level by level from left to right

queue = [root]

while queue:

    first = queue.pop(0)
    # operation can be performed here like printing values
    print(first.val)

    if first.left:
        queue.append(first.left)
    if first.right:
        queue.append(first.right)

