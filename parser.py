from antlr4 import *
from grammar.ShonqolListener import ShonqolListener
from grammar.ShonqolLexer import ShonqolLexer
from grammar.ShonqolParser import ShonqolParser
import json

# from ast_builder import ASTBuilder
# from interpreter import Interpreter
# from ast_nodes import Program, Assignment, Literal, Identifier, FunctionCall
from ast_def import Program, Assignment, Literal, Identifier, FunctionCall, ASTBuilder

def extract_function_calls_from_ast(ast):
    """
    Recursively traverse the AST (represented as nested dictionaries)
    and extract all function calls, evaluating `concat()` calls when possible.
    """
    calls = []

    def process_argument(arg_node):
        """Process a single AST node that is an argument."""
        if isinstance(arg_node, dict):
            node_type = arg_node.get("type")

            if node_type == "Literal":
                return arg_node.get("value")

            elif node_type == "FunctionCall":
                return process_function_call(arg_node)

            elif node_type == "Arguments":
                # Process expressions within an Arguments node
                exprs = arg_node.get("expressions", [])
                return [process_argument(expr) for expr in exprs]

        return arg_node  # Fallback: return as-is

    def process_function_call(node):
        """Extract function call details from a FunctionCall node."""
        func_name = node.get("func_name")
        args_node = node.get("arguments", {})

        # Handle different argument storage formats
        if isinstance(args_node, dict) and args_node.get("type") == "Arguments":
            exprs = args_node.get("expressions", [])
        elif isinstance(args_node, list):  # If it's already a list
            exprs = args_node
        else:
            exprs = []

        # Process each expression in the arguments
        arg_values = [process_argument(expr) for expr in exprs]

        # Evaluate `concat()` immediately if all arguments are literals
        if func_name == "concat" and all(isinstance(arg, str) for arg in arg_values):
            return "".join(arg_values)

        return {"name": func_name, "arguments": arg_values}

    def traverse(node):
        """Traverse the AST and collect function calls."""
        if isinstance(node, dict):
            if node.get("type") == "FunctionCall":
                calls.append(process_function_call(node))

            for key, value in node.items():  # Recursively process all values
                traverse(value)

        elif isinstance(node, list):
            for item in node:
                traverse(item)

    traverse(ast)
    return calls

def parse(code):
    # Create an input stream from the DSL code.
    input_stream = InputStream(code)

    # Instantiate the lexer and token stream.
    lexer = ShonqolLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Instantiate the parser and get the parse tree.
    parser = ShonqolParser(token_stream)
    tree = parser.program()

    # Create the evaluation listener and walk the parse tree.
    listener = ShonqolListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    # At this point, the listener has updated the AST with evaluated values,
    # e.g., static evaluation for concat.
    # Print the extracted function calls from the AST.
    extracted = extract_function_calls_from_ast(tree.ast)
    # print(tree.ast)
    print("Extracted function calls from AST:")
    json_obj=json.dumps(extracted, indent=4)
    print(json_obj)

    return json.loads(json_obj)

if __name__ == "__main__":
    parse()
