"""Tokenization for plagiarism checking.
"""

from builtins import open as _open
from codecs import BOM_UTF8
import collections
import functools
from io import TextIOWrapper
import itertools
import re

from kftoken import *

import kftoken
__all__ = kftoken.__all__ + []
del kftoken

# memorize function into cache (expression is compiled as unicode)
@functools.lru_cache
def _compile(expr):
    return re.compile(expr, re.UNICODE)

class TokenNode(collections.namedtuple('TokenNode', 'type string start end line')):
    def __repr__(self):
        annotated_type = '%d (%s)' % (self.type, names[self.type])
        return ('TokenInfo(type=%s, string=%r, start=%r, end=%r, line=%r)' %
                self._replace(type=annotated_type))

# regex group functions (grouping with or)
def group(*choices): return '(' + '|'.join(choices) + ')'
def any(*choices): return group(*choices) + '*'
def maybe(*choices): return group(*choices) + '?'

# basic regexes
Whitespace = r'[ \f\t]*'
Comment = r'#[^\r\n]*'
Name = r'\w+'

# making regex for every number literal
Hexnumber = r'0[xX](?:_?[0-9a-fA-F])+'
Binnumber = r'0[bB](?:_?[01])+'
Octnumber = r'0[oO](?:_?[0-7])+'
Decnumber = r'(?:0(?:_?0)*|[1-9](?:_?[0-9])*)'
Intnumber = group(Hexnumber, Binnumber, Octnumber, Decnumber)
Exponent = r'[eE][-+]?[0-9](?:_?[0-9])*'
Pointfloat = group(r'[0-9](?:_?[0-9])*\.(?:[0-9](?:_?[0-9])*)?', r'\.[0-9](?:_?[0-9])*') + maybe(Exponent)
Expfloat = r'[0-9](?:_?[0-9])*' + Exponent
Floatnumber = group(Pointfloat, Expfloat)
Imagnumber = group(r'[0-9](?:_?[0-9])*[jJ]', Floatnumber + r'[jJ]')
# combine all number regexes into single regex
Number = group(Imagnumber, Floatnumber, Intnumber)

# special symbols regex
# reverse to ensure shorter symbols don't come before longer ones, ending search
Special = group(*map(re.escape, sorted(symbols, reverse=True)))
# group them with withspaces
Special = group(r'\r?\n', Special)

# generate prefixes used in python
def _all_string_prefixes():
    _valid_string_prefixes = ['b', 'r', 'u', 'f', 'br', 'fr']
    result = {''}
    for prefix in _valid_string_prefixes:
        for perm in itertools.permutations(prefix):
            for prod in itertools.product(*[(pref, pref.upper()) for pref in perm]):
                result.add(''.join(prod))
    return result

StringPrefixRegex = group(*_all_string_prefixes())

# Tail end of ' string.
Single = r"[^'\\]*(?:\\.[^'\\]*)*'"
# Tail end of " string.
Double = r'[^"\\]*(?:\\.[^"\\]*)*"'
# Tail end of ''' string.
Single3 = r"[^'\\]*(?:(?:\\.|'(?!''))[^'\\]*)*'''"
# Tail end of """ string.
Double3 = r'[^"\\]*(?:(?:\\.|"(?!""))[^"\\]*)*"""'
# Beginning of ''' or """ string
Triple = group(StringPrefixRegex + "'''", StringPrefixRegex + '"""')

String = group(StringPrefixRegex + r"'[^\n'\\]*(?:\\.[^\n'\\]*)*" +
                group("'", r'\\\r?\n'),
                StringPrefixRegex + r'"[^\n"\\]*(?:\\.[^\n"\\]*)*' +
                group('"', r'\\\r?\n'))
Extras = group(r'\\\r?\n|\Z', Comment, Triple)
PseudoToken = Whitespace + group(Extras, Number, Special, String, Name)

class Tokenizer():
    def __init__(self):
        endpats = {}
        for _prefix in _all_string_prefixes():
            endpats[_prefix + "'"] = Single
            endpats[_prefix + '"'] = Double
            endpats[_prefix + "'''"] = Single3
            endpats[_prefix + '"""'] = Double3

        single_quoted = set()
        triple_quoted = set()
        for t in _all_string_prefixes():
            for u in (t + '"', t + "'"):
                single_quoted.add(u)
            for u in (t + '"""', t + "'''"):
                triple_quoted.add(u)

        tabsize = 8
    def tokenize(self, readline):
        pass


def detect_encoding(readline):
    default = 'utf-8'
    def read():
        try:
            return readline()
        except StopIteration:
            return b''

    line = read()
    if line.startswith(BOM_UTF8):
        line = line[3:]
        default = 'utf-8-sig'
    if not line:
        return default
    return default
    
def open(filename):
    buffer = _open(filename, 'rb')
    try:
        encoding = detect_encoding(buffer.readline)
        buffer.seek(0)
        text = TextIOWrapper(buffer, encoding, line_buffering=True)
        text.mode = 'r'
        return text
    except:
        buffer.close()
        raise    
