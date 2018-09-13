import unittest
from horizontalTree import syntaxValid

class TestSyntaxValid(unittest.TestCase):
	def test_matchedBrackets(self):
		self.assertEqual(syntaxValid("[1, 1, 1, [2]]"), True)
		self.assertEqual(syntaxValid("[1, 1, 1, [2, 2, 2]"), False)

		self.assertEqual(syntaxValid("[1, 1, 1, 1]"), True)
		self.assertEqual(syntaxValid("1, 1, 1, 1"), False)

		self.assertEqual(syntaxValid("[1, [2, [3, [4, [5]]]]]"), True)
		self.assertEqual(syntaxValid("[1, [2, [3, [4, [5]]]]"), False)

	def test_invalidNesting(self):
		self.assertEqual(syntaxValid("[[]]"), False)
		self.assertEqual(syntaxValid("[a, []]"), True)
		self.assertEqual(syntaxValid("[a, [a]]"), True)

	def test_delimNoSpace(self):
		self.assertEqual(syntaxValid("[1, 2, 3, [4, 5, 6]]"), True)
		self.assertEqual(syntaxValid("[1, 2, 3, [4,5, 6]]"), False)
		self.assertEqual(syntaxValid("[1, 2, 3, [4, 5, 6], 7]"), True)
		self.assertEqual(syntaxValid("[1, 2, 3, [4, 5, 6],7]"), False)
		self.assertEqual(syntaxValid("[ , 2, 3, [4, 5, 6], 7]"), True)
		self.assertEqual(syntaxValid("[, 2, 3, [4,5, 6], 7]"), False)

	def test_delimAfterNesting(self):
		self.assertEqual(syntaxValid("[1, 2, 3, [4, 5, 6], 7, [8, [9, 10, 11]]]"), True)
		self.assertEqual(syntaxValid("[1, 2, 3, [4, 5, 6] 7, [8, [9, 10, 11]]]"), False)

	def test_delimBeforeNesting(self):
		self.assertEqual(syntaxValid("[1, 2, 3, [4, 5, 6], 7, [8, [9, 10, 11]]]"), True)
		self.assertEqual(syntaxValid("[1, 2, 3 [4, 5, 6] 7, [8, [9, 10, 11]]]"), False)

	def test_emptyString(self):
		self.assertEqual(syntaxValid(""), False)

	def test_wrongType(self):
		self.assertEqual(syntaxValid({}), False)
		self.assertEqual(syntaxValid([1,2,3,[4,5,6]]), False)