import re

"""
\d          a digit
+           1 or more occurrence
{min,max}   between [min,max] occurrences
{2,}        2 or more occurrences
{3}         3 occurrences
{1,}        <=> +
{0,}        <=> *
{0,1}       <=> ?
.           any character except a new line
\.          the character .
[123]       the digits 1,2 or 3
[a-z] [A-Z] small or capitals letters
\d          <=> [0123456789]
\d          <=> [0-9]
^           begin with
[^0-9]      any character except a digit
\D          <=> [^0-9]
\s          <=> white space
\S          any character except a whitespace
"""

text="value 278.3 gkhfdqhgdqsghkj "

# regexp=re.compile(r"(\D+)\s+(\d+\.\d+)(.*)")
regexp=re.compile(r"^[^0-9]")

matchobj=regexp.search(text)
if matchobj:
    print("The string text 'match'")
# =============================================================================
    print(matchobj.group(0))

# =============================================================================
else:
    print("The string text does not 'match'")