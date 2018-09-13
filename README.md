# Horizontal Tree

## Assumptions:

All of the following must be true for an input string to be valid:
- (1) Matched brackets (e.g "[abc[]" would be invalid).
- (2) The input string must begin with an open bracket and end with a closed bracket.
- (3) All characters must be surrounded by at least one pair of matched brackets.
- (4) No commas can never be directly adjacent to an opening or closing bracket (e.g "[, [abc]]" would be invalid but "[ , [abc]] would be valid)
- (5) A space character must follow directly after every comma.

Additionally,
- A  delimiter ", " before a new nesting level is optional (e.g [First Level, [Second Level]] and [First Level [Second Level]] are both valid strings).
- Spaces are only to define the delimiter and are ignored otherwise.

## Algorithm: 

The algorithm works in two passes: The first pass checks for proper syntax and the second deals with the print logic. While we could certaintly do this is in one pass, I found it is much clearer to what is happening. Of course, if the we expect very long strings, we could certaitnly condense the algorithm into a single pass with the sacrafice of some clarity. 

Time complexity: Let N be the length of the input string S. For the first pass, we simply iterate through S checking proper syntax. On the second pass, we iterate through S again, appending to an output buffer for at most N characters (which is an amortized constant operation). This gives us a linear run time, hence O(N).

Space complexity: Every character (besides delimiters and brackets) must be added to the output buffer, along ' ' and '\n' characters for print structure. While even for the worst case we have many nested levels and single elements (hence, many newlines), the amount of characters in the output buffer cannot be more than .   
