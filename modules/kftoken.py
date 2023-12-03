"""Token constants for plagiarism check."""

__all__ = ['names', 'symbols', 'syntax']

ENDMARKER = 0
NAME = 1
NUMBER = 2
STRING = 3
NEWLINE = 4
INDENT = 5
DEDENT = 6
LPAR = 7
RPAR = 8
LSQB = 9
RSQB = 10
LBR = 11
RBR = 12
COLON = 13
SEMICON = 14
DOT = 15
COMMA = 16
ASSIGN = 17
OP = 18
LOP = 19
ANNOTE = 20
PLACEHOLD = 21
LOOP = 22
COMP = 23
RETURN = 24
AND = 25
AS = 26
ASSERT = 27
ASYNC = 28
AWAIT = 29
BREAK = 30
CLASS = 31
CONTINUE = 32
DEF = 33
DEL = 34
EXCEPT = 35
FALSE = 36
TRUE = 37
NONE = 38
FINALLY = 39
FROM = 40
NONLOCAL = 41
NOT = 42
OR = 43
PASS = 44
RAISE = 45
TRY = 46
WITH = 47
CASE = 48
MATCH = 49
FSTRING_START = 50
FSTRING_MIDDLE = 51
FSTRING_END = 52
COMMENT = 53
NL = 54
TYPE_IGNORE = 55
TYPE_COMMENT = 56
SOFT_KEYWORD = 57
ERRORTOKEN = 58
ENCODING = 59
N_TOKENS = 60
# Special definitions for cooperation with parser
NT_OFFSET = 256

names = {value: name
            for name, value in globals().items()
            if isinstance(value, int) and not name.startswith('_')}

__all__.extend(names.values())

symbols = {
    '!=': LOP,       
    '%': OP, 
    '%=': ASSIGN, 
    '&': OP, 
    '&=': ASSIGN, 
    '(': LPAR, 
    ')': RPAR, 
    '*': OP, 
    '**': OP, 
    '**=': ASSIGN, 
    '*=': ASSIGN, 
    '+': OP, 
    '+=': ASSIGN, 
    ',': COMMA, 
    '-': OP, 
    '-=': ASSIGN, 
    '->': ANNOTE, 
    '.': DOT, 
    '...': PLACEHOLD, 
    '/': OP, 
    '//': OP, 
    '//=': ASSIGN, 
    '/=': ASSIGN, 
    ':': COLON, 
    ':=': ASSIGN, 
    ';': SEMICON, 
    '<': LOP, 
    '<<': OP, 
    '<<=': ASSIGN, 
    '<=': LOP, 
    '=': ASSIGN, 
    '==': LOP, 
    '>': LOP, 
    '>=': LOP, 
    '>>': OP, 
    '>>=': ASSIGN, 
    '@': OP, 
    '@=': ASSIGN, 
    '[': LSQB, 
    ']': RSQB, 
    '^': OP, 
    '^=': ASSIGN, 
    '{': LBR, 
    '|': OP, 
    '|=': ASSIGN, 
    '}': RBR, 
    '~': OP
}

syntax = {
    'for': LOOP,
    'while': LOOP,
    'if': COMP,
    'elif': COMP,
    'else': COMP,
    'return': RETURN,
    'yield': RETURN,
    'and': AND,
    'as': AS,
    'assert': ASSERT,
    'async': ASYNC,
    'await': AWAIT,
    'break': BREAK,
    'class': CLASS,
    'continue': CONTINUE,
    'def': DEF,
    'del': DEL,
    'except': EXCEPT,
    'False': FALSE,
    'True': TRUE,
    'None': NONE,
    'finally': FINALLY,
    'from': FROM,
    'nonlocal': NONLOCAL,
    'not': NOT,
    'or': OR,
    'pass': PASS,
    'raise': RAISE,
    'try': TRY,
    'with': WITH,
    'case': CASE,
    'match': MATCH
}