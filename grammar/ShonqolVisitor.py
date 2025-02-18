# Generated from ./grammar/Shonqol.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ShonqolParser import ShonqolParser
else:
    from ShonqolParser import ShonqolParser

# This class defines a complete generic visitor for a parse tree produced by ShonqolParser.

class ShonqolVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ShonqolParser#program.
    def visitProgram(self, ctx:ShonqolParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShonqolParser#statement.
    def visitStatement(self, ctx:ShonqolParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShonqolParser#assignment.
    def visitAssignment(self, ctx:ShonqolParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShonqolParser#expression.
    def visitExpression(self, ctx:ShonqolParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShonqolParser#functionCall.
    def visitFunctionCall(self, ctx:ShonqolParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShonqolParser#arguments.
    def visitArguments(self, ctx:ShonqolParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShonqolParser#literal.
    def visitLiteral(self, ctx:ShonqolParser.LiteralContext):
        return self.visitChildren(ctx)



del ShonqolParser