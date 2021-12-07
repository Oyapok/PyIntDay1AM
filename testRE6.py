import re

text="123 56:678   789;;897"

"""
sub() replace the substring that matches the pattern by something else
"""

regexp=re.compile(r"[;:\s]+")


result=regexp.sub(",", text)

print(result)
   