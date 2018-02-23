'''
Find the next biggest node in BST
'''

class Node(object):

    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right

def next_biggest_node(node):
    if not node: return None
    next_biggest = None
    if not node.right:
        next_biggest = find_node_upper(node)
    else:
        next_biggest = find_leftmost_node(node.right)
    return next_biggest

def find_leftmost_node(node):
    if not node.left: return node
    return find_leftmost_node(node.left)

def find_node_upper(node):
    if not node.parent: return None
    if node.parent.left == node: return node.parent
    if node.parent.right == node:
        return find_node_upper(node.parent)

'''
                    20
            8               22
        4       12
            10      14
Next biggest for 8 -> 10
Next biggest for 14 -> 20
'''
root = Node(20)
root.right = Node(22, parent=root)
eight = Node(8, parent=root)
four = Node(4, parent=eight)
twelve = Node(12, parent=eight)
eight.right = twelve
eight.left = four
root.left = eight
twelve.left = Node(10, parent=twelve)
twelve.right = Node(14, parent=twelve)
assert next_biggest_node(eight).val == 10
assert next_biggest_node(twelve.right).val == 20
assert next_biggest_node(root.right) == None
assert next_biggest_node(twelve.left).val == 12