class TreeNode(object):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_binary_tree(root):
    if not root:
        return root
    root.left, root.right = invert_binary_tree(root.right), \
        invert_binary_tree(root.left)
    return root


t = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)),
             TreeNode(7, TreeNode(6), TreeNode(9)))
print invert_binary_tree(t)
