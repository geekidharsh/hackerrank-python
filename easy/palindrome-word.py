# reverse a word to find palindrome if it's a palindrome
def palindrome_word(inp):
	word = inp
	reverse = word[::-1]
	if word == reverse:
		print "palindrome"
	else:
		print "not a palindrome"

palindrome_word(raw_input("enter a word:\t"))