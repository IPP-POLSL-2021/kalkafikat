import tokenize as tkn
import token as tk
import kftokenize
import re
from io import TextIOWrapper
import codecs
from token import EXACT_TOKEN_TYPES

with kftokenize.open('./modules/kftokenize.py') as f:
    with open('out.txt', 'w') as ff:
        tokens = kftokenize.tokenize(f.readline)
        for token in tokens:
            ff.write(str(token)+'\n')