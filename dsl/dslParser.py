# Generated from dsl.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\27")
        buf.write("W\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\5\2\30\n\2\3\2\3\2")
        buf.write("\3\2\7\2\35\n\2\f\2\16\2 \13\2\3\3\3\3\3\4\3\4\3\4\3\4")
        buf.write("\7\4(\n\4\f\4\16\4+\13\4\3\4\3\4\3\5\3\5\3\5\5\5\62\n")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\7\69\n\6\f\6\16\6<\13\6\5\6>\n")
        buf.write("\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\7\bG\n\b\f\b\16\bJ\13\b")
        buf.write("\5\bL\n\b\3\t\3\t\3\n\3\n\3\n\5\nS\n\n\3\13\3\13\3\13")
        buf.write("\2\2\f\2\4\6\b\n\f\16\20\22\24\2\5\3\2\4\5\3\2\n\13\3")
        buf.write("\2\16\24V\2\27\3\2\2\2\4!\3\2\2\2\6#\3\2\2\2\b\61\3\2")
        buf.write("\2\2\n\63\3\2\2\2\f?\3\2\2\2\16A\3\2\2\2\20M\3\2\2\2\22")
        buf.write("O\3\2\2\2\24T\3\2\2\2\26\30\5\4\3\2\27\26\3\2\2\2\27\30")
        buf.write("\3\2\2\2\30\31\3\2\2\2\31\36\5\6\4\2\32\33\7\3\2\2\33")
        buf.write("\35\5\6\4\2\34\32\3\2\2\2\35 \3\2\2\2\36\34\3\2\2\2\36")
        buf.write("\37\3\2\2\2\37\3\3\2\2\2 \36\3\2\2\2!\"\t\2\2\2\"\5\3")
        buf.write("\2\2\2#$\7\25\2\2$)\5\b\5\2%&\7\6\2\2&(\5\b\5\2\'%\3\2")
        buf.write("\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*,\3\2\2\2+)\3\2\2")
        buf.write("\2,-\7\26\2\2-\7\3\2\2\2.\62\5\n\6\2/\62\5\16\b\2\60\62")
        buf.write("\5\22\n\2\61.\3\2\2\2\61/\3\2\2\2\61\60\3\2\2\2\62\t\3")
        buf.write("\2\2\2\63=\7\7\2\2\64\65\7\b\2\2\65:\5\f\7\2\66\67\7\t")
        buf.write("\2\2\679\5\f\7\28\66\3\2\2\29<\3\2\2\2:8\3\2\2\2:;\3\2")
        buf.write("\2\2;>\3\2\2\2<:\3\2\2\2=\64\3\2\2\2=>\3\2\2\2>\13\3\2")
        buf.write("\2\2?@\t\3\2\2@\r\3\2\2\2AK\7\f\2\2BC\7\b\2\2CH\5\20\t")
        buf.write("\2DE\7\t\2\2EG\5\20\t\2FD\3\2\2\2GJ\3\2\2\2HF\3\2\2\2")
        buf.write("HI\3\2\2\2IL\3\2\2\2JH\3\2\2\2KB\3\2\2\2KL\3\2\2\2L\17")
        buf.write("\3\2\2\2MN\t\3\2\2N\21\3\2\2\2OR\7\r\2\2PQ\7\b\2\2QS\5")
        buf.write("\24\13\2RP\3\2\2\2RS\3\2\2\2S\23\3\2\2\2TU\t\4\2\2U\25")
        buf.write("\3\2\2\2\13\27\36)\61:=HKR")
        return buf.getvalue()


class dslParser ( Parser ):

    grammarFileName = "dsl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'html'", "'pdf'", "','", "'g'", 
                     "'?'", "'|'", "'scale_log'", "'monthly'", "'t'", "'s'", 
                     "'count'", "'sum'", "'mean'", "'median'", "'min'", 
                     "'max'", "'std'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "TITLE", "TEXT", 
                      "WS" ]

    RULE_expression = 0
    RULE_output = 1
    RULE_command = 2
    RULE_operation = 3
    RULE_graph = 4
    RULE_graph_arg = 5
    RULE_table = 6
    RULE_table_arg = 7
    RULE_stats = 8
    RULE_stats_arg = 9

    ruleNames =  [ "expression", "output", "command", "operation", "graph", 
                   "graph_arg", "table", "table_arg", "stats", "stats_arg" ]

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
    TITLE=19
    TEXT=20
    WS=21

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dslParser.CommandContext)
            else:
                return self.getTypedRuleContext(dslParser.CommandContext,i)


        def output(self):
            return self.getTypedRuleContext(dslParser.OutputContext,0)


        def getRuleIndex(self):
            return dslParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = dslParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            _la = self._input.LA(1)
            if _la==dslParser.T__1 or _la==dslParser.T__2:
                self.state = 20
                self.output()


            self.state = 23
            self.command()
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==dslParser.T__0:
                self.state = 24
                self.match(dslParser.T__0)
                self.state = 25
                self.command()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OutputContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return dslParser.RULE_output

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutput" ):
                return visitor.visitOutput(self)
            else:
                return visitor.visitChildren(self)




    def output(self):

        localctx = dslParser.OutputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_output)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            _la = self._input.LA(1)
            if not(_la==dslParser.T__1 or _la==dslParser.T__2):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TITLE(self):
            return self.getToken(dslParser.TITLE, 0)

        def operation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dslParser.OperationContext)
            else:
                return self.getTypedRuleContext(dslParser.OperationContext,i)


        def TEXT(self):
            return self.getToken(dslParser.TEXT, 0)

        def getRuleIndex(self):
            return dslParser.RULE_command

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = dslParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(dslParser.TITLE)
            self.state = 34
            self.operation()
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==dslParser.T__3:
                self.state = 35
                self.match(dslParser.T__3)
                self.state = 36
                self.operation()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
            self.match(dslParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def graph(self):
            return self.getTypedRuleContext(dslParser.GraphContext,0)


        def table(self):
            return self.getTypedRuleContext(dslParser.TableContext,0)


        def stats(self):
            return self.getTypedRuleContext(dslParser.StatsContext,0)


        def getRuleIndex(self):
            return dslParser.RULE_operation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperation" ):
                return visitor.visitOperation(self)
            else:
                return visitor.visitChildren(self)




    def operation(self):

        localctx = dslParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_operation)
        try:
            self.state = 47
            token = self._input.LA(1)
            if token in [dslParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.graph()

            elif token in [dslParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.table()

            elif token in [dslParser.T__10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.stats()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GraphContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def graph_arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dslParser.Graph_argContext)
            else:
                return self.getTypedRuleContext(dslParser.Graph_argContext,i)


        def getRuleIndex(self):
            return dslParser.RULE_graph

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGraph" ):
                return visitor.visitGraph(self)
            else:
                return visitor.visitChildren(self)




    def graph(self):

        localctx = dslParser.GraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_graph)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(dslParser.T__4)
            self.state = 59
            _la = self._input.LA(1)
            if _la==dslParser.T__5:
                self.state = 50
                self.match(dslParser.T__5)
                self.state = 51
                self.graph_arg()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==dslParser.T__6:
                    self.state = 52
                    self.match(dslParser.T__6)
                    self.state = 53
                    self.graph_arg()
                    self.state = 58
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Graph_argContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return dslParser.RULE_graph_arg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGraph_arg" ):
                return visitor.visitGraph_arg(self)
            else:
                return visitor.visitChildren(self)




    def graph_arg(self):

        localctx = dslParser.Graph_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_graph_arg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            _la = self._input.LA(1)
            if not(_la==dslParser.T__7 or _la==dslParser.T__8):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def table_arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dslParser.Table_argContext)
            else:
                return self.getTypedRuleContext(dslParser.Table_argContext,i)


        def getRuleIndex(self):
            return dslParser.RULE_table

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTable" ):
                return visitor.visitTable(self)
            else:
                return visitor.visitChildren(self)




    def table(self):

        localctx = dslParser.TableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_table)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(dslParser.T__9)
            self.state = 73
            _la = self._input.LA(1)
            if _la==dslParser.T__5:
                self.state = 64
                self.match(dslParser.T__5)
                self.state = 65
                self.table_arg()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==dslParser.T__6:
                    self.state = 66
                    self.match(dslParser.T__6)
                    self.state = 67
                    self.table_arg()
                    self.state = 72
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Table_argContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return dslParser.RULE_table_arg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTable_arg" ):
                return visitor.visitTable_arg(self)
            else:
                return visitor.visitChildren(self)




    def table_arg(self):

        localctx = dslParser.Table_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_table_arg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            _la = self._input.LA(1)
            if not(_la==dslParser.T__7 or _la==dslParser.T__8):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stats_arg(self):
            return self.getTypedRuleContext(dslParser.Stats_argContext,0)


        def getRuleIndex(self):
            return dslParser.RULE_stats

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStats" ):
                return visitor.visitStats(self)
            else:
                return visitor.visitChildren(self)




    def stats(self):

        localctx = dslParser.StatsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_stats)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(dslParser.T__10)
            self.state = 80
            _la = self._input.LA(1)
            if _la==dslParser.T__5:
                self.state = 78
                self.match(dslParser.T__5)
                self.state = 79
                self.stats_arg()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Stats_argContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return dslParser.RULE_stats_arg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStats_arg" ):
                return visitor.visitStats_arg(self)
            else:
                return visitor.visitChildren(self)




    def stats_arg(self):

        localctx = dslParser.Stats_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_stats_arg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << dslParser.T__11) | (1 << dslParser.T__12) | (1 << dslParser.T__13) | (1 << dslParser.T__14) | (1 << dslParser.T__15) | (1 << dslParser.T__16) | (1 << dslParser.T__17))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





