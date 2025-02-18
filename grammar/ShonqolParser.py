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
        4,1,9,54,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,1,1,1,1,3,1,25,8,1,1,2,1,
        2,1,2,1,2,1,2,1,3,1,3,1,3,3,3,35,8,3,1,4,1,4,1,4,3,4,40,8,4,1,4,
        1,4,1,5,1,5,1,5,5,5,47,8,5,10,5,12,5,50,9,5,1,6,1,6,1,6,0,0,7,0,
        2,4,6,8,10,12,0,1,1,0,7,8,52,0,17,1,0,0,0,2,24,1,0,0,0,4,26,1,0,
        0,0,6,34,1,0,0,0,8,36,1,0,0,0,10,43,1,0,0,0,12,51,1,0,0,0,14,16,
        3,2,1,0,15,14,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,
        18,20,1,0,0,0,19,17,1,0,0,0,20,21,5,0,0,1,21,1,1,0,0,0,22,25,3,4,
        2,0,23,25,3,8,4,0,24,22,1,0,0,0,24,23,1,0,0,0,25,3,1,0,0,0,26,27,
        5,6,0,0,27,28,5,1,0,0,28,29,3,6,3,0,29,30,5,2,0,0,30,5,1,0,0,0,31,
        35,3,12,6,0,32,35,5,6,0,0,33,35,3,8,4,0,34,31,1,0,0,0,34,32,1,0,
        0,0,34,33,1,0,0,0,35,7,1,0,0,0,36,37,5,6,0,0,37,39,5,3,0,0,38,40,
        3,10,5,0,39,38,1,0,0,0,39,40,1,0,0,0,40,41,1,0,0,0,41,42,5,4,0,0,
        42,9,1,0,0,0,43,48,3,6,3,0,44,45,5,5,0,0,45,47,3,6,3,0,46,44,1,0,
        0,0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,11,1,0,0,0,50,48,
        1,0,0,0,51,52,7,0,0,0,52,13,1,0,0,0,5,17,24,34,39,48
    ]

class ShonqolParser ( Parser ):

    grammarFileName = "Shonqol.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "Identifier", "STRING", 
                      "NUMBER", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_expression = 3
    RULE_functionCall = 4
    RULE_arguments = 5
    RULE_literal = 6

    ruleNames =  [ "program", "statement", "assignment", "expression", "functionCall", 
                   "arguments", "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    Identifier=6
    STRING=7
    NUMBER=8
    WS=9

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
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 14
                self.statement()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
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
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
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
            self.state = 26
            self.match(ShonqolParser.Identifier)
            self.state = 27
            self.match(ShonqolParser.T__0)
            self.state = 28
            self.expression()
            self.state = 29
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
            self.state = 34
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.match(ShonqolParser.Identifier)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 33
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
            self.state = 36
            self.match(ShonqolParser.Identifier)
            self.state = 37
            self.match(ShonqolParser.T__2)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0):
                self.state = 38
                self.arguments()


            self.state = 41
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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShonqolParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ShonqolParser.ExpressionContext,i)


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
            self.state = 43
            self.expression()
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 44
                self.match(ShonqolParser.T__4)
                self.state = 45
                self.expression()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def STRING(self):
            return self.getToken(ShonqolParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(ShonqolParser.NUMBER, 0)

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
        self.enterRule(localctx, 12, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





