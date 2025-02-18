# Modified ShonqolListener.py with evaluation and AST building.
from antlr4 import *
if "." in __name__:
    from .ShonqolParser import ShonqolParser
else:
    from ShonqolParser import ShonqolParser

class ShonqolListener(ParseTreeListener):
    def __init__(self):
        # Environment to store variable assignments.
        self.env = {}

    # --- Program ---
    def enterProgram(self, ctx: ShonqolParser.ProgramContext):
        pass

    def exitProgram(self, ctx: ShonqolParser.ProgramContext):
        # Build AST for the program by collecting the AST of all statements.
        ctx.ast = {
            "type": "Program",
            "statements": [stmt.ast for stmt in ctx.statement()]
        }
        ctx.value = self.env  # Attach the final environment

    # --- Statement ---
    def enterStatement(self, ctx: ShonqolParser.StatementContext):
        pass

    def exitStatement(self, ctx: ShonqolParser.StatementContext):
        # Assume the statement is an assignment.
        # Its AST is the AST of its first (and only) child.
        ctx.ast = ctx.getChild(0).ast

    # --- Assignment ---
    def enterAssignment(self, ctx: ShonqolParser.AssignmentContext):
        pass

    def exitAssignment(self, ctx: ShonqolParser.AssignmentContext):
        var_name = ctx.Identifier().getText()
        expr_value = ctx.expression().value
        self.env[var_name] = expr_value
        ctx.value = expr_value
        ctx.ast = {
            "type": "Assignment",
            "var_name": var_name,
            "expression": ctx.expression().ast
        }

    # --- Expression ---
    def enterExpression(self, ctx: ShonqolParser.ExpressionContext):
        pass

    def exitExpression(self, ctx: ShonqolParser.ExpressionContext):
        # Expression can be a literal, a function call, or an identifier.
        if ctx.literal():
            ctx.value = ctx.literal().value
            ctx.ast = ctx.literal().ast
        elif ctx.functionCall():
            ctx.value = ctx.functionCall().value
            ctx.ast = ctx.functionCall().ast
        elif ctx.Identifier():
            identifier = ctx.Identifier().getText()
            # For evaluation, look up the identifier in the environment.
            ctx.value = self.env.get(identifier, None)
            ctx.ast = {
                "type": "Identifier",
                "name": identifier
            }

    # --- Function Call ---
    def enterFunctionCall(self, ctx: ShonqolParser.FunctionCallContext):
        pass

    def exitFunctionCall(self, ctx: ShonqolParser.FunctionCallContext):
        func_name = ctx.Identifier().getText()
        args_value = []
        args_ast = []
        if ctx.arguments():
            args_value = ctx.arguments().value
            args_ast = ctx.arguments().ast
        if func_name == "concat":
            # Static evaluation: join the arguments (expected to be strings)
            result = "".join(str(arg) for arg in args_value)
            ctx.value = result
        else:
            # Placeholder evaluation for other functions.
            result = f"{func_name}({', '.join(map(str, args_value))})"
            ctx.value = result
        ctx.ast = {
            "type": "FunctionCall",
            "func_name": func_name,
            "arguments": args_ast
        }

    # --- Arguments ---
    def enterArguments(self, ctx: ShonqolParser.ArgumentsContext):
        pass

    def exitArguments(self, ctx: ShonqolParser.ArgumentsContext):
        values = [expr.value for expr in ctx.expression()]
        asts = [expr.ast for expr in ctx.expression()]
        ctx.value = values
        ctx.ast = {
            "type": "Arguments",
            "expressions": asts
        }

    # --- Literal ---
    def enterLiteral(self, ctx: ShonqolParser.LiteralContext):
        pass

    def exitLiteral(self, ctx: ShonqolParser.LiteralContext):
        if ctx.NUMBER():
            num_text = ctx.NUMBER().getText()
            if '.' in num_text:
                val = float(num_text)
            else:
                val = int(num_text)
            ctx.value = val
            ctx.ast = {
                "type": "Literal",
                "value": val
            }
        elif ctx.STRING():
            text = ctx.STRING().getText()[1:-1]  # remove quotes
            ctx.value = text
            ctx.ast = {
                "type": "Literal",
                "value": text
            }
        else:
            ctx.value = None
            ctx.ast = {"type": "Literal", "value": None}

del ShonqolParser
