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
        4,1,12,80,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,3,1,29,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,3,3,39,8,3,1,4,1,4,
        1,4,3,4,44,8,4,1,4,1,4,1,5,1,5,1,5,5,5,51,8,5,10,5,12,5,54,9,5,1,
        6,1,6,3,6,58,8,6,1,6,1,6,1,7,1,7,1,7,3,7,65,8,7,1,8,1,8,1,8,1,8,
        5,8,71,8,8,10,8,12,8,74,9,8,3,8,76,8,8,1,8,1,8,1,8,0,0,9,0,2,4,6,
        8,10,12,14,16,0,0,81,0,21,1,0,0,0,2,28,1,0,0,0,4,30,1,0,0,0,6,38,
        1,0,0,0,8,40,1,0,0,0,10,47,1,0,0,0,12,57,1,0,0,0,14,64,1,0,0,0,16,
        66,1,0,0,0,18,20,3,2,1,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,
        0,21,22,1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,24,25,5,0,0,1,25,1,1,
        0,0,0,26,29,3,4,2,0,27,29,3,8,4,0,28,26,1,0,0,0,28,27,1,0,0,0,29,
        3,1,0,0,0,30,31,5,8,0,0,31,32,5,1,0,0,32,33,3,6,3,0,33,34,5,2,0,
        0,34,5,1,0,0,0,35,39,3,14,7,0,36,39,5,8,0,0,37,39,3,8,4,0,38,35,
        1,0,0,0,38,36,1,0,0,0,38,37,1,0,0,0,39,7,1,0,0,0,40,41,5,8,0,0,41,
        43,5,3,0,0,42,44,3,10,5,0,43,42,1,0,0,0,43,44,1,0,0,0,44,45,1,0,
        0,0,45,46,5,4,0,0,46,9,1,0,0,0,47,52,3,12,6,0,48,49,5,5,0,0,49,51,
        3,12,6,0,50,48,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,
        53,11,1,0,0,0,54,52,1,0,0,0,55,56,5,8,0,0,56,58,5,1,0,0,57,55,1,
        0,0,0,57,58,1,0,0,0,58,59,1,0,0,0,59,60,3,6,3,0,60,13,1,0,0,0,61,
        65,5,10,0,0,62,65,5,9,0,0,63,65,3,16,8,0,64,61,1,0,0,0,64,62,1,0,
        0,0,64,63,1,0,0,0,65,15,1,0,0,0,66,75,5,6,0,0,67,72,3,14,7,0,68,
        69,5,5,0,0,69,71,3,14,7,0,70,68,1,0,0,0,71,74,1,0,0,0,72,70,1,0,
        0,0,72,73,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,75,67,1,0,0,0,75,76,
        1,0,0,0,76,77,1,0,0,0,77,78,5,7,0,0,78,17,1,0,0,0,9,21,28,38,43,
        52,57,64,72,75
    ]

class ShonqolParser ( Parser ):

    grammarFileName = "Shonqol.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'('", "')'", "','", "'['", 
                     "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Identifier", "STRING", "NUMBER", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_expression = 3
    RULE_functionCall = 4
    RULE_arguments = 5
    RULE_argument = 6
    RULE_literal = 7
    RULE_array = 8

    ruleNames =  [ "program", "statement", "assignment", "expression", "functionCall", 
                   "arguments", "argument", "literal", "array" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    Identifier=8
    STRING=9
    NUMBER=10
    WS=11
    COMMENT=12

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

        localctx = ShonqolParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 18
                self.statement()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ShonqolParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

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
            self.state = 30
            self.match(ShonqolParser.Identifier)
            self.state = 31
            self.match(ShonqolParser.T__0)
            self.state = 32
            self.expression()
            self.state = 33
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ShonqolParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expression)
        try:
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.match(ShonqolParser.Identifier)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

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
            self.state = 40
            self.match(ShonqolParser.Identifier)
            self.state = 41
            self.match(ShonqolParser.T__2)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1856) != 0):
                self.state = 42
                self.arguments()


            self.state = 45
            self.match(ShonqolParser.T__3)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)

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
            self.state = 47
            self.argument()
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 48
                self.match(ShonqolParser.T__4)
                self.state = 49
                self.argument()
                self.state = 54
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)

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
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 55
                self.match(ShonqolParser.Identifier)
                self.state = 56
                self.match(ShonqolParser.T__0)


            self.state = 59
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


        def getRuleIndex(self):
            return ShonqolParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ShonqolParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_literal)
        try:
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.match(ShonqolParser.NUMBER)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(ShonqolParser.STRING)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 63
                self.array()
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)

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
            self.state = 66
            self.match(ShonqolParser.T__5)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1600) != 0):
                self.state = 67
                self.literal()
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 68
                    self.match(ShonqolParser.T__4)
                    self.state = 69
                    self.literal()
                    self.state = 74
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 77
            self.match(ShonqolParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





