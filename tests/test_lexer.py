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

    assert tokens[-1] == Token(TokenTypes.EOF, "", 2)


def test_console_log() -> None:
    source: str = "console_log 123"
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)

    expected: list = [
        Token(TokenTypes.CONSOLE_LOG, "console_log", 1),
        Token(TokenTypes.NUMBER, "123", 1)
    ]
    
    assert tokens == expected


def test_numbers() -> None:
    source: str = "123 12.3"
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)

    expected: list = [
        Token(TokenTypes.NUMBER, "123", 1),
        Token(TokenTypes.NUMBER, "12.3", 1)
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
        Token(TokenTypes.BOOLEAN, "true", 1),
        Token(TokenTypes.BOOLEAN, "false", 1),
    ]
    
    assert tokens == expected


def test_invalid_bool() -> None:
    source: str = "truefalse"
    
    lexer: Lexer = Lexer(source)        
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    unexpected = [
        Token(TokenTypes.BOOLEAN, "true", 1),
        Token(TokenTypes.BOOLEAN, "false", 1),
    ]
    
    assert tokens != unexpected


def test_equal_assign() -> None:
    source: str = "= =="
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    expected: list = [
        Token(TokenTypes.ASSIGN, "=", 1),
        Token(TokenTypes.EQUAL, "==", 1)
    ]
    
    assert tokens == expected


def test_identifier() -> None:
    source: str = "abc test123 var2a_"

    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    expected: list = [
        Token(TokenTypes.IDENTIFIER, "abc", 1),
        Token(TokenTypes.IDENTIFIER, "test123", 1),
        Token(TokenTypes.IDENTIFIER, "var2a_", 1)
    ]
    
    assert tokens == expected


def test_multiply() -> None:
    source: str = "* **"
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    expected: list = [
        Token(TokenTypes.MULTIPLY, "*", 1),
        Token(TokenTypes.MULTIPLY, "*", 1),
        Token(TokenTypes.MULTIPLY, "*", 1)
    ]
    
    assert tokens == expected


def test_divide() -> None:
    source: str = "/ //"
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    expected: list = [
        Token(TokenTypes.DIVIDE, "/", 1),
        Token(TokenTypes.DIVIDE, "/", 1),
        Token(TokenTypes.DIVIDE, "/", 1)
    ]
    
    assert tokens == expected


def test_plus() -> None:
    source: str = "+ ++"
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    expected: list = [
        Token(TokenTypes.PLUS, "+", 1),
        Token(TokenTypes.PLUS, "+", 1),
        Token(TokenTypes.PLUS, "+", 1)
    ]
    
    assert tokens == expected


def test_minus() -> None:
    source: str = "- --"
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    expected: list = [
        Token(TokenTypes.MINUS, "-", 1),
        Token(TokenTypes.MINUS, "-", 1),
        Token(TokenTypes.MINUS, "-", 1)
    ]
    
    assert tokens == expected


def test_semicolon() -> None:
    source: str = "; ;;"
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    expected: list = [
        Token(TokenTypes.SEMICOLON, ";", 1),
        Token(TokenTypes.SEMICOLON, ";", 1),
        Token(TokenTypes.SEMICOLON, ";", 1)
    ]
    
    assert tokens == expected


def test_newline() -> None:
    source: str = """
    
    \n"""
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    expected: list = [
        Token(TokenTypes.NEWLINE, "\n", 1),
        Token(TokenTypes.NEWLINE, "\n", 2),
        Token(TokenTypes.NEWLINE, "\n", 3)
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
        Token(TokenTypes.IDENTIFIER, "console_log123", 1)
    ]
    
    assert tokens == expected


def test_invalid_console_log2() -> None:
    source: str = "abconsole_log"
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    expected: list = [
        Token(TokenTypes.IDENTIFIER, "abconsole_log", 1)
    ]
    
    assert tokens == expected


def test_parens() -> None:
    source: str = "a(b)s"
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    expected: list = [
        Token(TokenTypes.IDENTIFIER, "a", 1),
        Token(TokenTypes.L_PARENS, "(", 1),
        Token(TokenTypes.IDENTIFIER, "b", 1),
        Token(TokenTypes.R_PARENS, ")", 1),
        Token(TokenTypes.IDENTIFIER, "s", 1)
    ]
    
    assert tokens == expected
    

def test_comparations() -> None:
    source: str = "a == b a > b a < b a >= b a <= b a != b"
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    tokens.pop(-1)
    
    expected: list = [
        Token(TokenTypes.IDENTIFIER, "a", 1),
        Token(TokenTypes.EQUAL, "==", 1),
        Token(TokenTypes.IDENTIFIER, "b", 1),
        Token(TokenTypes.IDENTIFIER, "a", 1),
        Token(TokenTypes.GREATER, ">", 1),
        Token(TokenTypes.IDENTIFIER, "b", 1),
        Token(TokenTypes.IDENTIFIER, "a", 1),
        Token(TokenTypes.LESS, "<", 1),
        Token(TokenTypes.IDENTIFIER, "b", 1),
        Token(TokenTypes.IDENTIFIER, "a", 1),
        Token(TokenTypes.GREATER_EQUAL, ">=", 1),
        Token(TokenTypes.IDENTIFIER, "b", 1),
        Token(TokenTypes.IDENTIFIER, "a", 1),
        Token(TokenTypes.LESS_EQUAL, "<=", 1),
        Token(TokenTypes.IDENTIFIER, "b", 1),
        Token(TokenTypes.IDENTIFIER, "a", 1),
        Token(TokenTypes.NOT_EQUAL, "!=", 1),
        Token(TokenTypes.IDENTIFIER, "b", 1)
    ]
    
    assert tokens == expected
