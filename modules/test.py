import tokenize as tkn
import token as tk
import kftoken
import re
from token import EXACT_TOKEN_TYPES

def group(*choices): return '(' + '|'.join(choices) + ')'

print(group(*map(re.escape, sorted(EXACT_TOKEN_TYPES, reverse=True))))
print(kftoken.names)
print(EXACT_TOKEN_TYPES.keys())
print(tkn.String)