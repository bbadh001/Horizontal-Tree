# Horizontal Tree

## How to Run:

To run:
```
git clone https://github.com/bbadh001/Horizontal-Tree
cd Horizontal-Tree
python horizontalTree.py
```

To run tests:
```
python -m unittest horizontalTree_test.py
```

## Assumptions:

All of the following must be true for an input string to be valid:
- (1) Matched brackets (e.g. "[abc, []" would be invalid).
- (2) The input string must begin with an open bracket and end with a closed bracket.
- (3) All characters must be surrounded by at least one pair of matched brackets.
- (4) Delimiters must be of the form: ", ".
- (5) Every element (including []) requires a delimiter (e.g. "[1, 2, [A, B, C], 3, 4] would be valid but "[1, 2, [A, B, C] 3, 4]" would be invalid).
- (6) There are no delimiters directly after an opening bracket (e.g. "[, [abc]]" would be invalid but "[ , [abc]]" would be valid).

## The Algorithm: 

The algorithm works in two passes: the first pass checks for proper syntax and the second deals with the print logic. While we could certainly do this is in one pass, I found it to be much clearer to separate the syntax-checking from the printing logic entirely. Of course, if we do expect very long strings, we could condense the algorithm into a single pass with the sacrifice of some clarity. 

Let N be the length of the input string S.

Time complexity: For the first pass, we simply iterate through S checking proper syntax. On the second pass, we iterate through S again, appending to an output buffer on every iteration (which is an amortized constant operation). This gives us a linear runtime, or O(N).

Space complexity: Every character (besides delimiters and brackets) must be added to the output buffer, along with space and newline characters for the print structure. Even in the worst case, where we have many nested levels and single elements, the number of space and newline characters would grow proportionally to the input size. This will give us a linear space complexity, or O(N).
