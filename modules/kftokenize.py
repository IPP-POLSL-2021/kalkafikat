"""Tokenization for plagiarism checking.
"""

import collections
from kftoken import *

import kftoken
__all__ = kftoken.__all__ + []
del kftoken

class TokenNode(collections.namedtuple('TokenNode', 'type string start end line')):
    def __repr__(self):
        annotated_type = '%d (%s)' % (self.type, names[self.type])
        return ('TokenInfo(type=%s, string=%r, start=%r, end=%r, line=%r)' %
                self._replace(type=annotated_type))
