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
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, Identifier=11, STRING=12, NUMBER=13, WS=14, COMMENT=15;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "Identifier", "STRING", "NUMBER", "WS", "COMMENT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'='", "';'", "'('", "')'", "','", "'['", "']'", "'{'", "'}'", 
			"':'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, "Identifier", 
			"STRING", "NUMBER", "WS", "COMMENT"
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
		"\u0004\u0000\u000fn\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0001"+
		"\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001"+
		"\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001"+
		"\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001"+
		"\t\u0001\n\u0001\n\u0005\n6\b\n\n\n\f\n9\t\n\u0001\u000b\u0001\u000b\u0005"+
		"\u000b=\b\u000b\n\u000b\f\u000b@\t\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0005\u000bE\b\u000b\n\u000b\f\u000bH\t\u000b\u0001\u000b\u0003"+
		"\u000bK\b\u000b\u0001\f\u0003\fN\b\f\u0001\f\u0004\fQ\b\f\u000b\f\f\f"+
		"R\u0001\f\u0001\f\u0004\fW\b\f\u000b\f\f\fX\u0003\f[\b\f\u0001\r\u0004"+
		"\r^\b\r\u000b\r\f\r_\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0005\u000eh\b\u000e\n\u000e\f\u000ek\t\u000e\u0001\u000e"+
		"\u0001\u000e\u0000\u0000\u000f\u0001\u0001\u0003\u0002\u0005\u0003\u0007"+
		"\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b"+
		"\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u0001\u0000\b\u0003\u0000AZ_"+
		"_az\u0005\u0000..09AZ__az\u0003\u0000\n\n\r\r\"\"\u0003\u0000\n\n\r\r"+
		"\'\'\u0002\u0000++--\u0001\u000009\u0003\u0000\t\n\r\r  \u0002\u0000\n"+
		"\n\r\rw\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000"+
		"\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000"+
		"\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000"+
		"\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000"+
		"\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000"+
		"\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000"+
		"\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000"+
		"\u001d\u0001\u0000\u0000\u0000\u0001\u001f\u0001\u0000\u0000\u0000\u0003"+
		"!\u0001\u0000\u0000\u0000\u0005#\u0001\u0000\u0000\u0000\u0007%\u0001"+
		"\u0000\u0000\u0000\t\'\u0001\u0000\u0000\u0000\u000b)\u0001\u0000\u0000"+
		"\u0000\r+\u0001\u0000\u0000\u0000\u000f-\u0001\u0000\u0000\u0000\u0011"+
		"/\u0001\u0000\u0000\u0000\u00131\u0001\u0000\u0000\u0000\u00153\u0001"+
		"\u0000\u0000\u0000\u0017J\u0001\u0000\u0000\u0000\u0019M\u0001\u0000\u0000"+
		"\u0000\u001b]\u0001\u0000\u0000\u0000\u001dc\u0001\u0000\u0000\u0000\u001f"+
		" \u0005=\u0000\u0000 \u0002\u0001\u0000\u0000\u0000!\"\u0005;\u0000\u0000"+
		"\"\u0004\u0001\u0000\u0000\u0000#$\u0005(\u0000\u0000$\u0006\u0001\u0000"+
		"\u0000\u0000%&\u0005)\u0000\u0000&\b\u0001\u0000\u0000\u0000\'(\u0005"+
		",\u0000\u0000(\n\u0001\u0000\u0000\u0000)*\u0005[\u0000\u0000*\f\u0001"+
		"\u0000\u0000\u0000+,\u0005]\u0000\u0000,\u000e\u0001\u0000\u0000\u0000"+
		"-.\u0005{\u0000\u0000.\u0010\u0001\u0000\u0000\u0000/0\u0005}\u0000\u0000"+
		"0\u0012\u0001\u0000\u0000\u000012\u0005:\u0000\u00002\u0014\u0001\u0000"+
		"\u0000\u000037\u0007\u0000\u0000\u000046\u0007\u0001\u0000\u000054\u0001"+
		"\u0000\u0000\u000069\u0001\u0000\u0000\u000075\u0001\u0000\u0000\u0000"+
		"78\u0001\u0000\u0000\u00008\u0016\u0001\u0000\u0000\u000097\u0001\u0000"+
		"\u0000\u0000:>\u0005\"\u0000\u0000;=\b\u0002\u0000\u0000<;\u0001\u0000"+
		"\u0000\u0000=@\u0001\u0000\u0000\u0000><\u0001\u0000\u0000\u0000>?\u0001"+
		"\u0000\u0000\u0000?A\u0001\u0000\u0000\u0000@>\u0001\u0000\u0000\u0000"+
		"AK\u0005\"\u0000\u0000BF\u0005\'\u0000\u0000CE\b\u0003\u0000\u0000DC\u0001"+
		"\u0000\u0000\u0000EH\u0001\u0000\u0000\u0000FD\u0001\u0000\u0000\u0000"+
		"FG\u0001\u0000\u0000\u0000GI\u0001\u0000\u0000\u0000HF\u0001\u0000\u0000"+
		"\u0000IK\u0005\'\u0000\u0000J:\u0001\u0000\u0000\u0000JB\u0001\u0000\u0000"+
		"\u0000K\u0018\u0001\u0000\u0000\u0000LN\u0007\u0004\u0000\u0000ML\u0001"+
		"\u0000\u0000\u0000MN\u0001\u0000\u0000\u0000NP\u0001\u0000\u0000\u0000"+
		"OQ\u0007\u0005\u0000\u0000PO\u0001\u0000\u0000\u0000QR\u0001\u0000\u0000"+
		"\u0000RP\u0001\u0000\u0000\u0000RS\u0001\u0000\u0000\u0000SZ\u0001\u0000"+
		"\u0000\u0000TV\u0005.\u0000\u0000UW\u0007\u0005\u0000\u0000VU\u0001\u0000"+
		"\u0000\u0000WX\u0001\u0000\u0000\u0000XV\u0001\u0000\u0000\u0000XY\u0001"+
		"\u0000\u0000\u0000Y[\u0001\u0000\u0000\u0000ZT\u0001\u0000\u0000\u0000"+
		"Z[\u0001\u0000\u0000\u0000[\u001a\u0001\u0000\u0000\u0000\\^\u0007\u0006"+
		"\u0000\u0000]\\\u0001\u0000\u0000\u0000^_\u0001\u0000\u0000\u0000_]\u0001"+
		"\u0000\u0000\u0000_`\u0001\u0000\u0000\u0000`a\u0001\u0000\u0000\u0000"+
		"ab\u0006\r\u0000\u0000b\u001c\u0001\u0000\u0000\u0000cd\u0005/\u0000\u0000"+
		"de\u0005/\u0000\u0000ei\u0001\u0000\u0000\u0000fh\b\u0007\u0000\u0000"+
		"gf\u0001\u0000\u0000\u0000hk\u0001\u0000\u0000\u0000ig\u0001\u0000\u0000"+
		"\u0000ij\u0001\u0000\u0000\u0000jl\u0001\u0000\u0000\u0000ki\u0001\u0000"+
		"\u0000\u0000lm\u0006\u000e\u0000\u0000m\u001e\u0001\u0000\u0000\u0000"+
		"\u000b\u00007>FJMRXZ_i\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}