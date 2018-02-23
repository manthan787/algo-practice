'''
Reverse words in a string in place, without extra space:
ex:
my name is manthan => manthan is name my
'''

def reverse_words(s):
	return " ".join(s.strip().split()[::-1])

print reverse_words("My name is Manthan")
print reverse_words("I like this program very much")