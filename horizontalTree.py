def checkSyntax(s):
	""" Checks for proper syntax:
		Returns True if a valid string, otherwise False:
	"""
	if not s or type(s) != str or s[0] != '[':
		return False

	bracketStack = []
	for i in range(len(s)):
		currentChar = s[i]
		if currentChar == '[':
			bracketStack.append('[')
		elif currentChar == ']':
			if bracketStack:
				bracketStack.pop()
			else:
				return False
		elif currentChar == ',':
			if i == 0 or i == len(s)-1 or s[i-1] == '[' or s[i+1] != ' ':
				return False
	return len(bracketStack) == 0
