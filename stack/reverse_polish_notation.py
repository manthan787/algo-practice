'''
https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

Evaluate Reverse Polish Notation.

["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        i = 0
        for i, _ in enumerate(tokens):
            if tokens[i] in "+-/*":
                a = stack.pop()
                b = stack.pop()
                res = self.eval((b, a), tokens[i])
                stack.append(int(res))
            else:
                stack.append(int(tokens[i]))
        return stack.pop()

    def eval(self, operands, operator):
        if operator == '+':
            return operands[0] + operands[1]
        elif operator == '*':
            return operands[0] * operands[1]
        elif operator == '/':
            return operands[0] / float(operands[1])
        else:
            return operands[0] - operands[1]