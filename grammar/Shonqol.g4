grammar Shonqol;

// The entry point for the parser.
program: statement* EOF;

// Every statement is an assignment.
statement: assignment| functionCall;

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
arguments: expression (',' expression)*;

// Literals: numbers or strings.

// Lexer rules
Identifier: [a-zA-Z_][a-zA-Z0-9_]*;

literal: STRING | NUMBER;

STRING: '"' (~["\r\n])* '"';
NUMBER: [+-]? [0-9]+ ('.' [0-9]+)?;
// Skip whitespace.
WS: [ \t\r\n]+ -> skip;