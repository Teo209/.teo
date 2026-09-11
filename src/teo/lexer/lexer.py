from enum import Enum, auto
import re


class TokenTypes(Enum):
    NUMBER = auto()         # number
    IDENTIFIER = auto()     # variable name
    EQUAL = auto()          # equality ==
    ASSIGN = auto()         # =
    PLUS = auto()           # +
    MINUS = auto()          # -
    SEMICOLON = auto()      # end of instruction ;
    NEWLINE = auto()        # new line \n (enter)
    SKIP = auto()           # white space
    MISMATCH = auto()       # other


TOKEN_RULES = [
    (TokenTypes.NUMBER,      r"\d+"),
    (TokenTypes.IDENTIFIER,  r"[a-zA-Z]\w*"),
    (TokenTypes.MISMATCH,    r"={3,}"),         # don't confuse === or more with == =
    (TokenTypes.EQUAL,       r"=="),
    (TokenTypes.ASSIGN,      r"="),
    (TokenTypes.PLUS,        r"\+"),
    (TokenTypes.MINUS,       r"-"),
    (TokenTypes.SEMICOLON,   r";"),
    (TokenTypes.NEWLINE,     r"\n"),
    (TokenTypes.SKIP,        r"[ \t]+"),
    (TokenTypes.MISMATCH,    r".")              # other mismatches
]


class Token():
    def __init__(self, type: TokenTypes, value: str, line: int) -> None:
        self.type = type
        self.value = value
        self.line = line
        
    def __repr__(self) -> str:
        return f"Token (type: {self.type.name}; value: {repr(self.value)}; line: {self.line})\n"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Token):
            return NotImplemented

        return (
            self.type == other.type
            and self.value == other.value
            and self.line == other.line
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
        
        for match in re.finditer(token_regex, self.source):
            group_name = match.lastgroup
            group_value = match.group(group_name)
        
            # print("group:", group_name, "\nvalue:", group_value, "\n")
            
            rule_index = int(group_name.removeprefix("TOKEN_"))
            token_type = TOKEN_RULES[rule_index][0]
            
            if token_type == TokenTypes.SKIP: 
                continue
            if token_type == TokenTypes.MISMATCH:
                raise SyntaxError(f"Invalid character \'{group_value}\' at line {curent_line}")
            else:
                new_token = Token(token_type, group_value, curent_line)
                token_list.append(new_token)
                if token_type == TokenTypes.NEWLINE: curent_line += 1
            
        return token_list


if __name__ == "__main__":    
    # token = Token(type=TokenTypes.NUMBER, value="234", line=12)
    lexer = Lexer("var = 23; \naaa = 3 + var")
    tokens = lexer.tokenize()
    # print('\n', token)
    print('\n', tokens)
