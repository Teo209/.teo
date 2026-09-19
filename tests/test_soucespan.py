from teo.lexer.lexer import Lexer, TokenTypes
from teo.sourcespan.sourcespan import SourceSpan, SourcePosition
import pytest


def test_simple():
    source = "123"
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    tokens.pop(-1)
    
    span = list(map(lambda token: token.span, tokens))
    
    expected = [
        SourceSpan(SourcePosition(1, 0), SourcePosition(1, 3))
    ]
    
    assert span == expected


def test_multiple():
    source = "123 + 321"
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    tokens.pop(-1)
    
    span = list(map(lambda token: token.span, tokens))
    
    expected = [
        SourceSpan(SourcePosition(1, 0), SourcePosition(1, 3)),
        SourceSpan(SourcePosition(1, 4), SourcePosition(1, 5)),
        SourceSpan(SourcePosition(1, 6), SourcePosition(1, 9))
    ]
    
    assert span == expected


def test_newline():
    source = "123\n456"
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    tokens.pop(-1)
    
    span = list(map(lambda token: token.span, tokens))
    
    expected = [
        SourceSpan(SourcePosition(1, 0), SourcePosition(1, 3)),
        SourceSpan(SourcePosition(1, 3), SourcePosition(1, 4)),
        SourceSpan(SourcePosition(2, 0), SourcePosition(2, 3))
    ]
    
    assert span == expected
   

def test_spaces():
    source = "   123"
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    tokens.pop(-1)
    
    span = list(map(lambda token: token.span, tokens))
    
    expected = [
        SourceSpan(SourcePosition(1, 3), SourcePosition(1, 6))
    ]
    
    assert span == expected
    

def test_mismatch():
    source = "123 @"
    
    lexer = Lexer(source)
    
    with pytest.raises(SyntaxError):
        tokens = lexer.tokenize()


def test_eof():
    source = "   123"
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    span = [
        tokens[-1].span
    ]
    
    expected = [
        SourceSpan(SourcePosition(1, 6), SourcePosition(1, 6))
    ]
    
    assert span == expected