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
functionCall: Identifier '(' arguments? ')';

// A comma-separated list of expressions.
arguments: argument (',' argument)*;
//ignore the argument rule for now like call(page=50) to call(50)
argument: (Identifier '=')? expression;

// Literals: numbers or strings.

// Lexer rules
Identifier: [a-zA-Z_][a-zA-Z0-9_]*;

literal: NUMBER | STRING | array;

STRING: '"' (~["\r\n])* '"' | '\'' (~['\r\n])* '\'';
NUMBER: [+-]? [0-9]+ ('.' [0-9]+)?;
// Update the literal rule to include array literals.

// Array literal: a comma‐separated list of expressions inside square brackets.
array: '[' (literal (',' literal)*)? ']';

// Skip whitespace.
WS: [ \t\r\n]+ -> skip;

// Comments
COMMENT: '//' ~[\r\n]* -> skip;