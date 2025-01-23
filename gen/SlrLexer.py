# Generated from E:/University/Semester6/Compiler/SLR-Compiler-Project/Grammar/Slr.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,3,26,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,1,4,1,13,
        8,1,11,1,12,1,14,1,1,1,1,1,2,1,2,1,2,1,2,3,2,23,8,2,1,2,1,2,0,0,
        3,1,1,3,2,5,3,1,0,1,3,0,9,9,13,13,32,32,28,0,1,1,0,0,0,0,3,1,0,0,
        0,0,5,1,0,0,0,1,7,1,0,0,0,3,12,1,0,0,0,5,22,1,0,0,0,7,8,5,115,0,
        0,8,9,5,108,0,0,9,10,5,114,0,0,10,2,1,0,0,0,11,13,7,0,0,0,12,11,
        1,0,0,0,13,14,1,0,0,0,14,12,1,0,0,0,14,15,1,0,0,0,15,16,1,0,0,0,
        16,17,6,1,0,0,17,4,1,0,0,0,18,23,5,10,0,0,19,20,5,13,0,0,20,23,5,
        10,0,0,21,23,5,13,0,0,22,18,1,0,0,0,22,19,1,0,0,0,22,21,1,0,0,0,
        23,24,1,0,0,0,24,25,6,2,0,0,25,6,1,0,0,0,3,0,14,22,1,6,0,0
    ]

class SlrLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    WS = 2
    NEWLINE = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'slr'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "NEWLINE" ]

    ruleNames = [ "T__0", "WS", "NEWLINE" ]

    grammarFileName = "Slr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


