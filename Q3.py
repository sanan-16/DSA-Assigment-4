class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_min(node):
    while node.left is not None:
        node = node.left
    return node.key

def find_max(node):
    while node.right is not None:
        node = node.right
    return node.key

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)

min_value = find_min(root)
max_value = find_max(root)

print("Minimum value in the BST:", min_value)
print("Maximum value in the BST:", max_value)
