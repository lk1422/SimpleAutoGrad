from Number import Number 

def topsort(root):
    order = []
    seen = set()
    DFS(root, seen, order)
    order.reverse()
    return order

def DFS(root, seen, order):
    seen.add(root)
    for node in root.parents:
        if node not in seen:
            DFS(node, seen, order)
    order.append(root)

