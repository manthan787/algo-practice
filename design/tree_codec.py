class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        return "{}-L:{} R:{}".format(self.val, self.left, self.right)


class Codec(object):

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        return str(self.traverse(root))

    def traverse(self, root):
        ''' Traverses the tree in preorder fashion and returns the
            traversal
        '''
        traversal = []
        if not root:
            traversal.append(None)
            return traversal
        else:
            traversal.append(root.val)
            traversal += self.traverse(root.left)
            traversal += self.traverse(root.right)
            return traversal

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        nodes = []
        for val in data[1:-1].split(","):
            nodes.append(int(val.strip()) if val.strip() != 'None' else None)
        print nodes
        return self.build_tree(nodes)[0]

    def build_tree(self, nodes, pos=-1):
        ''' Builds tree from given pre-order traversal '''
        pos += 1
        if pos >= len(nodes):
            return None, pos
        if nodes[pos] is None:
            return None, pos
        else:
            node = TreeNode(int(nodes[pos]))
            left, pos = self.build_tree(nodes, pos)
            right, pos = self.build_tree(nodes, pos)
            node.left = left
            node.right = right
            return node, pos


# test_tree = TreeNode(3, TreeNode(1), TreeNode(-1))
c = Codec()
# serialized = c.serialize(test_tree)
# print serialized
# de = c.deserialize(serialized)
# print c.traverse(de)
# print c.traverse(test_tree)

# failing_test = TreeNode(5, TreeNode(2), TreeNode(3, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(4)))
failing_test = TreeNode(-1, TreeNode(0), TreeNode(1))
serialized = c.serialize(failing_test)
print serialized
de = c.deserialize(serialized)
print c.traverse(de)
