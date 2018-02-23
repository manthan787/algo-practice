from __future__ import print_function, division

# Tree Node definition
class Tree(object):

	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def evaluate(n):
    ''' Evaluate a tree containing arithmetic expression rooted
        at `n`.
    '''
    if not n: return None
    if n.val.isdigit(): return float(n.val)
    l, r = evaluate(n.left), evaluate(n.right)
    if not all([l, r]): raise Exception("Invalid Expression Tree! Missing operands.")
    return eval_expr(l, r, n.val)


def eval_expr(l, r, operator):
    ''' Given left and right operands and an operator, evaluates
        the expresson and returns l <operator> r
    '''
    if operator == '+': return l + r
    elif operator == '-': return l - r
    elif operator == '/': return l / r
    elif operator == '*': return l * r


# Tests
t = Tree("*", Tree("+", Tree("3"), Tree("2")), Tree("+", Tree("4"), Tree("5")))
assert evaluate(t) == 45

t1 = Tree("-", Tree("1"), Tree("1"))
assert evaluate(t1) == 0

t2 = Tree("/", Tree("*", Tree("1"), Tree("100")), Tree("/", Tree("400"), Tree("200")))
assert evaluate(t2) == 50

t3 = Tree("/", Tree("1"))
evaluate(t3)