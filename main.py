"""
Basic Node class that I took from Leetcode
"""
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Depth First Search
Goes all the way down on one path of the tree and repeats this until it finds a solution.
Complete, but not optimal.
However, it is very memory efficient because it only stores up to d nodes where d is the maximum depth.
"""
def dfs(currNode : Node, target : int) -> bool:
    if not currNode: return False
    if currNode.val == target:
        return True
    return dfs(currNode.left, target) or dfs(currNode.right, target)


"""
Breadth First Search -
Expands level by level and uses a queue.
Because it expands level by level, it will find the optimal solution.
But it may not be the most memory efficient - it may store up to 2^d nodes in the queue where d is the maximum depth of the tree.
"""
from collections import deque
def bfs(root : Node, target: int) -> bool:
    if not root: return False
    q = deque([root])
    while q:
        currNode = q.popleft()
        if currNode.val == target:
            return True
        else:
            if currNode.left:
                q.append(currNode.left)
            if currNode.right:
                q.append(currNode.right)
    return False

"""
Depth Limited Search -
Complete, but not optimal. It is memory efficient because we store only one path.
"""
def dls(root: Node, target: int, remaining_depth: int) -> bool:
    if not root: return False
    if root.val == target: return True
    if remaining_depth == 0: return False

    return dls(root.left, target, remaining_depth - 1) or dls(root.right, target, remaining_depth - 1)

"""
Iterative Deepening Search -
It is essentially depth-limited search repeated called using increasing depths.
By using increasing depths, we can guarantee optimality.

This version return the highest level (most optimal) solution to illustrate this.
"""
def iddfs(root: Node, target: int, farthest_depth: int) -> int:
    if not root: return -1
    depth = 0
    while depth <= farthest_depth:
        if dls(root, target, depth):
            return depth
        depth += 1
    return -1


# Testbench
from random import randint

print("Generating random tree...")
# Generate a random tree
root = Node(50)
q = deque([root])
for _ in range(randint(50, 75)):
    currNode = q.popleft()
    l, r = Node(randint(1, 50)), Node(randint(1, 50))
    currNode.left = l
    currNode.right = r
    q.append(currNode.left)
    q.append(currNode.right)
print("Finished!\n")

target = 25
dls_limit = 3

# Print out results of all searches in the tree.

indent = "  "
print("Depth-first Search")
print(indent, f"Result = {"Found" if dfs(root, target) else "Not Found"}")

print("\nBreadth-first Search")
print(indent, f"Result = {"Found" if bfs(root, target) else "Not Found"}")

print("\nDepth-limited Search")
print(indent, f"Used a depth limit of {dls_limit}")
print(indent, f"Result = {"Found" if dls(root, target, dls_limit) else "Not Found"}")

print("\nIterative Deepening Search")
print(indent, f"Used a depth limit of {dls_limit}")
res = iddfs(root, target, dls_limit)
print(indent, f"Result = {"Found at depth " + str(res) if res != -1 else "Not Found"}")


