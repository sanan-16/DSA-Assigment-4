class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)

def count_internal_nodes(node):
    if node is None:
        return 0
    left_count = count_internal_nodes(node.left)
    right_count = count_internal_nodes(node.right)
    return 1 + (left_count + right_count) if node.left or node.right else 0

def identify_full_subtrees(node):
    if node is None:
        return True
    left_full = identify_full_subtrees(node.left)
    right_full = identify_full_subtrees(node.right)
    return left_full and right_full and ((node.left and node.right) or (node.left is None and node.right is None))

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)

print("Number of leaves:", count_leaves(root))
print("Number of internal nodes:", count_internal_nodes(root))
print("Identify full subtrees:", identify_full_subtrees(root))
