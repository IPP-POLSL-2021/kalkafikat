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
        return ('TokenNode(type=%s, string=%r, start=%r, end=%r, line=%r)' %
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

class TokenError(Exception): pass
class StopTokenizing(Exception): pass


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

def token_generator(readline):
    lnum = parenlev = continued = 0
    numchars = '0123456789'
    contstr, needcont = '', 0
    contline = None
    indents = [0]

    last_line = b''
    line = b''
    while True:
        try:
            # We capture the value of the line variable here because
            # readline uses the empty string '' to signal end of input,
            last_line = line
            line = readline()
        except StopIteration:
            line = b''

        lnum += 1
        pos, max = 0, len(line)

        # continued string
        if contstr:
            if not line:
                raise TokenError("EOF in multi-line string", strstart)
            endmatch = endprog.match(line)
            if endmatch:
                pos = end = endmatch.end(0)
                yield TokenNode(STRING, contstr + line[:end],
                    strstart, (lnum, end), contline + line)
                contstr, needcont = '', 0
                contline = None
            elif needcont and line[-2:] != '\\\n' and line[-3:] != '\\\r\n':
                yield TokenNode(ERRORTOKEN, contstr + line,
                        strstart, (lnum, len(line)), contline)
                contstr = ''
                contline = None
                continue
            else:
                contstr = contstr + line
                contline = contline + line
                continue

        elif parenlev == 0 and not continued:
            if not line: break
            column = 0
            while pos < max:
                if line[pos] == ' ':
                    column += 1
                elif line[pos] == '\t':
                    column = (column//tabsize + 1)*tabsize
                elif line[pos] == '\f':
                    column = 0
                else:
                    break
                pos += 1
            if pos == max:
                break

            if line[pos] in '#\r\n':           # skip comments or blank lines
                if line[pos] == '#':
                    comment_token = line[pos:].rstrip('\r\n')
                    yield TokenNode(COMMENT, comment_token,
                        (lnum, pos), (lnum, pos + len(comment_token)), line)
                    pos += len(comment_token)

                yield TokenNode(NL, line[pos:],
                        (lnum, pos), (lnum, len(line)), line)
                continue

            if column > indents[-1]:           # count indents or dedents
                indents.append(column)
                yield TokenNode(INDENT, line[:pos], (lnum, 0), (lnum, pos), line)
            while column < indents[-1]:
                if column not in indents:
                    raise IndentationError(
                        "unindent does not match any outer indentation level",
                        ("<tokenize>", lnum, pos, line))
                indents = indents[:-1]

                yield TokenNode(DEDENT, '', (lnum, pos), (lnum, pos), line)

        else:                                  # continued statement
            if not line:
                raise TokenError("EOF in multi-line statement", (lnum, 0))
            continued = 0

        while pos < max:
            pseudomatch = _compile(PseudoToken).match(line, pos)
            if pseudomatch:                                # scan for tokens
                start, end = pseudomatch.span(1)
                spos, epos, pos = (lnum, start), (lnum, end), end
                if start == end:
                    continue
                token, initial = line[start:end], line[start]
                print(token)

                if (initial in numchars or                 # ordinary number
                    (initial == '.' and token != '.' and token != '...')):
                    yield TokenNode(NUMBER, token, spos, epos, line)
                elif initial in '\r\n':
                    if parenlev > 0:
                        yield TokenNode(NL, token, spos, epos, line)
                    else:
                        yield TokenNode(NEWLINE, token, spos, epos, line)

                elif initial == '#':
                    assert not token.endswith("\n")
                    yield TokenNode(COMMENT, token, spos, epos, line)

                elif token in triple_quoted:
                    endprog = _compile(endpats[token])
                    endmatch = endprog.match(line, pos)
                    if endmatch:                           # all on one line
                        pos = endmatch.end(0)
                        token = line[start:pos]
                        yield TokenNode(STRING, token, spos, (lnum, pos), line)
                    else:
                        strstart = (lnum, start)           # multiple lines
                        contstr = line[start:]
                        contline = line
                        break

                elif (initial in single_quoted or
                    token[:2] in single_quoted or
                    token[:3] in single_quoted):
                    if token[-1] == '\n':                  # continued string
                        strstart = (lnum, start)
                        endprog = _compile(endpats.get(initial) or
                                        endpats.get(token[1]) or
                                        endpats.get(token[2]))
                        contstr, needcont = line[start:], 1
                        contline = line
                        break
                    else:                                  # ordinary string
                        yield TokenNode(STRING, token, spos, epos, line)

                elif initial.isidentifier():               # ordinary name
                    if token in syntax:
                        yield TokenNode(syntax[token], token, spos, epos, line)
                    yield TokenNode(NAME, token, spos, epos, line)
                elif initial == '\\':                      # continued stmt
                    continued = 1
                else:
                    if initial in '([{':
                        parenlev += 1
                    elif initial in ')]}':
                        parenlev -= 1
                    yield TokenNode(symbols[initial], token, spos, epos, line)
            else:
                yield TokenNode(ERRORTOKEN, line[pos],
                        (lnum, pos), (lnum, pos+1), line)
                pos += 1

    # Add an implicit NEWLINE if the input doesn't end in one
    if last_line and last_line[-1] not in '\r\n' and not last_line.strip().startswith("#"):
        yield TokenNode(NEWLINE, '', (lnum - 1, len(last_line)), (lnum - 1, len(last_line) + 1), '')
    for indent in indents[1:]:                 # pop remaining indent levels
        yield TokenNode(DEDENT, '', (lnum, 0), (lnum, 0), '')
    yield TokenNode(ENDMARKER, '', (lnum, 0), (lnum, 0), '')

def tokenize(readline):
    return token_generator(readline)

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
