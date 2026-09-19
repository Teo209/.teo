from teo.sourcespan.sourcespan import SourceSpan, SourcePosition
from teo.errors.lexer import TeoLexerError
from enum import Enum, auto
import re


class TokenTypes(Enum):
    CONSOLE_LOG = auto()    # console_log
    NUMBER = auto()         # number
    L_PARENS = auto()       # ()
    R_PARENS = auto()       # )
    BOOLEAN = auto()       # true / false
    VAR = auto()            # define local variable
    IDENTIFIER = auto()     # variable name
    EQUAL = auto()          # equality ==
    NOT_EQUAL = auto()      # !=
    LESS = auto()           # <
    GREATER = auto()        # >
    LESS_EQUAL = auto()     # <=
    GREATER_EQUAL = auto()  # >=
    ASSIGN = auto()         # =
    MULTIPLY = auto()       # *
    DIVIDE = auto()         # /
    PLUS = auto()           # +
    MINUS = auto()          # -
    SEMICOLON = auto()      # end of instruction ;
    NEWLINE = auto()        # new line \n (enter)
    SKIP = auto()           # white space
    MISMATCH = auto()       # other characters
    EOF = auto()            # end of file, always last token


TOKEN_RULES = [
    (TokenTypes.CONSOLE_LOG,        r"console_log\b"                ),
    (TokenTypes.NUMBER,             r"\d+(\.\d+)?"                  ),
    (TokenTypes.R_PARENS,           r"\)"                           ),
    (TokenTypes.L_PARENS,           r"\("                           ),
    (TokenTypes.BOOLEAN,            r"(true\b)|(false\b)"           ),
    (TokenTypes.VAR,                r"var\b"                        ),
    (TokenTypes.IDENTIFIER,         r"[a-zA-Z]\w*"                  ),
    (TokenTypes.MISMATCH,           r"={3,}"                        ),         # don't confuse === or more with == =
    (TokenTypes.EQUAL,              r"=="                           ),
    (TokenTypes.NOT_EQUAL,          r"!="                           ),
    (TokenTypes.LESS_EQUAL,         r"<="                           ),
    (TokenTypes.GREATER_EQUAL,      r">="                           ),
    (TokenTypes.LESS,               r"<"                            ),
    (TokenTypes.GREATER,            r">"                            ),
    (TokenTypes.ASSIGN,             r"="                            ),
    (TokenTypes.MULTIPLY,           r"\*"                           ),
    (TokenTypes.DIVIDE,             r"/"                            ),
    (TokenTypes.PLUS,               r"\+"                           ),
    (TokenTypes.MINUS,              r"-"                            ),
    (TokenTypes.SEMICOLON,          r";"                            ),
    (TokenTypes.NEWLINE,            r"\n"                           ),
    (TokenTypes.SKIP,               r"[ \t]+"                       ),
    (TokenTypes.MISMATCH,           r"."                            )          # other mismatches
]


class Token():
    def __init__(self, type: TokenTypes, value: str, span: SourceSpan = None):
        self.type = type
        self.value = value
        self.span = span
        
    
    def __repr__(self) -> str:
        return f"Token (type: {self.type.name}; value: {repr(self.value)}; span: [{self.span})]\n"


    def __eq__(self, other) -> bool:
        if not isinstance(other, Token):
            return NotImplemented

        return (
            self.type == other.type and
            self.value == other.value
        )


class Lexer():
    def __init__(self, source: str) -> None:
        self.source = source
    

    def tokenize(self) -> list[Token]:
        # "(?P<nume>regex)"
        
        token_regex = "|".join(f"(?P<TOKEN_{i}>{rule[1]})" for i, rule in enumerate(TOKEN_RULES))
        
        #print(self.token_regex)
        
        token_list = []
        curent_line = 1
        current_column = 0
        
        for match in re.finditer(token_regex, self.source):
            
            group_name = match.lastgroup
            group_value = match.group(group_name)
        
            # print("group:", group_name, "\nvalue:", group_value, "\n")
            
            rule_index = int(group_name.removeprefix("TOKEN_"))
            token_type = TOKEN_RULES[rule_index][0]
            
            if token_type == TokenTypes.SKIP:
                current_column += len(group_value)
                continue
            
            
            else:
                span = SourceSpan(
                    SourcePosition(curent_line, current_column), 
                    SourcePosition(curent_line, current_column + len(group_value))
                )
                
                current_column += len(group_value)
                
                if token_type == TokenTypes.MISMATCH:
                    raise TeoLexerError(f"\nInvalid character \'{group_value}\'", span)
                
                if token_type == TokenTypes.NEWLINE: 
                    curent_line += 1
                    current_column = 0
                
                new_token = Token(token_type, group_value, span)
                token_list.append(new_token)
                

        token_list.append(
            Token(
                TokenTypes.EOF, 
                "",
                SourceSpan(
                    SourcePosition(curent_line, current_column),
                    SourcePosition(curent_line, current_column)
                    )
                )
            )
            
        return token_list
