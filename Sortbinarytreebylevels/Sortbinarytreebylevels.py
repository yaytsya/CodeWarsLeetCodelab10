from collections import deque

def tree_by_levels(node):
    if not node:
        return []
    
    result = []
    queue = deque([node])
    
    while queue:
        current = queue.popleft()
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return result
