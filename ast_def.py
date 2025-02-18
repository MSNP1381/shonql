import json
from antlr4 import *
from grammar.ShonqolParser import ShonqolParser
from grammar.ShonqolVisitor import ShonqolVisitor

# === AST Node Definitions ===

class ASTNode:
    pass

class Program(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class Assignment(ASTNode):
    def __init__(self, var_name, expression):
        self.var_name = var_name
        self.expression = expression

class Literal(ASTNode):
    def __init__(self, value):
        self.value = value

class Identifier(ASTNode):
    def __init__(self, name):
        self.name = name

class FunctionCall(ASTNode):
    def __init__(self, func_name, arguments):
        self.func_name = func_name
        self.arguments = arguments

# === AST Builder using the Visitor Pattern ===

class ASTBuilder(ShonqolVisitor):
    def visitProgram(self, ctx:ShonqolParser.ProgramContext):
        statements = [self.visit(stmt) for stmt in ctx.statement()]
        return Program(statements)
    
    def visitAssignment(self, ctx:ShonqolParser.AssignmentContext):
        var_name = ctx.Identifier().getText()
        expr = self.visit(ctx.expression())
        return Assignment(var_name, expr)
    
    def visitFunctionCall(self, ctx:ShonqolParser.FunctionCallContext):
        func_name = ctx.Identifier().getText()
        args = []
        if ctx.arguments():
            args = self.visit(ctx.arguments())
        return FunctionCall(func_name, args)
    
    def visitArguments(self, ctx:ShonqolParser.ArgumentsContext):
        return [self.visit(expr) for expr in ctx.expression()]
    
    def visitLiteral(self, ctx:ShonqolParser.LiteralContext):
        if ctx.Number():
            return Literal(int(ctx.Number().getText()))
        elif ctx.String():
            # Remove the surrounding quotes
            text = ctx.String().getText()
            return Literal(text[1:-1])
        return None
    
    def visitExpression(self, ctx:ShonqolParser.ExpressionContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())
        elif ctx.Identifier():
            return Identifier(ctx.Identifier().getText())
        else:
            return None
