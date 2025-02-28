# Generated from ./grammar/Shonqol.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ShonqolParser import ShonqolParser
else:
    from ShonqolParser import ShonqolParser

# This class defines a complete listener for a parse tree produced by ShonqolParser.
class ShonqolListener(ParseTreeListener):

    # Enter a parse tree produced by ShonqolParser#program.
    def enterProgram(self, ctx:ShonqolParser.ProgramContext):
        pass

    # Exit a parse tree produced by ShonqolParser#program.
    def exitProgram(self, ctx:ShonqolParser.ProgramContext):
        pass


    # Enter a parse tree produced by ShonqolParser#statement.
    def enterStatement(self, ctx:ShonqolParser.StatementContext):
        pass

    # Exit a parse tree produced by ShonqolParser#statement.
    def exitStatement(self, ctx:ShonqolParser.StatementContext):
        pass


    # Enter a parse tree produced by ShonqolParser#assignment.
    def enterAssignment(self, ctx:ShonqolParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ShonqolParser#assignment.
    def exitAssignment(self, ctx:ShonqolParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ShonqolParser#expression.
    def enterExpression(self, ctx:ShonqolParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ShonqolParser#expression.
    def exitExpression(self, ctx:ShonqolParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ShonqolParser#functionCall.
    def enterFunctionCall(self, ctx:ShonqolParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by ShonqolParser#functionCall.
    def exitFunctionCall(self, ctx:ShonqolParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by ShonqolParser#arguments.
    def enterArguments(self, ctx:ShonqolParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by ShonqolParser#arguments.
    def exitArguments(self, ctx:ShonqolParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by ShonqolParser#argument.
    def enterArgument(self, ctx:ShonqolParser.ArgumentContext):
        pass

    # Exit a parse tree produced by ShonqolParser#argument.
    def exitArgument(self, ctx:ShonqolParser.ArgumentContext):
        pass


    # Enter a parse tree produced by ShonqolParser#literal.
    def enterLiteral(self, ctx:ShonqolParser.LiteralContext):
        pass

    # Exit a parse tree produced by ShonqolParser#literal.
    def exitLiteral(self, ctx:ShonqolParser.LiteralContext):
        pass


    # Enter a parse tree produced by ShonqolParser#array.
    def enterArray(self, ctx:ShonqolParser.ArrayContext):
        pass

    # Exit a parse tree produced by ShonqolParser#array.
    def exitArray(self, ctx:ShonqolParser.ArrayContext):
        pass



del ShonqolParser