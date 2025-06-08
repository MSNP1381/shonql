# Shonqol

Shonqol is a custom Domain-Specific Language (DSL) designed for tool interaction and automation. It provides a structured, expressive syntax for calling functions, managing variables, and composing results in a clear and readable way.

## Overview

Shonqol (pronounced "shon-kol") is built using ANTLR 4 and generates parsers for both Python and Java. The language is designed to bridge the gap between natural language queries and programmatic tool execution, making it ideal for automation scripts, data processing pipelines, and AI-assisted workflows.

## Language Features

### Core Syntax

- **Variable Assignment**: Store values in variables using `=`
- **Function Calls**: Call tools/functions with arguments
- **Literals**: Support for strings, numbers, arrays, and dictionaries
- **Comments**: C-style single-line comments with `//`

### Data Types

- **Numbers**: `42`, `-3.14`, `+100`
- **Strings**: `"hello"` or `'world'`
- **Arrays**: `[1, 2, 3]`, `["a", "b", "c"]`
- **Dictionaries**: `{name: "John", age: 30}`

## Syntax Examples

### Basic Variable Assignment

```shonqol
x = 42;
name = "John";
```

### Function Calls

```shonqol
result = add(5, 3);
greeting = makeGreeting("John");
print(greeting);
```

### Complex Expressions

```shonqol
// Nested function calls
result = add(
    multiply(getValue(), 2),
    subtract(10, 5)
);

// String concatenation
fullName = concat(firstName, concat(" ", lastName));
```

### Arrays and Dictionaries

```shonqol
numbers = [1, 2, 3, 4, 5];
person = {
    name: "Alice",
    age: 30,
    email: "alice@example.com"
};
```

## Grammar Definition

The language is defined in `grammar/Shonqol.g4` using ANTLR 4 syntax. Key grammar rules include:

- **Program**: A sequence of statements
- **Statement**: Assignment or function call
- **Expression**: Literal, variable reference, or function call
- **Literal**: Number, string, array, or dictionary

## Project Structure

```text
shonql/
├── grammar/
│   ├── Shonqol.g4                 # ANTLR grammar definition
│   ├── ShonqolParser.py           # Generated Python parser
│   ├── ShonqolLexer.py            # Generated Python lexer
│   ├── ShonqolListener.py         # Generated listener (with evaluation)
│   └── ShonqolVisitor.py          # Generated visitor
├── examples.py                    # Usage examples
├── prompts.py                     # Main language prompt/documentation
├── main.ipynb                     # Jupyter notebook for development
├── requirements.txt               # Python dependencies
├── setup.py                       # Setup utilities
└── README.md                      # This file
```

## Installation

### Prerequisites

- Python 3.7+
- ANTLR 4.13.2

### Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Key dependencies include:

- `antlr4-python3-runtime==4.13.2`
- `aiohttp` for async HTTP operations
- `black` for code formatting
- Various other packages for extended functionality

### Building the Parser

If you need to regenerate the parser from the grammar:

```bash
# Install ANTLR 4 (if not already installed)
# Then generate Python files from grammar
antlr4 -Dlanguage=Python3 grammar/Shonqol.g4 -o grammar/
```

## Usage

### Parsing Shonqol Code

```python
from antlr4 import *
from grammar.ShonqolLexer import ShonqolLexer
from grammar.ShonqolParser import ShonqolParser
from grammar.ShonqolListener import ShonqolListener

# Parse Shonqol code
code = '''
x = 42;
result = add(x, 8);
print(result);
'''

# Create lexer and parser
input_stream = InputStream(code)
lexer = ShonqolLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = ShonqolParser(stream)

# Parse and evaluate
tree = parser.program()
listener = ShonqolListener()
walker = ParseTreeWalker()
walker.walk(listener, tree)
```

### Interactive Development

Use the Jupyter notebook `main.ipynb` for interactive development and testing:

```bash
jupyter notebook main.ipynb
```

## Language Design Philosophy

Shonqol is designed with several key principles:

1. **Simplicity**: Clean, readable syntax that's easy to learn
2. **Tool-Oriented**: Optimized for function/tool calling patterns
3. **Composability**: Easy to combine results from multiple operations
4. **Structured**: Enforces good practices through syntax
5. **Extensible**: Easy to add new functions and data types

## Important Notes

- **No Attribute Access**: The language intentionally doesn't support attribute access (e.g., `obj.property`)
- **Statement Termination**: Most statements end with semicolons
- **Function-First**: Designed around function calls rather than object methods
- **Immutable Results**: Function results are treated as values, not objects

## Examples

See `examples.py` for comprehensive usage examples, including:

- Basic variable assignments
- Function composition
- Complex data structures
- Conditional logic patterns

## Contributing

When contributing to Shonqol:

1. Modify the grammar in `grammar/Shonqol.g4`
2. Regenerate parser files using ANTLR
3. Update examples and tests
4. Ensure compatibility with both Python and Java targets


## Development Status

This project is actively developed for tool interaction and automation use cases. The core language features are stable, with ongoing enhancements for better tool integration and performance.
