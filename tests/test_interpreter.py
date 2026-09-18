from teo.ast.expression import (
    Literal,
    Variable,
    BinaryOperation,
    UnaryOperation,
)
from teo.ast.statement import (
    ExpressionStatement,
    Assign,
    ConsoleLog,
)
from teo.interpreter.interpreter import Interpreter
import pytest


def test_literal():
    interpreter = Interpreter()

    result = interpreter.evaluate(Literal(5))

    assert result == 5


def test_variable():
    interpreter = Interpreter()

    interpreter.execute(
        Assign("a", Literal(5))
    )

    result = interpreter.evaluate(
        Variable("a")
    )

    assert result == 5


def test_binary_operation():
    interpreter = Interpreter()

    expressions = [
        (BinaryOperation(Literal(5), "+", Literal(10)), 15),
        (BinaryOperation(Literal(10), "-", Literal(5)), 5),
        (BinaryOperation(Literal(5), "*", Literal(10)), 50),
        (BinaryOperation(Literal(10), "/", Literal(2)), 5)
    ]

    for expression, expected in expressions:
        assert interpreter.evaluate(expression) == expected


def test_unary_operation():
    interpreter = Interpreter()

    expressions = [
        (UnaryOperation("-", Literal(5)), -5),
        (UnaryOperation("+", Literal(5)), 5)
    ]

    for expression, expected in expressions:
        assert interpreter.evaluate(expression) == expected


def test_expression_statement():
    interpreter = Interpreter()

    statement = ExpressionStatement(
        BinaryOperation(
            Literal(5), 
            "+", 
            Literal(10)
        )
    )

    result = interpreter.execute(statement)

    assert result == 15


def test_assignment():
    interpreter = Interpreter()

    interpreter.execute(
        Assign("a", Literal(5))
    )

    assert interpreter.global_env.get("a") == 5

    interpreter.execute(
        Assign("a", Literal(10))
    )

    assert interpreter.global_env.get("a") == 10


def test_local_assignment():
    interpreter = Interpreter()

    interpreter.execute(
        Assign("a", Literal(5), is_local=True)
    )

    assert interpreter.global_env.get("a") == 5


def test_local_assignment_existing_variable():
    interpreter = Interpreter()

    interpreter.execute(
        Assign("a", Literal(5), is_local=True)
    )

    with pytest.raises(NameError):
        interpreter.execute(
            Assign("a", Literal(10), is_local=True)
        )


def test_assignment_expression():
    interpreter = Interpreter()

    interpreter.execute(
        Assign("a", Literal(5))
    )

    expression = BinaryOperation(
        Variable("a"),
        "+",
        Literal(10)
    )

    assert interpreter.evaluate(expression) == 15


def test_console_log(capsys):
    interpreter = Interpreter()

    interpreter.execute(
        ConsoleLog(Literal(5))
    )

    captured = capsys.readouterr()

    assert captured.out == "5\n"


def test_console_log_variable(capsys):
    interpreter = Interpreter()

    interpreter.execute(
        Assign("a", Literal(5))
    )

    interpreter.execute(
        ConsoleLog(Variable("a"))
    )

    captured = capsys.readouterr()

    assert captured.out == "5\n"


def test_binary_operation_with_variables():
    interpreter = Interpreter()

    interpreter.execute(Assign("a", Literal(5)))
    interpreter.execute(Assign("b", Literal(10)))

    expression = BinaryOperation(
        Variable("a"),
        "+",
        Variable("b")
    )

    assert interpreter.evaluate(expression) == 15


def test_comparations1():
    interpreter = Interpreter()

    expression = BinaryOperation(
        Literal(2),
        "<",
        Literal(3)
    )

    assert interpreter.evaluate(expression) == True


def test_comparations2():
    interpreter = Interpreter()

    expression = BinaryOperation(
        Literal("2"),
        ">",
        Literal("3")
    )

    assert interpreter.evaluate(expression) == False


def test_comparations3():
    interpreter = Interpreter()

    expression = BinaryOperation(
        Literal(2),
        "==",
        Literal(2)
    )

    assert interpreter.evaluate(expression) == True


def test_comparations4():
    interpreter = Interpreter()

    expression = BinaryOperation(
        Literal(2),
        "!=",
        Literal(3)
    )

    assert interpreter.evaluate(expression) == True


def test_comparations5():
    interpreter = Interpreter()

    expression = BinaryOperation(
        Literal(2),
        "<=",
        Literal(2)
    )

    assert interpreter.evaluate(expression) == True


def test_comparations6():
    interpreter = Interpreter()

    expression = BinaryOperation(
        Literal(2),
        ">=",
        Literal(3)
    )

    assert interpreter.evaluate(expression) == False


def test_comparations7():
    interpreter = Interpreter()

    expression = BinaryOperation(
        BinaryOperation(
            Literal(2),
            "+",
            Literal(3)
        ),
        "<",
        Literal(10)
    )

    assert interpreter.evaluate(expression) == True


def test_comparations8():
    interpreter = Interpreter()

    expression = BinaryOperation(
        BinaryOperation(
            Literal(2),
            "*",
            Literal(3)
        ),
        ">=",
        Literal(6)
    )

    assert interpreter.evaluate(expression) == True