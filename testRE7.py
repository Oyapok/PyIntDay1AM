import re

"""
sub()
"""

text="date: 2002:23:02"

regexp=re.compile(r"(\d{4}):(\d{2}):(\d{2})")


result=regexp.sub(r"\2/\3/\1", text)

print(result)
   