from teo.lexer.lexer import Lexer, Token, TokenTypes
import pytest


def test_empty() -> None:
    source: str = ""
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    expected: list = []
    
    assert tokens == expected
    

def test_eof() -> None:
    source = "123"

    lexer = Lexer(source)
    tokens = lexer.tokenize()

    assert tokens[-1] == Token(TokenTypes.EOF, "")


def test_console_log() -> None:
    source: str = "console_log 123"
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)

    expected: list = [
        Token(TokenTypes.CONSOLE_LOG, "console_log"),
        Token(TokenTypes.NUMBER, "123")
    ]
    
    assert tokens == expected


def test_numbers() -> None:
    source: str = "123 12.3"
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)

    expected: list = [
        Token(TokenTypes.NUMBER, "123"),
        Token(TokenTypes.NUMBER, "12.3")
    ]
    
    assert tokens == expected


def test_invalid_numbers1() -> None:
    source: str = "."
    
    lexer: Lexer = Lexer(source)
    
    with pytest.raises(SyntaxError):
        lexer.tokenize()
        

def test_invalid_numbers2() -> None:
    source: str = "5."
    
    lexer: Lexer = Lexer(source)
    
    with pytest.raises(SyntaxError):
        lexer.tokenize()


def test_invalid_numbers3() -> None:
    source: str = ".2"
    
    lexer: Lexer = Lexer(source)
        
    with pytest.raises(SyntaxError):
        lexer.tokenize()
        

def test_invalid_numbers4() -> None:
    source: str = "1.2.3"
    
    lexer: Lexer = Lexer(source)
        
    with pytest.raises(SyntaxError):
        lexer.tokenize()


def test_bool() -> None:
    source: str = "true false"
    
    lexer: Lexer = Lexer(source)        
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    expected = [
        Token(TokenTypes.BOOLEAN, "true"),
        Token(TokenTypes.BOOLEAN, "false"),
    ]
    
    assert tokens == expected


def test_invalid_bool() -> None:
    source: str = "truefalse"
    
    lexer: Lexer = Lexer(source)        
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    unexpected = [
        Token(TokenTypes.BOOLEAN, "true"),
        Token(TokenTypes.BOOLEAN, "false"),
    ]
    
    assert tokens != unexpected


def test_equal_assign() -> None:
    source: str = "= =="
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    expected: list = [
        Token(TokenTypes.ASSIGN, "="),
        Token(TokenTypes.EQUAL, "==")
    ]
    
    assert tokens == expected


def test_identifier() -> None:
    source: str = "abc test123 var2a_"

    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    expected: list = [
        Token(TokenTypes.IDENTIFIER, "abc"),
        Token(TokenTypes.IDENTIFIER, "test123"),
        Token(TokenTypes.IDENTIFIER, "var2a_")
    ]
    
    assert tokens == expected


def test_multiply() -> None:
    source: str = "* **"
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    expected: list = [
        Token(TokenTypes.MULTIPLY, "*"),
        Token(TokenTypes.MULTIPLY, "*"),
        Token(TokenTypes.MULTIPLY, "*")
    ]
    
    assert tokens == expected


def test_divide() -> None:
    source: str = "/ //"
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    expected: list = [
        Token(TokenTypes.DIVIDE, "/"),
        Token(TokenTypes.DIVIDE, "/"),
        Token(TokenTypes.DIVIDE, "/")
    ]
    
    assert tokens == expected


def test_plus() -> None:
    source: str = "+ ++"
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    expected: list = [
        Token(TokenTypes.PLUS, "+"),
        Token(TokenTypes.PLUS, "+"),
        Token(TokenTypes.PLUS, "+")
    ]
    
    assert tokens == expected


def test_minus() -> None:
    source: str = "- --"
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    expected: list = [
        Token(TokenTypes.MINUS, "-"),
        Token(TokenTypes.MINUS, "-"),
        Token(TokenTypes.MINUS, "-")
    ]
    
    assert tokens == expected


def test_semicolon() -> None:
    source: str = "; ;;"
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    expected: list = [
        Token(TokenTypes.SEMICOLON, ";"),
        Token(TokenTypes.SEMICOLON, ";"),
        Token(TokenTypes.SEMICOLON, ";")
    ]
    
    assert tokens == expected


def test_newline() -> None:
    source: str = """
    
    \n"""
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    expected: list = [
        Token(TokenTypes.NEWLINE, "\n"),
        Token(TokenTypes.NEWLINE, "\n"),
        Token(TokenTypes.NEWLINE, "\n")
    ]
    
    assert tokens == expected


def test_skip() -> None:
    source: str = "     \t"
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    expected: list = [
    ]
    
    assert tokens == expected


def test_missmatch1() -> None:
    source: str = "_abcd"
    
    lexer: Lexer = Lexer(source)

    with pytest.raises(SyntaxError):
        lexer.tokenize()


def test_invalid_equal_assign1() -> None:
    source: str = "==="
    
    lexer: Lexer = Lexer(source)

    with pytest.raises(SyntaxError):
        lexer.tokenize()


def test_invalid_equal_assign2() -> None:
    source: str = "===="
    
    lexer: Lexer = Lexer(source)

    with pytest.raises(SyntaxError):
        lexer.tokenize()


def test_invalid_console_log1() -> None:
    source: str = "console_log123"
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    expected: list = [
        Token(TokenTypes.IDENTIFIER, "console_log123")
    ]
    
    assert tokens == expected


def test_invalid_console_log2() -> None:
    source: str = "abconsole_log"
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    expected: list = [
        Token(TokenTypes.IDENTIFIER, "abconsole_log")
    ]
    
    assert tokens == expected


def test_parens() -> None:
    source: str = "a(b)s"
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    expected: list = [
        Token(TokenTypes.IDENTIFIER, "a"),
        Token(TokenTypes.L_PARENS, "("),
        Token(TokenTypes.IDENTIFIER, "b"),
        Token(TokenTypes.R_PARENS, ")"),
        Token(TokenTypes.IDENTIFIER, "s")
    ]
    
    assert tokens == expected
    

def test_comparations() -> None:
    source: str = "a == b a > b a < b a >= b a <= b a != b"
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    expected: list = [
        Token(TokenTypes.IDENTIFIER, "a"),
        Token(TokenTypes.EQUAL, "=="),
        Token(TokenTypes.IDENTIFIER, "b"),
        Token(TokenTypes.IDENTIFIER, "a"),
        Token(TokenTypes.GREATER, ">"),
        Token(TokenTypes.IDENTIFIER, "b"),
        Token(TokenTypes.IDENTIFIER, "a"),
        Token(TokenTypes.LESS, "<"),
        Token(TokenTypes.IDENTIFIER, "b"),
        Token(TokenTypes.IDENTIFIER, "a"),
        Token(TokenTypes.GREATER_EQUAL, ">="),
        Token(TokenTypes.IDENTIFIER, "b"),
        Token(TokenTypes.IDENTIFIER, "a"),
        Token(TokenTypes.LESS_EQUAL, "<="),
        Token(TokenTypes.IDENTIFIER, "b"),
        Token(TokenTypes.IDENTIFIER, "a"),
        Token(TokenTypes.NOT_EQUAL, "!="),
        Token(TokenTypes.IDENTIFIER, "b")
    ]
    
    assert tokens == expected
