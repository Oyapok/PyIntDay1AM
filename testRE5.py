import re

"""
split()
"""

text="123 56:678   789;;897"


regexp=re.compile(r"[;:\s]+")

result=regexp.split(text)

print(result)
   