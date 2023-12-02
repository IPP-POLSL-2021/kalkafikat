import tokenize as tkn
import token as tk
import kftoken
import re
from io import TextIOWrapper
import codecs
from token import EXACT_TOKEN_TYPES

def group(*choices): return '(' + '|'.join(choices) + ')'

print(group(*map(re.escape, sorted(EXACT_TOKEN_TYPES, reverse=True))))
print(kftoken.names)
print(EXACT_TOKEN_TYPES.keys())
print(tkn.Funny)

f = open('tokens.txt', 'rb')
b = f.readline()
print(b.startswith(codecs.BOM_UTF8))

buffer = open('tokens.txt', 'rb')
try:
    buffer.seek(0)
    text = TextIOWrapper(buffer, 'utf-8', line_buffering=True)
    text.mode = 'r'
    print(text)
except:
    buffer.close()
    raise
"""Plany
 - rozwiazac problem encodowania
 - open file bit
 - tokenizer class
 - prefixes
 - tokenize func
"""