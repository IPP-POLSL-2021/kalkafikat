import tokenize as tkn
import token as tk
import kftokenize
import re
from io import TextIOWrapper
import codecs
from token import EXACT_TOKEN_TYPES
import glob
import numpy as np


def similar(str1, str2):
    str1 = str1 + ' ' * (len(str2) - len(str1))
    str2 = str2 + ' ' * (len(str1) - len(str2))
    return sum(1 if i == j else 0
               for i, j in zip(str1, str2)) / float(len(str1))


def TakPlagiat(str1):
    plagiatNaTaken = 0
    with kftokenize.open(str1) as f:
        original_tokens = list(kftokenize.tokenize(f.readline))

        pliki = glob.glob('./baza/*.py')
        print(pliki)
        tabavg = []

        for token in original_tokens:
            max_similarity_per_line = []

            for plik in pliki:
                with kftokenize.open(plik) as plagiat:
                    plagiat_tokens = list(
                        kftokenize.tokenize(plagiat.readline))
                    max_similarity = 0

                    for token2 in plagiat_tokens:
                        tok_str2 = repr(token2)
                        token_str = repr(token)
                        max_similarity = max(
                            max_similarity, similar(token_str, tok_str2))

                    max_similarity_per_line.append(max_similarity)

            tabavg.append(max(max_similarity_per_line))

        print(np.average(tabavg) * 100)
        plagiatNaTaken = (np.average(tabavg) * 100)
    return plagiatNaTaken
