# Generated from E:/University/Semester6/Compiler/SLR-Compiler-Project/Grammar/Slr.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,35,205,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,
        1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,
        1,4,5,4,74,8,4,10,4,12,4,77,9,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,
        1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,
        1,8,1,8,1,8,5,8,106,8,8,10,8,12,8,109,9,8,1,8,1,8,1,8,1,9,1,9,1,
        9,1,9,1,10,1,10,1,10,1,10,1,10,5,10,123,8,10,10,10,12,10,126,9,10,
        1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,
        1,14,1,14,1,15,1,15,1,15,1,15,1,15,5,15,161,8,15,10,15,12,15,164,
        9,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,20,
        1,20,1,20,1,20,1,21,5,21,195,8,21,10,21,12,21,198,9,21,1,22,4,22,
        201,8,22,11,22,12,22,202,1,22,0,0,23,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,0,0,187,0,46,1,0,0,0,2,49,1,
        0,0,0,4,55,1,0,0,0,6,59,1,0,0,0,8,68,1,0,0,0,10,81,1,0,0,0,12,87,
        1,0,0,0,14,91,1,0,0,0,16,100,1,0,0,0,18,113,1,0,0,0,20,117,1,0,0,
        0,22,130,1,0,0,0,24,139,1,0,0,0,26,147,1,0,0,0,28,151,1,0,0,0,30,
        155,1,0,0,0,32,168,1,0,0,0,34,172,1,0,0,0,36,181,1,0,0,0,38,185,
        1,0,0,0,40,189,1,0,0,0,42,196,1,0,0,0,44,200,1,0,0,0,46,47,3,2,1,
        0,47,48,5,0,0,1,48,1,1,0,0,0,49,50,3,4,2,0,50,51,3,6,3,0,51,52,3,
        14,7,0,52,53,3,22,11,0,53,54,3,34,17,0,54,3,1,0,0,0,55,56,5,1,0,
        0,56,57,5,28,0,0,57,58,3,44,22,0,58,5,1,0,0,0,59,60,5,2,0,0,60,61,
        5,31,0,0,61,62,3,42,21,0,62,63,3,8,4,0,63,64,3,10,5,0,64,65,3,12,
        6,0,65,66,5,32,0,0,66,67,3,42,21,0,67,7,1,0,0,0,68,69,5,3,0,0,69,
        70,5,29,0,0,70,75,5,28,0,0,71,72,5,4,0,0,72,74,5,28,0,0,73,71,1,
        0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,78,1,0,0,0,77,
        75,1,0,0,0,78,79,5,30,0,0,79,80,3,44,22,0,80,9,1,0,0,0,81,82,5,5,
        0,0,82,83,5,26,0,0,83,84,5,6,0,0,84,85,5,26,0,0,85,86,3,44,22,0,
        86,11,1,0,0,0,87,88,5,7,0,0,88,89,5,26,0,0,89,90,3,44,22,0,90,13,
        1,0,0,0,91,92,5,8,0,0,92,93,5,31,0,0,93,94,3,42,21,0,94,95,3,16,
        8,0,95,96,3,18,9,0,96,97,3,20,10,0,97,98,5,32,0,0,98,99,3,42,21,
        0,99,15,1,0,0,0,100,101,5,9,0,0,101,102,5,29,0,0,102,107,5,28,0,
        0,103,104,5,4,0,0,104,106,5,28,0,0,105,103,1,0,0,0,106,109,1,0,0,
        0,107,105,1,0,0,0,107,108,1,0,0,0,108,110,1,0,0,0,109,107,1,0,0,
        0,110,111,5,30,0,0,111,112,3,44,22,0,112,17,1,0,0,0,113,114,5,10,
        0,0,114,115,5,26,0,0,115,116,3,44,22,0,116,19,1,0,0,0,117,118,5,
        11,0,0,118,119,5,29,0,0,119,124,5,24,0,0,120,121,5,4,0,0,121,123,
        5,24,0,0,122,120,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,
        1,0,0,0,125,127,1,0,0,0,126,124,1,0,0,0,127,128,5,30,0,0,128,129,
        3,44,22,0,129,21,1,0,0,0,130,131,5,12,0,0,131,132,5,31,0,0,132,133,
        3,42,21,0,133,134,3,24,12,0,134,135,3,30,15,0,135,136,3,32,16,0,
        136,137,5,32,0,0,137,138,3,42,21,0,138,23,1,0,0,0,139,140,5,13,0,
        0,140,141,5,31,0,0,141,142,3,42,21,0,142,143,3,26,13,0,143,144,3,
        28,14,0,144,145,5,32,0,0,145,146,3,44,22,0,146,25,1,0,0,0,147,148,
        5,14,0,0,148,149,5,22,0,0,149,150,3,44,22,0,150,27,1,0,0,0,151,152,
        5,15,0,0,152,153,5,26,0,0,153,154,3,44,22,0,154,29,1,0,0,0,155,156,
        5,16,0,0,156,157,5,29,0,0,157,162,5,28,0,0,158,159,5,4,0,0,159,161,
        5,28,0,0,160,158,1,0,0,0,161,164,1,0,0,0,162,160,1,0,0,0,162,163,
        1,0,0,0,163,165,1,0,0,0,164,162,1,0,0,0,165,166,5,30,0,0,166,167,
        3,44,22,0,167,31,1,0,0,0,168,169,5,17,0,0,169,170,5,25,0,0,170,171,
        3,44,22,0,171,33,1,0,0,0,172,173,5,18,0,0,173,174,5,31,0,0,174,175,
        3,42,21,0,175,176,3,36,18,0,176,177,3,38,19,0,177,178,3,40,20,0,
        178,179,5,32,0,0,179,180,3,42,21,0,180,35,1,0,0,0,181,182,5,19,0,
        0,182,183,5,23,0,0,183,184,3,44,22,0,184,37,1,0,0,0,185,186,5,20,
        0,0,186,187,5,25,0,0,187,188,3,44,22,0,188,39,1,0,0,0,189,190,5,
        21,0,0,190,191,5,28,0,0,191,192,3,44,22,0,192,41,1,0,0,0,193,195,
        5,34,0,0,194,193,1,0,0,0,195,198,1,0,0,0,196,194,1,0,0,0,196,197,
        1,0,0,0,197,43,1,0,0,0,198,196,1,0,0,0,199,201,5,34,0,0,200,199,
        1,0,0,0,201,202,1,0,0,0,202,200,1,0,0,0,202,203,1,0,0,0,203,45,1,
        0,0,0,6,75,107,124,162,196,202
    ]

class SlrParser ( Parser ):

    grammarFileName = "Slr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'topic '", "'search'", "'query'", "','", 
                     "'year_range'", "'to'", "'max_results'", "'filters'", 
                     "'exclude_keywords'", "'min_pages'", "'languages'", 
                     "'analyze'", "'summarize'", "'method'", "'max_length'", 
                     "'extract_fields'", "'keyword_cloud'", "'report'", 
                     "'format'", "'include_metadata'", "'output_path'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'['", "']'", 
                     "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "METHID", "FORMAT", "LN", 
                      "BOOLEAN", "NUMBER", "DIGIT", "STRING", "LB", "RB", 
                      "LCB", "RCB", "COMMENT", "NEWLINE", "WS" ]

    RULE_start = 0
    RULE_program = 1
    RULE_topic = 2
    RULE_search = 3
    RULE_query = 4
    RULE_yearRange = 5
    RULE_maxResults = 6
    RULE_filters = 7
    RULE_excludeKeywords = 8
    RULE_minPages = 9
    RULE_languages = 10
    RULE_analyze = 11
    RULE_summarize = 12
    RULE_method = 13
    RULE_maxLength = 14
    RULE_extractFields = 15
    RULE_keywordCloud = 16
    RULE_report = 17
    RULE_format = 18
    RULE_includeMetadata = 19
    RULE_outputPath = 20
    RULE_optional_nl = 21
    RULE_mandatory_nl = 22

    ruleNames =  [ "start", "program", "topic", "search", "query", "yearRange", 
                   "maxResults", "filters", "excludeKeywords", "minPages", 
                   "languages", "analyze", "summarize", "method", "maxLength", 
                   "extractFields", "keywordCloud", "report", "format", 
                   "includeMetadata", "outputPath", "optional_nl", "mandatory_nl" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    METHID=22
    FORMAT=23
    LN=24
    BOOLEAN=25
    NUMBER=26
    DIGIT=27
    STRING=28
    LB=29
    RB=30
    LCB=31
    RCB=32
    COMMENT=33
    NEWLINE=34
    WS=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def program(self):
            return self.getTypedRuleContext(SlrParser.ProgramContext,0)


        def EOF(self):
            return self.getToken(SlrParser.EOF, 0)

        def getRuleIndex(self):
            return SlrParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = SlrParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.program()
            self.state = 47
            self.match(SlrParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def topic(self):
            return self.getTypedRuleContext(SlrParser.TopicContext,0)


        def search(self):
            return self.getTypedRuleContext(SlrParser.SearchContext,0)


        def filters(self):
            return self.getTypedRuleContext(SlrParser.FiltersContext,0)


        def analyze(self):
            return self.getTypedRuleContext(SlrParser.AnalyzeContext,0)


        def report(self):
            return self.getTypedRuleContext(SlrParser.ReportContext,0)


        def getRuleIndex(self):
            return SlrParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SlrParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.topic()
            self.state = 50
            self.search()
            self.state = 51
            self.filters()
            self.state = 52
            self.analyze()
            self.state = 53
            self.report()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(SlrParser.STRING, 0)

        def mandatory_nl(self):
            return self.getTypedRuleContext(SlrParser.Mandatory_nlContext,0)


        def getRuleIndex(self):
            return SlrParser.RULE_topic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopic" ):
                listener.enterTopic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopic" ):
                listener.exitTopic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopic" ):
                return visitor.visitTopic(self)
            else:
                return visitor.visitChildren(self)




    def topic(self):

        localctx = SlrParser.TopicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_topic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(SlrParser.T__0)
            self.state = 56
            self.match(SlrParser.STRING)
            self.state = 57
            self.mandatory_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SearchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(SlrParser.LCB, 0)

        def optional_nl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SlrParser.Optional_nlContext)
            else:
                return self.getTypedRuleContext(SlrParser.Optional_nlContext,i)


        def query(self):
            return self.getTypedRuleContext(SlrParser.QueryContext,0)


        def yearRange(self):
            return self.getTypedRuleContext(SlrParser.YearRangeContext,0)


        def maxResults(self):
            return self.getTypedRuleContext(SlrParser.MaxResultsContext,0)


        def RCB(self):
            return self.getToken(SlrParser.RCB, 0)

        def getRuleIndex(self):
            return SlrParser.RULE_search

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSearch" ):
                listener.enterSearch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSearch" ):
                listener.exitSearch(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSearch" ):
                return visitor.visitSearch(self)
            else:
                return visitor.visitChildren(self)




    def search(self):

        localctx = SlrParser.SearchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_search)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(SlrParser.T__1)
            self.state = 60
            self.match(SlrParser.LCB)
            self.state = 61
            self.optional_nl()
            self.state = 62
            self.query()
            self.state = 63
            self.yearRange()
            self.state = 64
            self.maxResults()
            self.state = 65
            self.match(SlrParser.RCB)
            self.state = 66
            self.optional_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(SlrParser.LB, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(SlrParser.STRING)
            else:
                return self.getToken(SlrParser.STRING, i)

        def RB(self):
            return self.getToken(SlrParser.RB, 0)

        def mandatory_nl(self):
            return self.getTypedRuleContext(SlrParser.Mandatory_nlContext,0)


        def getRuleIndex(self):
            return SlrParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)




    def query(self):

        localctx = SlrParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(SlrParser.T__2)
            self.state = 69
            self.match(SlrParser.LB)
            self.state = 70
            self.match(SlrParser.STRING)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 71
                self.match(SlrParser.T__3)
                self.state = 72
                self.match(SlrParser.STRING)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.match(SlrParser.RB)
            self.state = 79
            self.mandatory_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class YearRangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(SlrParser.NUMBER)
            else:
                return self.getToken(SlrParser.NUMBER, i)

        def mandatory_nl(self):
            return self.getTypedRuleContext(SlrParser.Mandatory_nlContext,0)


        def getRuleIndex(self):
            return SlrParser.RULE_yearRange

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterYearRange" ):
                listener.enterYearRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitYearRange" ):
                listener.exitYearRange(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitYearRange" ):
                return visitor.visitYearRange(self)
            else:
                return visitor.visitChildren(self)




    def yearRange(self):

        localctx = SlrParser.YearRangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_yearRange)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(SlrParser.T__4)
            self.state = 82
            self.match(SlrParser.NUMBER)
            self.state = 83
            self.match(SlrParser.T__5)
            self.state = 84
            self.match(SlrParser.NUMBER)
            self.state = 85
            self.mandatory_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MaxResultsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(SlrParser.NUMBER, 0)

        def mandatory_nl(self):
            return self.getTypedRuleContext(SlrParser.Mandatory_nlContext,0)


        def getRuleIndex(self):
            return SlrParser.RULE_maxResults

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMaxResults" ):
                listener.enterMaxResults(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMaxResults" ):
                listener.exitMaxResults(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMaxResults" ):
                return visitor.visitMaxResults(self)
            else:
                return visitor.visitChildren(self)




    def maxResults(self):

        localctx = SlrParser.MaxResultsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_maxResults)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(SlrParser.T__6)
            self.state = 88
            self.match(SlrParser.NUMBER)
            self.state = 89
            self.mandatory_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FiltersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(SlrParser.LCB, 0)

        def optional_nl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SlrParser.Optional_nlContext)
            else:
                return self.getTypedRuleContext(SlrParser.Optional_nlContext,i)


        def excludeKeywords(self):
            return self.getTypedRuleContext(SlrParser.ExcludeKeywordsContext,0)


        def minPages(self):
            return self.getTypedRuleContext(SlrParser.MinPagesContext,0)


        def languages(self):
            return self.getTypedRuleContext(SlrParser.LanguagesContext,0)


        def RCB(self):
            return self.getToken(SlrParser.RCB, 0)

        def getRuleIndex(self):
            return SlrParser.RULE_filters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilters" ):
                listener.enterFilters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilters" ):
                listener.exitFilters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilters" ):
                return visitor.visitFilters(self)
            else:
                return visitor.visitChildren(self)




    def filters(self):

        localctx = SlrParser.FiltersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_filters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(SlrParser.T__7)
            self.state = 92
            self.match(SlrParser.LCB)
            self.state = 93
            self.optional_nl()
            self.state = 94
            self.excludeKeywords()
            self.state = 95
            self.minPages()
            self.state = 96
            self.languages()
            self.state = 97
            self.match(SlrParser.RCB)
            self.state = 98
            self.optional_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExcludeKeywordsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(SlrParser.LB, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(SlrParser.STRING)
            else:
                return self.getToken(SlrParser.STRING, i)

        def RB(self):
            return self.getToken(SlrParser.RB, 0)

        def mandatory_nl(self):
            return self.getTypedRuleContext(SlrParser.Mandatory_nlContext,0)


        def getRuleIndex(self):
            return SlrParser.RULE_excludeKeywords

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExcludeKeywords" ):
                listener.enterExcludeKeywords(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExcludeKeywords" ):
                listener.exitExcludeKeywords(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExcludeKeywords" ):
                return visitor.visitExcludeKeywords(self)
            else:
                return visitor.visitChildren(self)




    def excludeKeywords(self):

        localctx = SlrParser.ExcludeKeywordsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_excludeKeywords)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(SlrParser.T__8)
            self.state = 101
            self.match(SlrParser.LB)
            self.state = 102
            self.match(SlrParser.STRING)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 103
                self.match(SlrParser.T__3)
                self.state = 104
                self.match(SlrParser.STRING)
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 110
            self.match(SlrParser.RB)
            self.state = 111
            self.mandatory_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MinPagesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(SlrParser.NUMBER, 0)

        def mandatory_nl(self):
            return self.getTypedRuleContext(SlrParser.Mandatory_nlContext,0)


        def getRuleIndex(self):
            return SlrParser.RULE_minPages

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMinPages" ):
                listener.enterMinPages(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMinPages" ):
                listener.exitMinPages(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinPages" ):
                return visitor.visitMinPages(self)
            else:
                return visitor.visitChildren(self)




    def minPages(self):

        localctx = SlrParser.MinPagesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_minPages)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(SlrParser.T__9)
            self.state = 114
            self.match(SlrParser.NUMBER)
            self.state = 115
            self.mandatory_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LanguagesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(SlrParser.LB, 0)

        def LN(self, i:int=None):
            if i is None:
                return self.getTokens(SlrParser.LN)
            else:
                return self.getToken(SlrParser.LN, i)

        def RB(self):
            return self.getToken(SlrParser.RB, 0)

        def mandatory_nl(self):
            return self.getTypedRuleContext(SlrParser.Mandatory_nlContext,0)


        def getRuleIndex(self):
            return SlrParser.RULE_languages

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLanguages" ):
                listener.enterLanguages(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLanguages" ):
                listener.exitLanguages(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLanguages" ):
                return visitor.visitLanguages(self)
            else:
                return visitor.visitChildren(self)




    def languages(self):

        localctx = SlrParser.LanguagesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_languages)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(SlrParser.T__10)
            self.state = 118
            self.match(SlrParser.LB)
            self.state = 119
            self.match(SlrParser.LN)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 120
                self.match(SlrParser.T__3)
                self.state = 121
                self.match(SlrParser.LN)
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
            self.match(SlrParser.RB)
            self.state = 128
            self.mandatory_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnalyzeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(SlrParser.LCB, 0)

        def optional_nl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SlrParser.Optional_nlContext)
            else:
                return self.getTypedRuleContext(SlrParser.Optional_nlContext,i)


        def summarize(self):
            return self.getTypedRuleContext(SlrParser.SummarizeContext,0)


        def extractFields(self):
            return self.getTypedRuleContext(SlrParser.ExtractFieldsContext,0)


        def keywordCloud(self):
            return self.getTypedRuleContext(SlrParser.KeywordCloudContext,0)


        def RCB(self):
            return self.getToken(SlrParser.RCB, 0)

        def getRuleIndex(self):
            return SlrParser.RULE_analyze

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnalyze" ):
                listener.enterAnalyze(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnalyze" ):
                listener.exitAnalyze(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnalyze" ):
                return visitor.visitAnalyze(self)
            else:
                return visitor.visitChildren(self)




    def analyze(self):

        localctx = SlrParser.AnalyzeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_analyze)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(SlrParser.T__11)
            self.state = 131
            self.match(SlrParser.LCB)
            self.state = 132
            self.optional_nl()
            self.state = 133
            self.summarize()
            self.state = 134
            self.extractFields()
            self.state = 135
            self.keywordCloud()
            self.state = 136
            self.match(SlrParser.RCB)
            self.state = 137
            self.optional_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SummarizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(SlrParser.LCB, 0)

        def optional_nl(self):
            return self.getTypedRuleContext(SlrParser.Optional_nlContext,0)


        def method(self):
            return self.getTypedRuleContext(SlrParser.MethodContext,0)


        def maxLength(self):
            return self.getTypedRuleContext(SlrParser.MaxLengthContext,0)


        def RCB(self):
            return self.getToken(SlrParser.RCB, 0)

        def mandatory_nl(self):
            return self.getTypedRuleContext(SlrParser.Mandatory_nlContext,0)


        def getRuleIndex(self):
            return SlrParser.RULE_summarize

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSummarize" ):
                listener.enterSummarize(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSummarize" ):
                listener.exitSummarize(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSummarize" ):
                return visitor.visitSummarize(self)
            else:
                return visitor.visitChildren(self)




    def summarize(self):

        localctx = SlrParser.SummarizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_summarize)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(SlrParser.T__12)
            self.state = 140
            self.match(SlrParser.LCB)
            self.state = 141
            self.optional_nl()
            self.state = 142
            self.method()
            self.state = 143
            self.maxLength()
            self.state = 144
            self.match(SlrParser.RCB)
            self.state = 145
            self.mandatory_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def METHID(self):
            return self.getToken(SlrParser.METHID, 0)

        def mandatory_nl(self):
            return self.getTypedRuleContext(SlrParser.Mandatory_nlContext,0)


        def getRuleIndex(self):
            return SlrParser.RULE_method

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod" ):
                listener.enterMethod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod" ):
                listener.exitMethod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = SlrParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(SlrParser.T__13)
            self.state = 148
            self.match(SlrParser.METHID)
            self.state = 149
            self.mandatory_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MaxLengthContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(SlrParser.NUMBER, 0)

        def mandatory_nl(self):
            return self.getTypedRuleContext(SlrParser.Mandatory_nlContext,0)


        def getRuleIndex(self):
            return SlrParser.RULE_maxLength

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMaxLength" ):
                listener.enterMaxLength(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMaxLength" ):
                listener.exitMaxLength(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMaxLength" ):
                return visitor.visitMaxLength(self)
            else:
                return visitor.visitChildren(self)




    def maxLength(self):

        localctx = SlrParser.MaxLengthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_maxLength)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(SlrParser.T__14)
            self.state = 152
            self.match(SlrParser.NUMBER)
            self.state = 153
            self.mandatory_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExtractFieldsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(SlrParser.LB, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(SlrParser.STRING)
            else:
                return self.getToken(SlrParser.STRING, i)

        def RB(self):
            return self.getToken(SlrParser.RB, 0)

        def mandatory_nl(self):
            return self.getTypedRuleContext(SlrParser.Mandatory_nlContext,0)


        def getRuleIndex(self):
            return SlrParser.RULE_extractFields

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtractFields" ):
                listener.enterExtractFields(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtractFields" ):
                listener.exitExtractFields(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtractFields" ):
                return visitor.visitExtractFields(self)
            else:
                return visitor.visitChildren(self)




    def extractFields(self):

        localctx = SlrParser.ExtractFieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_extractFields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(SlrParser.T__15)
            self.state = 156
            self.match(SlrParser.LB)
            self.state = 157
            self.match(SlrParser.STRING)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 158
                self.match(SlrParser.T__3)
                self.state = 159
                self.match(SlrParser.STRING)
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 165
            self.match(SlrParser.RB)
            self.state = 166
            self.mandatory_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeywordCloudContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(SlrParser.BOOLEAN, 0)

        def mandatory_nl(self):
            return self.getTypedRuleContext(SlrParser.Mandatory_nlContext,0)


        def getRuleIndex(self):
            return SlrParser.RULE_keywordCloud

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeywordCloud" ):
                listener.enterKeywordCloud(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeywordCloud" ):
                listener.exitKeywordCloud(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeywordCloud" ):
                return visitor.visitKeywordCloud(self)
            else:
                return visitor.visitChildren(self)




    def keywordCloud(self):

        localctx = SlrParser.KeywordCloudContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_keywordCloud)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(SlrParser.T__16)
            self.state = 169
            self.match(SlrParser.BOOLEAN)
            self.state = 170
            self.mandatory_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReportContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(SlrParser.LCB, 0)

        def optional_nl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SlrParser.Optional_nlContext)
            else:
                return self.getTypedRuleContext(SlrParser.Optional_nlContext,i)


        def format_(self):
            return self.getTypedRuleContext(SlrParser.FormatContext,0)


        def includeMetadata(self):
            return self.getTypedRuleContext(SlrParser.IncludeMetadataContext,0)


        def outputPath(self):
            return self.getTypedRuleContext(SlrParser.OutputPathContext,0)


        def RCB(self):
            return self.getToken(SlrParser.RCB, 0)

        def getRuleIndex(self):
            return SlrParser.RULE_report

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReport" ):
                listener.enterReport(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReport" ):
                listener.exitReport(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReport" ):
                return visitor.visitReport(self)
            else:
                return visitor.visitChildren(self)




    def report(self):

        localctx = SlrParser.ReportContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_report)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(SlrParser.T__17)
            self.state = 173
            self.match(SlrParser.LCB)
            self.state = 174
            self.optional_nl()
            self.state = 175
            self.format_()
            self.state = 176
            self.includeMetadata()
            self.state = 177
            self.outputPath()
            self.state = 178
            self.match(SlrParser.RCB)
            self.state = 179
            self.optional_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FORMAT(self):
            return self.getToken(SlrParser.FORMAT, 0)

        def mandatory_nl(self):
            return self.getTypedRuleContext(SlrParser.Mandatory_nlContext,0)


        def getRuleIndex(self):
            return SlrParser.RULE_format

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormat" ):
                listener.enterFormat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormat" ):
                listener.exitFormat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormat" ):
                return visitor.visitFormat(self)
            else:
                return visitor.visitChildren(self)




    def format_(self):

        localctx = SlrParser.FormatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_format)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(SlrParser.T__18)
            self.state = 182
            self.match(SlrParser.FORMAT)
            self.state = 183
            self.mandatory_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncludeMetadataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(SlrParser.BOOLEAN, 0)

        def mandatory_nl(self):
            return self.getTypedRuleContext(SlrParser.Mandatory_nlContext,0)


        def getRuleIndex(self):
            return SlrParser.RULE_includeMetadata

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncludeMetadata" ):
                listener.enterIncludeMetadata(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncludeMetadata" ):
                listener.exitIncludeMetadata(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncludeMetadata" ):
                return visitor.visitIncludeMetadata(self)
            else:
                return visitor.visitChildren(self)




    def includeMetadata(self):

        localctx = SlrParser.IncludeMetadataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_includeMetadata)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(SlrParser.T__19)
            self.state = 186
            self.match(SlrParser.BOOLEAN)
            self.state = 187
            self.mandatory_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputPathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(SlrParser.STRING, 0)

        def mandatory_nl(self):
            return self.getTypedRuleContext(SlrParser.Mandatory_nlContext,0)


        def getRuleIndex(self):
            return SlrParser.RULE_outputPath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutputPath" ):
                listener.enterOutputPath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutputPath" ):
                listener.exitOutputPath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutputPath" ):
                return visitor.visitOutputPath(self)
            else:
                return visitor.visitChildren(self)




    def outputPath(self):

        localctx = SlrParser.OutputPathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_outputPath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(SlrParser.T__20)
            self.state = 190
            self.match(SlrParser.STRING)
            self.state = 191
            self.mandatory_nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_nlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(SlrParser.NEWLINE)
            else:
                return self.getToken(SlrParser.NEWLINE, i)

        def getRuleIndex(self):
            return SlrParser.RULE_optional_nl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptional_nl" ):
                listener.enterOptional_nl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptional_nl" ):
                listener.exitOptional_nl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_nl" ):
                return visitor.visitOptional_nl(self)
            else:
                return visitor.visitChildren(self)




    def optional_nl(self):

        localctx = SlrParser.Optional_nlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_optional_nl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 193
                self.match(SlrParser.NEWLINE)
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mandatory_nlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(SlrParser.NEWLINE)
            else:
                return self.getToken(SlrParser.NEWLINE, i)

        def getRuleIndex(self):
            return SlrParser.RULE_mandatory_nl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMandatory_nl" ):
                listener.enterMandatory_nl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMandatory_nl" ):
                listener.exitMandatory_nl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMandatory_nl" ):
                return visitor.visitMandatory_nl(self)
            else:
                return visitor.visitChildren(self)




    def mandatory_nl(self):

        localctx = SlrParser.Mandatory_nlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_mandatory_nl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 199
                self.match(SlrParser.NEWLINE)
                self.state = 202 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==34):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





