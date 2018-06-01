class Tree(object):

    def __init__(self, x=0, l=None, r=None):
        self.x = x
        self.l = l
        self.r = r


def solution(T):
    return largest_perfect_subtree(T)[0]


def largest_perfect_subtree(T, depth=0):
    size = 0
    if not T:
        return 0, depth
    if T.l and T.r:
        depth += 1
    left_size, left_depth = largest_perfect_subtree(T.l, depth + 1)
    right_size, right_depth = largest_perfect_subtree(T.r, depth + 1)
    if left_depth == right_depth:
        size = 1 + left_size + right_size
    return max(size, left_size, right_size), min(left_depth, right_depth)


t = Tree(1, l=Tree(1), r=Tree(1))
t1 = Tree(1, l=Tree(1))
t2 = Tree(1, l=Tree(2, r=Tree(3)), r=Tree(4))
t3 = Tree(1, l=Tree(2, l=Tree(-10, l=t2, r=t2), r=Tree(3)),
          r=Tree(4, l=Tree(-10)))
print(solution(t1))
