'''
Implement an autocomplete system.
That is, given a query string s and a dictionary of all possible query strings,
return all strings in the dictionary that have s as a prefix.
'''
class Node(object):
	''' A node in trie '''

	def __init__(self, data, neighbors = None):
		self.data = data
		self.neighbors = neighbors or {}

	def __repr__(self):
		return "<{}>".format(self.neighbors)

class Trie(object):

	def __init__(self):
		self.heads = {}

	def add_word(self, word):
		if word[0] in self.heads:
			head = self.heads[word[0]]
		else:
			head = Node(word[0])
			self.heads[word[0]] = head

		for i in xrange(1, len(word)):
			if word[i] in head.neighbors:
				head = head.neighbors[word[i]]
			else:
				new_node = Node(word[i])
				head.neighbors[word[i]] = new_node
				head = new_node
		head.neighbors['__end__'] = Node("__end__")

	def traverse(self, node, prefix, suggestions):
		if node.data == '__end__':
			suggestions.append(prefix)

		for n, nn in node.neighbors.iteritems():
			if n == '__end__':
				n = ''
			self.traverse(nn, prefix + n, suggestions)
		return suggestions

	def __repr__(self):
		return str(self.heads)

def autocomplete(s, dictionary):
	trie = Trie()

	for word in dictionary:
		trie.add_word(word)

	if s[0] not in trie.heads: return []
	head = trie.heads[s[0]]
	for i in xrange(1, len(s)):
		head = head.neighbors.get(s[i])
		if not head: return []

	return trie.traverse(head, s, [])

print autocomplete("hel", ["duke", "held", "hello", "hell", "hey", "roses", "hits", "interstellar", "international", "inception", "dukki", "dukkar", "dukkareshwar", "dang", "dank", "don"])
