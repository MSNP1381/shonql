grammar Shonqol;

// The entry point for the parser.
program: statement* EOF;

// Every statement is an assignment.
statement: assignment | functionCall;

// Assignment: Identifier '=' expression ';'
assignment: Identifier '=' expression ';';

// Expression can be a literal, a variable reference, or a function call.
expression:
	literal
	| Identifier // variable reference
	| functionCall;

// Function call with an optional argument list.
functionCall: Identifier '(' arguments? ')' ';'?;

// A comma-separated list of expressions.
arguments: argument (',' argument)*;
//ignore the argument rule for now like call(page=50) to call(50)
argument: (Identifier '=')? expression ;

// Literals: numbers or strings.

// Lexer rules
Identifier: [a-zA-Z_][a-zA-Z0-9_.]* ;

literal: NUMBER | STRING | array | dictionary;

STRING: '"' (~["\r\n])* '"' | '\'' (~['\r\n])* '\'';
NUMBER: [+-]? [0-9]+ ('.' [0-9]+)?;
// Update the literal rule to include array literals.

// Array literal: a comma‐separated list of expressions inside square brackets.
array: '[' (literal (',' literal)*)? ']';

// Dictionary literal: a comma‐separated list of key-value pairs inside curly braces.
dictionary: '{' (keyValuePair (',' keyValuePair)*)? '}';

// Key-value pair: a string or identifier followed by a colon and an expression.
keyValuePair: (STRING | Identifier) ':' expression;

// Skip whitespace.
WS: [ \t\r\n]+ -> skip;

// Comments
COMMENT: '//' ~[\r\n]* -> skip;