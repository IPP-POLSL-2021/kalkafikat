import tokenize as tkn
import token as tk
import kftokenize
import re
from io import TextIOWrapper
import codecs
import glob
import numpy as np
from token import EXACT_TOKEN_TYPES
oldtoken = ""


def similar(str1, str2):
    str1 = str1 + ' ' * (len(str2) - len(str1))
    str2 = str2 + ' ' * (len(str1) - len(str2))
    return sum(1 if i == j else 0
               for i, j in zip(str1, str2)) / float(len(str1))


with kftokenize.open('./kftokenize.py') as f:
    pliki = glob.glob('./baza/*.py')
    print(pliki)
    tabavg = []
    for plik in pliki:
        with kftokenize.open(plik) as plagiat:
            with open('out.txt', 'w') as ff:
                tokens = kftokenize.tokenize(f.readline)

                for token in tokens:
                    plagiatTokenizer = kftokenize.tokenize(plagiat.readline)
                    for token2 in plagiatTokenizer:
                        tokStr2 = repr(token2)
                        ff.write(str(token)+'\n')
                        tokenStr = repr(token)
                        # if oldtoken != "":
                        # porównywanie tokenów pokolei do siebie
                        # print(similar(tokenStr, tokStr2))
                        tabavg.append(similar(tokenStr, tokStr2))
    print(np.average(tabavg)*100)
    # oldtoken = repr(token)
