# Generated from ./grammar/Shonqol.g4 by ANTLR 4.13.2
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
        4,1,15,104,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,3,
        3,43,8,3,1,4,1,4,1,4,3,4,48,8,4,1,4,1,4,3,4,52,8,4,1,5,1,5,1,5,5,
        5,57,8,5,10,5,12,5,60,9,5,1,6,1,6,3,6,64,8,6,1,6,1,6,1,7,1,7,1,7,
        1,7,3,7,72,8,7,1,8,1,8,1,8,1,8,5,8,78,8,8,10,8,12,8,81,9,8,3,8,83,
        8,8,1,8,1,8,1,9,1,9,1,9,1,9,5,9,91,8,9,10,9,12,9,94,9,9,3,9,96,8,
        9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,
        18,20,0,1,1,0,11,12,107,0,25,1,0,0,0,2,32,1,0,0,0,4,34,1,0,0,0,6,
        42,1,0,0,0,8,44,1,0,0,0,10,53,1,0,0,0,12,63,1,0,0,0,14,71,1,0,0,
        0,16,73,1,0,0,0,18,86,1,0,0,0,20,99,1,0,0,0,22,24,3,2,1,0,23,22,
        1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,28,1,0,0,0,
        27,25,1,0,0,0,28,29,5,0,0,1,29,1,1,0,0,0,30,33,3,4,2,0,31,33,3,8,
        4,0,32,30,1,0,0,0,32,31,1,0,0,0,33,3,1,0,0,0,34,35,5,11,0,0,35,36,
        5,1,0,0,36,37,3,6,3,0,37,38,5,2,0,0,38,5,1,0,0,0,39,43,3,14,7,0,
        40,43,5,11,0,0,41,43,3,8,4,0,42,39,1,0,0,0,42,40,1,0,0,0,42,41,1,
        0,0,0,43,7,1,0,0,0,44,45,5,11,0,0,45,47,5,3,0,0,46,48,3,10,5,0,47,
        46,1,0,0,0,47,48,1,0,0,0,48,49,1,0,0,0,49,51,5,4,0,0,50,52,5,2,0,
        0,51,50,1,0,0,0,51,52,1,0,0,0,52,9,1,0,0,0,53,58,3,12,6,0,54,55,
        5,5,0,0,55,57,3,12,6,0,56,54,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,
        58,59,1,0,0,0,59,11,1,0,0,0,60,58,1,0,0,0,61,62,5,11,0,0,62,64,5,
        1,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,65,1,0,0,0,65,66,3,6,3,0,66,
        13,1,0,0,0,67,72,5,13,0,0,68,72,5,12,0,0,69,72,3,16,8,0,70,72,3,
        18,9,0,71,67,1,0,0,0,71,68,1,0,0,0,71,69,1,0,0,0,71,70,1,0,0,0,72,
        15,1,0,0,0,73,82,5,6,0,0,74,79,3,14,7,0,75,76,5,5,0,0,76,78,3,14,
        7,0,77,75,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,83,
        1,0,0,0,81,79,1,0,0,0,82,74,1,0,0,0,82,83,1,0,0,0,83,84,1,0,0,0,
        84,85,5,7,0,0,85,17,1,0,0,0,86,95,5,8,0,0,87,92,3,20,10,0,88,89,
        5,5,0,0,89,91,3,20,10,0,90,88,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,
        0,92,93,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,95,87,1,0,0,0,95,96,
        1,0,0,0,96,97,1,0,0,0,97,98,5,9,0,0,98,19,1,0,0,0,99,100,7,0,0,0,
        100,101,5,10,0,0,101,102,3,6,3,0,102,21,1,0,0,0,12,25,32,42,47,51,
        58,63,71,79,82,92,95
    ]

class ShonqolParser ( Parser ):

    grammarFileName = "Shonqol.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'('", "')'", "','", "'['", 
                     "']'", "'{'", "'}'", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "Identifier", 
                      "STRING", "NUMBER", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_expression = 3
    RULE_functionCall = 4
    RULE_arguments = 5
    RULE_argument = 6
    RULE_literal = 7
    RULE_array = 8
    RULE_dictionary = 9
    RULE_keyValuePair = 10

    ruleNames =  [ "program", "statement", "assignment", "expression", "functionCall", 
                   "arguments", "argument", "literal", "array", "dictionary", 
                   "keyValuePair" ]

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
    Identifier=11
    STRING=12
    NUMBER=13
    WS=14
    COMMENT=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ShonqolParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShonqolParser.StatementContext)
            else:
                return self.getTypedRuleContext(ShonqolParser.StatementContext,i)


        def getRuleIndex(self):
            return ShonqolParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ShonqolParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 22
                self.statement()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(ShonqolParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(ShonqolParser.AssignmentContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(ShonqolParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return ShonqolParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ShonqolParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(ShonqolParser.Identifier, 0)

        def expression(self):
            return self.getTypedRuleContext(ShonqolParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ShonqolParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = ShonqolParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(ShonqolParser.Identifier)
            self.state = 35
            self.match(ShonqolParser.T__0)
            self.state = 36
            self.expression()
            self.state = 37
            self.match(ShonqolParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(ShonqolParser.LiteralContext,0)


        def Identifier(self):
            return self.getToken(ShonqolParser.Identifier, 0)

        def functionCall(self):
            return self.getTypedRuleContext(ShonqolParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return ShonqolParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ShonqolParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expression)
        try:
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.match(ShonqolParser.Identifier)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(ShonqolParser.Identifier, 0)

        def arguments(self):
            return self.getTypedRuleContext(ShonqolParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return ShonqolParser.RULE_functionCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = ShonqolParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(ShonqolParser.Identifier)
            self.state = 45
            self.match(ShonqolParser.T__2)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14656) != 0):
                self.state = 46
                self.arguments()


            self.state = 49
            self.match(ShonqolParser.T__3)
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 50
                self.match(ShonqolParser.T__1)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShonqolParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(ShonqolParser.ArgumentContext,i)


        def getRuleIndex(self):
            return ShonqolParser.RULE_arguments

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = ShonqolParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.argument()
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 54
                self.match(ShonqolParser.T__4)
                self.state = 55
                self.argument()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ShonqolParser.ExpressionContext,0)


        def Identifier(self):
            return self.getToken(ShonqolParser.Identifier, 0)

        def getRuleIndex(self):
            return ShonqolParser.RULE_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = ShonqolParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 61
                self.match(ShonqolParser.Identifier)
                self.state = 62
                self.match(ShonqolParser.T__0)


            self.state = 65
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ShonqolParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ShonqolParser.STRING, 0)

        def array(self):
            return self.getTypedRuleContext(ShonqolParser.ArrayContext,0)


        def dictionary(self):
            return self.getTypedRuleContext(ShonqolParser.DictionaryContext,0)


        def getRuleIndex(self):
            return ShonqolParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ShonqolParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_literal)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.match(ShonqolParser.NUMBER)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.match(ShonqolParser.STRING)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 69
                self.array()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 70
                self.dictionary()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShonqolParser.LiteralContext)
            else:
                return self.getTypedRuleContext(ShonqolParser.LiteralContext,i)


        def getRuleIndex(self):
            return ShonqolParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = ShonqolParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(ShonqolParser.T__5)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 12608) != 0):
                self.state = 74
                self.literal()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 75
                    self.match(ShonqolParser.T__4)
                    self.state = 76
                    self.literal()
                    self.state = 81
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 84
            self.match(ShonqolParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DictionaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyValuePair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShonqolParser.KeyValuePairContext)
            else:
                return self.getTypedRuleContext(ShonqolParser.KeyValuePairContext,i)


        def getRuleIndex(self):
            return ShonqolParser.RULE_dictionary

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDictionary" ):
                return visitor.visitDictionary(self)
            else:
                return visitor.visitChildren(self)




    def dictionary(self):

        localctx = ShonqolParser.DictionaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_dictionary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(ShonqolParser.T__7)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11 or _la==12:
                self.state = 87
                self.keyValuePair()
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 88
                    self.match(ShonqolParser.T__4)
                    self.state = 89
                    self.keyValuePair()
                    self.state = 94
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 97
            self.match(ShonqolParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyValuePairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ShonqolParser.ExpressionContext,0)


        def STRING(self):
            return self.getToken(ShonqolParser.STRING, 0)

        def Identifier(self):
            return self.getToken(ShonqolParser.Identifier, 0)

        def getRuleIndex(self):
            return ShonqolParser.RULE_keyValuePair

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyValuePair" ):
                return visitor.visitKeyValuePair(self)
            else:
                return visitor.visitChildren(self)




    def keyValuePair(self):

        localctx = ShonqolParser.KeyValuePairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_keyValuePair)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 100
            self.match(ShonqolParser.T__9)
            self.state = 101
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





