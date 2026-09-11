from src.teo.lexer.lexer import Lexer, Token, TokenTypes
import pytest

def test_empty() -> None:
    source: str = ""
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    
    expected: list = []
    
    assert tokens == expected


def test_numbers() -> None:
    source: str = "123 907 921"
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()

    expected: list = [
        Token(TokenTypes.NUMBER, "123", 1),
        Token(TokenTypes.NUMBER, "907", 1),
        Token(TokenTypes.NUMBER, "921", 1),
    ]
    
    assert tokens == expected


def test_equal_assign() -> None:
    source: str = "= =="
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    
    expected: list = [
        Token(TokenTypes.ASSIGN, "=", 1),
        Token(TokenTypes.EQUAL, "==", 1),
    ]
    
    assert tokens == expected


def test_identifier() -> None:
    source: str = "abc test123 var2a_"

    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    
    expected: list = [
        Token(TokenTypes.IDENTIFIER, "abc", 1),
        Token(TokenTypes.IDENTIFIER, "test123", 1),
        Token(TokenTypes.IDENTIFIER, "var2a_", 1)
    ]
    
    assert tokens == expected


def test_plus() -> None:
    source: str = "+ ++"
    
    lexer: Lexer = Lexer(source)
    tokens: list[Token] = lexer.tokenize()
    
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
    
    expected: list = []
    
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