"""
https://leetcode.com/problems/word-search/description/

Given a 2D board and a word, find if the word exists in the grid. 
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = set()
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if (i, j) not in visited:
                    if self.search(board, i, j, visited, word):
                        return True
        return False

    def search(self, board, i, j, visited, word):
        if board[i][j] != word[0]:
            return False

        if len(word[1:]) == 0:
            return True
        # print word, visited, board[i][j], i, j
        visited.add((i, j))
        for neighbor in self.adjacent(board, i, j):
            neighbor_i, neighbor_j = neighbor
            if neighbor not in visited:
                if self.search(board, neighbor_i, neighbor_j, visited, word[1:]):
                    return True
        visited.remove((i, j))
        return False

    def adjacent(self, board, i, j):
        rows, cols = len(board), len(board[0])
        for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
            if x >= 0 and x < rows and y >= 0 and y < cols:
                yield (x, y)


s = Solution()
m1 = [['F', 'A', 'C', 'I'],
      ['O', 'B', 'Q', 'P'],
      ['A', 'N', 'O', 'B'],
      ['M', 'A', 'S', 'S']]
m2 = [["F", "Y", "C", "E", "N", "R", "D"],
      ["K", "L", "N", "F", "I", "N", "U"],
      ["A", "A", "A", "R", "A", "H", "R"],
      ["N", "D", "K", "L", "P", "N", "E"],
      ["A", "L", "A", "N", "S", "A", "P"],
      ["O", "O", "G", "O", "T", "P", "N"],
      ["H", "P", "O", "L", "A", "N", "O"]]
assert s.exist(m1, "FACE") == False
assert s.exist(m1, "FOAM") == True
assert s.exist(m1, "BOSS") == True
assert s.exist(m2, "FRANCE") == True
assert s.exist(m2, "LAARA") == True
