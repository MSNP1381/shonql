// Generated from c:/Users/msnp/Documents/GitHub/shonql/grammar/Shonqol.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class ShonqolLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, Identifier=8, 
		STRING=9, NUMBER=10, WS=11, COMMENT=12;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "Identifier", 
			"STRING", "NUMBER", "WS", "COMMENT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'='", "';'", "'('", "')'", "','", "'['", "']'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, "Identifier", "STRING", 
			"NUMBER", "WS", "COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public ShonqolLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Shonqol.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\fb\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0005\u0007"+
		"*\b\u0007\n\u0007\f\u0007-\t\u0007\u0001\b\u0001\b\u0005\b1\b\b\n\b\f"+
		"\b4\t\b\u0001\b\u0001\b\u0001\b\u0005\b9\b\b\n\b\f\b<\t\b\u0001\b\u0003"+
		"\b?\b\b\u0001\t\u0003\tB\b\t\u0001\t\u0004\tE\b\t\u000b\t\f\tF\u0001\t"+
		"\u0001\t\u0004\tK\b\t\u000b\t\f\tL\u0003\tO\b\t\u0001\n\u0004\nR\b\n\u000b"+
		"\n\f\nS\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0005\u000b\\\b\u000b\n\u000b\f\u000b_\t\u000b\u0001\u000b\u0001\u000b"+
		"\u0000\u0000\f\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005"+
		"\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0001"+
		"\u0000\b\u0003\u0000AZ__az\u0004\u000009AZ__az\u0003\u0000\n\n\r\r\"\""+
		"\u0003\u0000\n\n\r\r\'\'\u0002\u0000++--\u0001\u000009\u0003\u0000\t\n"+
		"\r\r  \u0002\u0000\n\n\r\rk\u0000\u0001\u0001\u0000\u0000\u0000\u0000"+
		"\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000"+
		"\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b"+
		"\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001"+
		"\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001"+
		"\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001"+
		"\u0000\u0000\u0000\u0001\u0019\u0001\u0000\u0000\u0000\u0003\u001b\u0001"+
		"\u0000\u0000\u0000\u0005\u001d\u0001\u0000\u0000\u0000\u0007\u001f\u0001"+
		"\u0000\u0000\u0000\t!\u0001\u0000\u0000\u0000\u000b#\u0001\u0000\u0000"+
		"\u0000\r%\u0001\u0000\u0000\u0000\u000f\'\u0001\u0000\u0000\u0000\u0011"+
		">\u0001\u0000\u0000\u0000\u0013A\u0001\u0000\u0000\u0000\u0015Q\u0001"+
		"\u0000\u0000\u0000\u0017W\u0001\u0000\u0000\u0000\u0019\u001a\u0005=\u0000"+
		"\u0000\u001a\u0002\u0001\u0000\u0000\u0000\u001b\u001c\u0005;\u0000\u0000"+
		"\u001c\u0004\u0001\u0000\u0000\u0000\u001d\u001e\u0005(\u0000\u0000\u001e"+
		"\u0006\u0001\u0000\u0000\u0000\u001f \u0005)\u0000\u0000 \b\u0001\u0000"+
		"\u0000\u0000!\"\u0005,\u0000\u0000\"\n\u0001\u0000\u0000\u0000#$\u0005"+
		"[\u0000\u0000$\f\u0001\u0000\u0000\u0000%&\u0005]\u0000\u0000&\u000e\u0001"+
		"\u0000\u0000\u0000\'+\u0007\u0000\u0000\u0000(*\u0007\u0001\u0000\u0000"+
		")(\u0001\u0000\u0000\u0000*-\u0001\u0000\u0000\u0000+)\u0001\u0000\u0000"+
		"\u0000+,\u0001\u0000\u0000\u0000,\u0010\u0001\u0000\u0000\u0000-+\u0001"+
		"\u0000\u0000\u0000.2\u0005\"\u0000\u0000/1\b\u0002\u0000\u00000/\u0001"+
		"\u0000\u0000\u000014\u0001\u0000\u0000\u000020\u0001\u0000\u0000\u0000"+
		"23\u0001\u0000\u0000\u000035\u0001\u0000\u0000\u000042\u0001\u0000\u0000"+
		"\u00005?\u0005\"\u0000\u00006:\u0005\'\u0000\u000079\b\u0003\u0000\u0000"+
		"87\u0001\u0000\u0000\u00009<\u0001\u0000\u0000\u0000:8\u0001\u0000\u0000"+
		"\u0000:;\u0001\u0000\u0000\u0000;=\u0001\u0000\u0000\u0000<:\u0001\u0000"+
		"\u0000\u0000=?\u0005\'\u0000\u0000>.\u0001\u0000\u0000\u0000>6\u0001\u0000"+
		"\u0000\u0000?\u0012\u0001\u0000\u0000\u0000@B\u0007\u0004\u0000\u0000"+
		"A@\u0001\u0000\u0000\u0000AB\u0001\u0000\u0000\u0000BD\u0001\u0000\u0000"+
		"\u0000CE\u0007\u0005\u0000\u0000DC\u0001\u0000\u0000\u0000EF\u0001\u0000"+
		"\u0000\u0000FD\u0001\u0000\u0000\u0000FG\u0001\u0000\u0000\u0000GN\u0001"+
		"\u0000\u0000\u0000HJ\u0005.\u0000\u0000IK\u0007\u0005\u0000\u0000JI\u0001"+
		"\u0000\u0000\u0000KL\u0001\u0000\u0000\u0000LJ\u0001\u0000\u0000\u0000"+
		"LM\u0001\u0000\u0000\u0000MO\u0001\u0000\u0000\u0000NH\u0001\u0000\u0000"+
		"\u0000NO\u0001\u0000\u0000\u0000O\u0014\u0001\u0000\u0000\u0000PR\u0007"+
		"\u0006\u0000\u0000QP\u0001\u0000\u0000\u0000RS\u0001\u0000\u0000\u0000"+
		"SQ\u0001\u0000\u0000\u0000ST\u0001\u0000\u0000\u0000TU\u0001\u0000\u0000"+
		"\u0000UV\u0006\n\u0000\u0000V\u0016\u0001\u0000\u0000\u0000WX\u0005/\u0000"+
		"\u0000XY\u0005/\u0000\u0000Y]\u0001\u0000\u0000\u0000Z\\\b\u0007\u0000"+
		"\u0000[Z\u0001\u0000\u0000\u0000\\_\u0001\u0000\u0000\u0000][\u0001\u0000"+
		"\u0000\u0000]^\u0001\u0000\u0000\u0000^`\u0001\u0000\u0000\u0000_]\u0001"+
		"\u0000\u0000\u0000`a\u0006\u000b\u0000\u0000a\u0018\u0001\u0000\u0000"+
		"\u0000\u000b\u0000+2:>AFLNS]\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}