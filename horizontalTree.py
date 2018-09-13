def syntaxValid(s):
	""" Checks if string s has valid syntax for horizontal tree.
	Args:
		s: input string to test for proper syntax.
	Returns:
		True if s has valid syntax, False otherwise.
	"""
	if not s or type(s) != str or s[0] != '[':
		return False

	#using stack to check for matching brackets
	#push '[' and pop for ']'
	bracketStack = []
	for i in range(len(s)):
		currentChar = s[i]
		if currentChar == '[':
			#check for there is a delimiter before open bracket or trying to double nest
			if i != 0 and s[i-1] == '[' or i > 1 and s[i-2] != ',':
				return False
			bracketStack.append('[')
		elif currentChar == ']':
			#check if stack is prematurely empty or no delimiter after closed bracket
			if not bracketStack or (i != len(s)-1 and s[i+1] != ']' and s[i+1] != ','):
				return False 
			else: 
				bracketStack.pop()
		elif currentChar == ',':
			#check if delimiter is invalid
			if i == 0 or i == len(s)-1 or s[i-1] == '[' or s[i+1] != ' ':
				return False
	#if the stack is empty, we have matched brackets, hence s is valid
	return len(bracketStack) == 0

def getHorizontalTreeString(s):
	""" Computes a string of characters that when printed displays horizontal tree of s
	Args:
		s: input string to print as a horizontal tree
	Returns:
		A string of characters
	"""
	#we know first character is '[' so we can skip it:
	outputBuffer = [s[1]]
	nestingLevel = 0
	for i in range(2,len(s)):
		currentChar = s[i]
		if currentChar == '[':
			nestingLevel += 1
			outputBuffer.append(' ')
		elif currentChar == ']':
			nestingLevel -= 1
		elif currentChar == ',':
			outputBuffer.append('\n')
			for _ in range(nestingLevel):
				outputBuffer.append(' ')
		elif currentChar != ' ':
			outputBuffer.append(currentChar)
	return "".join(outputBuffer)

def printAsHorizontalTree(s):
	""" Helper for Horizontal Tree
	Args: s: input string to print as a horizontal tree
	"""
	ERROR_MSG = "Invalid!"
	if syntaxValid(s):
		print(getHorizontalTreeString(s))
	else:
		print(ERROR_MSG)

def main():
	s = "[1, 2, [A, B, C, [5, 6]]]"
	printAsHorizontalTree(s)

if __name__ == "__main__":
    main()


