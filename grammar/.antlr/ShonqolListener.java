// Generated from c:/Users/msnp/Documents/GitHub/shonql/grammar/Shonqol.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ShonqolParser}.
 */
public interface ShonqolListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ShonqolParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(ShonqolParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShonqolParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(ShonqolParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShonqolParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(ShonqolParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShonqolParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(ShonqolParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShonqolParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(ShonqolParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShonqolParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(ShonqolParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShonqolParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(ShonqolParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShonqolParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(ShonqolParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShonqolParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCall(ShonqolParser.FunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShonqolParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCall(ShonqolParser.FunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShonqolParser#arguments}.
	 * @param ctx the parse tree
	 */
	void enterArguments(ShonqolParser.ArgumentsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShonqolParser#arguments}.
	 * @param ctx the parse tree
	 */
	void exitArguments(ShonqolParser.ArgumentsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShonqolParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(ShonqolParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShonqolParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(ShonqolParser.LiteralContext ctx);
}