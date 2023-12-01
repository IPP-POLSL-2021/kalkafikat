"""Token constants for plagiarism check."""

__all__ = ['tok_name']

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
LOOP = 20
COMP = 21
RETURN = 22
AND = 23
AS = 24
ASSERT = 25
ASYNC = 26
AWAIT = 27
BREAK = 28
CLASS = 29
CONTINUE = 30
DEF = 31
DEL = 32
EXCEPT = 33
FALSE = 34
TRUE = 35
NONE = 36
FINALLY = 37
FROM = 38
NONLOCAL = 39
NOT = 40
OR = 41
PASS = 42
RAISE = 43
TRY = 44
WITH = 45
CASE = 46
MATCH = 47
FSTRING_START = 48
FSTRING_MIDDLE = 49
FSTRING_END = 50
COMMENT = 51
NL = 52
TYPE_IGNORE = 53
TYPE_COMMENT = 54
SOFT_KEYWORD = 55
ERRORTOKEN = 56
ENCODING = 57
N_TOKENS = 58
# Special definitions for cooperation with parser
NT_OFFSET = 256

tok_name = {value: name
            for name, value in globals().items()
            if isinstance(value, int) and not name.startswith('_')}
__all__.extend(tok_name.values())