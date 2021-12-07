import re

text="value +8977654 the end"

"""
\d     a digit <=> [0123456789] <=> [0-9]
+      1 or more occurrences
{min,max} between [min,max] occurrences
{2,}    2 or more occurences
{3}     3 occurrences
{1,} <=> + (1 or more occurences)
{0,} <=> * (0 or more occurences)
{0,1} <=> ? (symbol can optionaly exist)
[abcAR65]
\s      a space
"""

regexp=re.compile(r"[+-]?\s*\d+")
# regexp=re.compile(r"a{2}")
match = regexp.search(text)
if match:
    print("The string text 'match'")
    print(match[0])
else:
    print("The string text does not 'match'")
