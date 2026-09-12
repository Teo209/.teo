from teo.parser.parser import Parser
from teo.lexer.lexer import Lexer
from teo.ast.expression import (
    Expression,
    Literal,
    Variable,
    BinaryOperation,
    UnaryOperation
)
from teo.ast.statement import (
    Statement,
    ExpressionStatement,
    Assign,
    ConsoleLog
)
import pytest


def test_empty():
    source: str = ""
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    expected: list = [
    ]
    
    assert ast == expected


def test_primary_expressions():
    source: str = """
    5
    42
    a
    """
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    expected: list = [
        ExpressionStatement(Literal(5)),
        ExpressionStatement(Literal(42)),
        ExpressionStatement(Variable("a"))
    ]
    
    assert ast == expected


def test_unary_operations():
    source: str = """
    -5
    +5
    --5
    -+5
    """
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    expected: list = [
        ExpressionStatement(
            UnaryOperation(
                "-", 
                Literal(5)
                )
            ),
        ExpressionStatement(
            UnaryOperation(
                "+", 
                Literal(5)
                )
            ),
        ExpressionStatement(
            UnaryOperation("-",
             UnaryOperation("-", 
             Literal(5)
                )
            )
        ),
        ExpressionStatement(
            UnaryOperation("-",
             UnaryOperation("+", 
             Literal(5)
                )
            )
        )
    ]
    
    assert ast == expected


def test_multiplication():
    source: str = "2 * 3"
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    expected: list = [
        ExpressionStatement(
            BinaryOperation(
                Literal(2),
                "*",
                Literal(3)
            )
        )
    ]
    
    assert ast == expected


def test_division():
    source: str = "10 / 2"
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    expected: list = [
        ExpressionStatement(
            BinaryOperation(
                Literal(10),
                "/",
                Literal(2)
            )
        )
    ]
    
    assert ast == expected


def test_multiplication_left_associativity():
    source: str = "2 * 3 * 4"
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    expected: list = [
        ExpressionStatement(
            BinaryOperation(
                BinaryOperation(
                    Literal(2),
                    "*",
                    Literal(3)
                ),
                "*",
                Literal(4)
            )
        )
    ]
    
    assert ast == expected


def test_addition():
    source: str = "2 + 3"
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    expected: list = [
        ExpressionStatement(
            BinaryOperation(
                Literal(2),
                "+",
                Literal(3)
            )
        )
    ]
    
    assert ast == expected


def test_subtraction():
    source: str = "10 - 4"
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    expected: list = [
        ExpressionStatement(
            BinaryOperation(
                Literal(10),
                "-",
                Literal(4)
            )
        )
    ]
    
    assert ast == expected


def test_addition_left_associativity():
    source: str = "10 - 3 - 2"
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    expected: list = [
        ExpressionStatement(
            BinaryOperation(
                BinaryOperation(
                    Literal(10),
                    "-",
                    Literal(3)
                ),
                "-",
                Literal(2)
            )
        )
    ]
    
    assert ast == expected


def test_operator_precedence():
    source: str = "2 + 3 * 4"
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    expected: list = [
        ExpressionStatement(
            BinaryOperation(
                Literal(2),
                "+",
                BinaryOperation(
                    Literal(3),
                    "*",
                    Literal(4)
                )
            )
        )
    ]
    
    assert ast == expected


def test_operator_precedence_reverse():
    source: str = "2 * 3 + 4"
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    expected: list = [
        ExpressionStatement(
            BinaryOperation(
                BinaryOperation(
                    Literal(2),
                    "*",
                    Literal(3)
                ),
                "+",
                Literal(4)
            )
        )
    ]
    
    assert ast == expected


def test_unary_precedence():
    source: str = "-5 * 2"
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    expected: list = [
        ExpressionStatement(
            BinaryOperation(
                UnaryOperation("-", Literal(5)),
                "*",
                Literal(2)
            )
        )
    ]
    
    assert ast == expected


def test_expression_statement():
    source: str = "a + 2"
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    expected: list = [
        ExpressionStatement(
            BinaryOperation(
                Variable("a"),
                "+",
                Literal(2)
            )
        )
    ]
    
    assert ast == expected


def test_assignment():
    source: str = "a = 5"
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    expected: list = [
        Assign(
            "a",
            Literal(5)
        )
    ]
    
    assert ast == expected


def test_assignment_expression():
    source: str = "a = 2 + 3 * 4"
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    expected: list = [
        Assign(
            "a",
            BinaryOperation(
                Literal(2),
                "+",
                BinaryOperation(
                    Literal(3),
                    "*",
                    Literal(4)
                )
            )
        )
    ]
    
    assert ast == expected


def test_assignment_unary():
    source: str = "a = -5"
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    expected: list = [
        Assign(
            "a",
            UnaryOperation("-", Literal(5))
        )
    ]
    
    assert ast == expected


def test_console_log_literal():
    source: str = "console_log 5"
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    expected: list = [
        ConsoleLog(Literal(5))
    ]
    
    assert ast == expected


def test_console_log_variable():
    source: str = "console_log a"
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    expected: list = [
        ConsoleLog(Variable("a"))
    ]
    
    assert ast == expected


def test_console_log_expression():
    source: str = "console_log a + 2"
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    expected: list = [
        ConsoleLog(
            BinaryOperation(
                Variable("a"),
                "+",
                Literal(2)
            )
        )
    ]
    
    assert ast == expected


def test_multiple_statements():
    source: str = """
    a = 5
    b = 10
    console_log a
    """
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    expected: list = [
        Assign("a", Literal(5)),
        Assign("b", Literal(10)),
        ConsoleLog(Variable("a"))
    ]
    
    assert ast == expected


def test_semicolon_separator():
    source: str = "a = 5; b = 10; console_log a"
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    expected: list = [
        Assign("a", Literal(5)),
        Assign("b", Literal(10)),
        ConsoleLog(Variable("a"))
    ]
    
    assert ast == expected


def test_consecutive_separators():
    source: str = """
    a = 5;;;

    ;b = 10
    """
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    expected: list = [
        Assign("a", Literal(5)),
        Assign("b", Literal(10))
    ]
    
    assert ast == expected


def test_invalid_primary():
    source: str = "*5"
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    
    with pytest.raises(SyntaxError):
        parser.parse()


def test_invalid_expression():
    source: str = "5 +"
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    
    with pytest.raises(SyntaxError):
        parser.parse()


def test_invalid_assignment():
    source: str = "a ="
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    
    with pytest.raises(SyntaxError):
        parser.parse()


def test_invalid_console_log():
    source: str = "console_log"
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    
    with pytest.raises(SyntaxError):
        parser.parse()
