class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

def inorder(root):
    traversal = []
    if not root:
        return traversal
    traversal += inorder(root.left)
    traversal.append(root.val)
    traversal += inorder(root.right)
    return traversal

def reverse_inorder(root, count, k):
    if not root or count >= k:
        return count
    count = reverse_inorder(root.right, count, k)
    count += 1
    if count == k:
        print "Second Largest Node: ", root.val
        return count
    count = reverse_inorder(root.left, count, k)
    return count

# Find kth largest element in the given BST
def find_kth_largest(root, k):
    return reverse_inorder(root, 0, k)

s = TreeNode(2)
s.left = TreeNode(1)
s.right = TreeNode(4, TreeNode(3), TreeNode(7))

find_kth_largest(s, 2)
find_kth_largest(s, 1)
find_kth_largest(s, 4)