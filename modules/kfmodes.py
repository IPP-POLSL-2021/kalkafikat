import modules.kftokenize as kftokenize
import glob
import numpy as np
import os

CUR_DIR = os.path.dirname(__file__)

__all__ = ['check', 'compare']

def similar(str1, str2):
    str1 = str1 + ' ' * (len(str2) - len(str1))
    str2 = str2 + ' ' * (len(str1) - len(str2))
    return sum(1 if i == j else 0
               for i, j in zip(str1, str2)) / float(len(str1))

def check(filename: str) -> float:
    with kftokenize.open(filename) as f:
        original_tokens = list(kftokenize.tokenize(f.readline))
        pliki = glob.glob(os.path.join(CUR_DIR,'baza','*'))
        tabavg = []

        for token in original_tokens:
            max_similarity_per_line = []

            for plik in pliki:
                with kftokenize.open(plik) as plagiat:
                    plagiat_tokens = list(kftokenize.tokenize(plagiat.readline))
                    max_similarity = 0

                    for token2 in plagiat_tokens:
                        tok_str2 = repr(token2)
                        token_str = repr(token)
                        max_similarity = max(max_similarity, similar(token_str, tok_str2))
                    max_similarity_per_line.append(max_similarity)
            tabavg.append(max(max_similarity_per_line))

    return(np.average(tabavg) * 100)

def compare(filename1: str, filename2: str) -> float:
    with kftokenize.open(filename1) as f:
        original_tokens = list(kftokenize.tokenize(f.readline))
        tabavg = []

        for token in original_tokens:
            max_similarity_per_line = []

            with kftokenize.open(filename2) as plagiat:
                plagiat_tokens = list(kftokenize.tokenize(plagiat.readline))
                max_similarity = 0

                for token2 in plagiat_tokens:
                    tok_str2 = repr(token2)
                    token_str = repr(token)
                    max_similarity = max(max_similarity, similar(token_str, tok_str2))
                max_similarity_per_line.append(max_similarity)
            tabavg.append(max(max_similarity_per_line))

    return(np.average(tabavg) * 100)
