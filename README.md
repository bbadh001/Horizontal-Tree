# Horizontal Tree

## Assumuptions:

All of the following must be true for an input string to be valid:
- (1) Matched brackets (e.g "[abc[]" would be invalid).
- (2) The input string must begin with an open bracket and end with a closed bracket.
- (3) All characters must be surrounded by at least one pair of matched brackets.
- (4) No commas can never be directly adjecent to a opening or closing bracket (e.g "[, [abc]]" would be invalid but "[ , [abc]] would be valid)
- (5) A space must follow directly after every comma.

Additonally,
- A  delimter ", " before a new nesting level is optional (e.g [First Level, [Second Level]] and [First Level [Second Level]] are both valid strings).
- Spaces are only to define the delimiter and are ignored otherwise.

## Algorithm: 
- 
